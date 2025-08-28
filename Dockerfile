# Usa uma imagem base leve do Python
FROM python:3.12-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo de dependências para o contêiner
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia a pasta de modelos e a pasta da API
COPY models/ ./models/
COPY api/ ./api/

# Define a variável de ambiente para o Flask
ENV FLASK_APP=api/freight_api/freight_api.py

# Define a porta que o Flask vai usar
EXPOSE 5000

# Comando para rodar a aplicação quando o contêiner for iniciado
CMD ["flask", "run", "--host=0.0.0.0"]
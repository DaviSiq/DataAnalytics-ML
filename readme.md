### **Pipeline de Análise e Machine Learning para E-commerce**

Este projeto é uma solução de dados de ponta a ponta que processa dados de transações do **Olist E-commerce Public Dataset** para gerar insights de negócio e construir modelos preditivos. O objetivo principal foi demonstrar a capacidade de construir um pipeline completo, desde a análise exploratória até a operacionalização de modelos de Machine Learning.

---

#### **1. Destaques e Resultados Principais**

* **Modelagem Preditiva de Alta Precisão:**
    * **Previsão de Frete:** Desenvolvido um modelo de regressão para prever o valor do frete (`freight_value`) com base nas características do produto e localizações do cliente/vendedor. O modelo alcançou um **R² de 0.96** e um **Erro Médio Absoluto (MAE) de R$ 1.17**, provando-se como o modelo mais robusto e útil do projeto.
    * **Previsão de Satisfação:** Construído um modelo de classificação para prever se um cliente ficaria satisfeito. O modelo alcançou uma **Acurácia de 96%**, demonstrando a capacidade de identificar clientes em potencial risco de insatisfação.
    
* **Análise de Clusterização e Insights de Negócio:**
    * O algoritmo `K-Means` foi utilizado para segmentar a base de clientes em 4 grupos distintos, como "Clientes Ativos" e "Clientes Insatisfeitos", permitindo a criação de estratégias de marketing direcionadas.

* **Resumo da Análise Exploratória (EDA):**
    * Identificação de que a maioria dos pedidos se origina em **São Paulo (SP)**.
    * **Atrasos Regionais**: Os estados com maior frequência de atrasos na entrega são BA, RJ, ES e SC, nesta ordem.
    * O **cartão de crédito** é o método de pagamento preferido, e o pico de compras ocorre na **segunda-feira** no período da tarde.
    * **Horário de Pico** : O horário com maior volume de compras é 16h. No entanto, o período entre 12h e 17h é o mais ativo do dia, seguido de um segundo pico entre 20h e 21h. 
    
---

#### **2. Metodologias e Tecnologias**

* **Data Wrangling:** Processamento de dados de `Data Warehouse` (`Snowflake`), limpeza e engenharia de features com `Pandas`.
* **Modelagem:** Aplicação de algoritmos de `Machine Learning` como `Random Forest`, `XGBoost`, `K-Means` e `Logistic Regression`.
* **Implantação:** Demonstração de um fluxo de trabalho de deploy de `API` usando `Docker`, tornando o projeto portátil e pronto para produção.
* **Ferramentas:** Python, Scikit-learn, Joblib, Matplotlib, Docker.

---

#### **3. Como Testar o Modelo de Frete Localmente**

Para testar a API, use um terminal para rodar o contêiner e outro para enviar a requisição JSON.

1.  **Construir a Imagem Docker:**
    ```sh
    docker build -t freight-api .
    ```
2.  **Rodar a API:**
    ```sh
    docker run -p 5000:5000 freight-api
    ```
3.  **Enviar a Requisição:**
    ```sh
    # Exemplo de requisição Postman
    POST [http://127.0.0.1:5000/predict_freight](http://127.0.0.1:5000/predict_freight)
    Content-Type: application/json
    
    {
      "price": 59.90,
      "product_weight_g": 1000,
      "product_volume_cm3": 5000,
      "product_length_cm": 30,
      "product_height_cm": 15,
      "product_width_cm": 20,
      "customer_state": "SP",
      "seller_state": "RJ"
    }
    ```
### **Análise de Dados e Machine Learning em E-commerce**

**Objetivo do Estudo:**

Este projeto tem como objetivo principal o aprimoramento e a aplicação prática de conceitos de `Data Science` e `Machine Learning`. A partir do **Olist Brazilian E-commerce Public Dataset**, este estudo visa dominar um pipeline completo de dados, desde a análise exploratória até a implantação de modelos preditivos, servindo como uma demonstração das habilidades adquiridas em todo o processo.

---

#### **Metodologias e Habilidades Adquiridas:**

* **Data Wrangling e Engenharia de Features:**
    * Prática em `ETL` (`Extração, Transformação e Carga`) de dados de múltiplas tabelas.
    * Utilização de `Pandas` e `Numpy` para limpeza de dados, padronização, e tratamento de valores ausentes.
    * Criação de features avançadas, como métricas `RFM` (`Recência, Frequência, Valor Monetário`) e variáveis de tempo (`timestamps`), essenciais para a modelagem.
    * `Data Warehouse`: Utilização e integração com um ambiente de `Snowflake` para o acesso aos dados.

* **Modelagem Preditiva e Analítica:**
    * **Análise de Churn:** Construção de um modelo de `classificação` para identificar clientes em risco de evasão, usando `Random Forest` e `XGBoost`.
    * **Análise de Clusterização:** Segmentação de clientes com base em seu comportamento de compra (`RFM`) usando o algoritmo `K-Means` para encontrar grupos de clientes com perfis distintos.
    * **Regressão:** Prática com modelos de `regressão` para prever valores contínuos como o `faturamento mensal` (como estudo de caso) e o `valor do próximo pedido` de um cliente.
    * **Controle de Qualidade:** Identificação e resolução de problemas comuns como `data leakage` e `inconsistência de dados` no pipeline.

* **Implantação de Modelos (MLOps):**
    * **Serialização de Modelos:** Uso de `joblib` para salvar modelos treinados e objetos de pré-processamento (`StandardScaler`, `OneHotEncoder`).
    * **API:** Criação de uma `API RESTful` (`Flask`) para operacionalizar os modelos de `ML`, permitindo que previsões sejam feitas em tempo real a partir de requisições externas.
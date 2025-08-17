### **Modelos de Machine Learning do Projeto**

Este diretório contém os artefatos dos modelos preditivos e analíticos desenvolvidos, serializados no formato `joblib` para serem utilizados em ambientes de produção através de APIs.

---

#### **1. Modelagem Preditiva**

* **Modelo de Previsão de Satisfação do Cliente**
    * **Tipo:** Classificação (`Random Forest Classifier`).
    * **Objetivo:** Prever se um cliente dará uma nota de avaliação >= 4 (`is_satisfied = 1`) ou não.
    * **Features:** `price`, `freight_value`, `product_weight_g`, `product_volume_cm3`, e `customer_state`.
    * **Desempenho:** Acurácia de aproximadamente **96%**.

* **Modelo de Previsão de Churn**
    * **Tipo:** Classificação (`XGBoost Classifier`).
    * **Objetivo:** Prever a probabilidade de um cliente se tornar inativo (`is_churn = 1`).
    * **Features:** Métricas `RFM` (`frequency_orders`, `monetary_value`) e `review_score`.
    * **Desempenho:** Acurácia de aproximadamente **90%**.

* **Modelo de Regressão (Estudo de Caso)**
    * **Tipo:** Regressão (`Random Forest Regressor`, `Linear Regression`).
    * **Objetivo:** Prever o faturamento mensal (modelo inconclusivo devido à escassez de dados).

---

#### **2. Análise de Clusterização**

* **Modelo:** `K-Means`.
* **Objetivo:** Segmentar a base de clientes em grupos com perfis de comportamento distintos.
* **Features:** Métricas `RFM` (`recency_days`, `frequency_orders`, `monetary_value`) e `review_score`.
* **Resultado:** 4 segmentos de clientes, que podem ser interpretados como "Clientes Campeões", "Clientes Ativos", "Clientes Hibernando" e "Clientes Insatisfeitos".
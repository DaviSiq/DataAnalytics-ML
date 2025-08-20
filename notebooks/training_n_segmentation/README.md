### **Modelos de Machine Learning do Projeto**

Este diretório contém os artefatos dos modelos preditivos e analíticos desenvolvidos, serializados no formato `joblib` para serem utilizados em ambientes de produção através de APIs.

---

#### **1. Modelagem Preditiva**

* **Modelo de Previsão de Satisfação do Cliente**
    * **Tipo:** Classificação (`Random Forest Classifier`).
    * **Objetivo:** Prever se um cliente dará uma nota de avaliação >= 4 (`is_satisfied = 1`) ou não.
    * **Features:** `price`, `freight_value`, `product_weight_g`, `product_volume_cm3`, e `customer_state`.
    * **Desempenho:** Acurácia de aproximadamente **96%**.

* **Modelo de Previsão do Valor do Frete (Modelo Principal)**
    * **Tipo:** Regressão (`Random Forest Regressor`).
    * **Objetivo:** Prever o valor do frete (`freight_value`) com base nas características físicas do produto e nas localizações do cliente e vendedor.
    * **Features:** `price`, `product_weight_g`, `product_volume_cm3`, `product_length_cm`, `product_height_cm`, `product_width_cm`, `customer_state`, e `seller_state`.
    * **Desempenho:** `R²` de **0.96**, **MAE** de **R$ 1.17** e **RMSE** de **R$ 3.22**.

* **Modelo de Regressão (Estudo de Caso)**
    * **Tipo:** Regressão (`Random Forest Regressor`, `Linear Regression`).
    * **Objetivo:** Prever o faturamento mensal (modelo inconclusivo devido à escassez de dados).

---

#### **2. Análise de Clusterização**

* **Modelo:** `K-Means`.
* **Objetivo:** Segmentar a base de clientes em grupos com perfis de comportamento distintos.
* **Features:** Métricas `RFM` (`recency_days`, `frequency_orders`, `monetary_value`) e `review_score`.
* **Resultado:** 4 segmentos de clientes, que podem ser interpretados como "Clientes Campeões", "Clientes Ativos", "Clientes Hibernando" e "Clientes Insatisfeitos".

##### **Estratégias de Negócio por Cluster**

A partir da segmentação, é possível criar estratégias de negócio específicas para cada grupo:

* **Clientes em Potencial:** Foco em campanhas de retenção ou incentivos para uma segunda compra.
* **Clientes Ativos e Recorrentes:** Investigar por que estão se tornando inativos para evitar a evasão.
* **Clientes Hibernando:** Foco em campanhas de reativação com ofertas agressivas, já que a satisfação no passado foi alta.
* **Clientes Insatisfeitos e Perigosos:** Foco em análise de causa-raiz para entender o problema e evitar danos à reputação.
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Helper Function to Load Data ---
@st.cache_data
def load_data(path):
    """Loads a CSV file and handles potential errors."""
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        st.error(f"Error: The file {path} was not found. Please ensure it exists.")
        return None

# --- Main Dashboard Structure ---
st.set_page_config(page_title="Olist E-commerce Dashboard", layout="wide")

st.title("📊 Olist E-commerce Analytics Dashboard")
st.markdown("### Análise e Insights de Vendas e Clientes")

# --- Load Datasets ---
# Adjust the path based on your file structure
customer_segments_path = os.path.join('notebooks', 'training_n_segmentation', 'olist_customer_segments.csv')
monthly_revenue_path = os.path.join('notebooks', 'training_n_segmentation', 'olist_monthly_revenue.csv')

df_segments = load_data(customer_segments_path)
df_revenue = load_data(monthly_revenue_path)


# --- Section 1: Customer Segmentation ---
st.header("1. Segmentação de Clientes (K-Means)")
if df_segments is not None:
    st.markdown("##### Média das métricas RFM por Cluster")
    # Group by cluster and get the mean of the features
    cluster_summary = df_segments.groupby('cluster')[['recency_days', 'frequency_orders', 'monetary_value', 'review_score']].mean()
    st.dataframe(cluster_summary)

    st.markdown("##### Visualização dos Clusters")
    # Create a simple bar chart to visualize cluster sizes
    st.bar_chart(df_segments['cluster'].value_counts(), use_container_width=True)

    # You can also use Matplotlib for more custom charts
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        data=df_segments,
        x='recency_days',
        y='monetary_value',
        hue='cluster',
        style='cluster',
        ax=ax
    )
    plt.title("Visualização 2D de Recência vs. Valor")
    st.pyplot(fig)


# --- Section 2: Revenue Forecasting Analytics ---
st.header("2. Análise de Faturamento Mensal")
if df_revenue is not None:
    # Ensure the date column is in datetime format
    df_revenue['data'] = pd.to_datetime(df_revenue['data'])
    st.dataframe(df_revenue.set_index('data'))
    
    st.markdown("##### Faturamento Total ao Longo do Tempo")
    st.line_chart(df_revenue.set_index('data')['faturamento_mensal'])

    st.markdown("##### Faturamento Mensal vs. Faturamento do Mês Anterior")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df_revenue, x='faturamento_mensal', y='faturamento_mes_anterior', ax=ax)
    plt.title("Faturamento Atual vs. Mês Anterior")
    st.pyplot(fig)


# --- How to Run the Dashboard ---
st.sidebar.header("Como Executar")
st.sidebar.markdown(
    """
    Para executar o dashboard:
    1. Certifique-se de que o ambiente Python está ativo.
    2. No terminal, execute o comando:
       `streamlit run app.py`
    3. O dashboard será aberto automaticamente no seu navegador.
    """
)
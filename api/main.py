from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
import os

# --- 1. Carregando Todos os Modelos e Pré-processadores ---
# Define os caminhos para o modelo de satisfação e o encoder
# 💡 NOTA: Ajuste esses caminhos se a sua estrutura de pastas for diferente
satisfied_model_path = os.path.join('models', 'is_satisfied_model', 'rf_classifier_satisfied.joblib')
satisfied_encoder_path = os.path.join('models', 'is_satisfied_model', 'one_hot_encoder.joblib')

# Define os caminhos para o modelo de churn e o scaler
churn_model_path = os.path.join('models', 'churn_rate_model', 'rf_churn_classifier.joblib')
churn_scaler_path = os.path.join('models', 'churn_rate_model', 'rfm_scaler.joblib')
customer_segments_path = os.path.join('notebooks', 'olist_customer_segments.csv')


try:
    satisfied_model = joblib.load(satisfied_model_path)
    satisfied_encoder = joblib.load(satisfied_encoder_path)
    
    churn_model = joblib.load(churn_model_path)
    churn_scaler = joblib.load(churn_scaler_path)

    df_customer_segments = pd.read_csv(customer_segments_path)
    df_customer_segments.set_index('customer_id', inplace=True)
    
    print("Todos os modelos e pré-processadores foram carregados com sucesso!")
except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado. Verifique se os caminhos e os nomes estão corretos: {e}")
    exit()

# Define as listas de features para cada modelo (alinhadas com o treinamento)
satisfied_numeric_features = [
    'price', 'freight_value', 'payment_installments',
     'product_weight_g', 'product_volume_cm3'
]
satisfied_categorical_features = ['customer_state']

churn_features = ['frequency_orders', 'monetary_value', 'review_score']


app = Flask(__name__)

# --- Rota para prever a satisfação do cliente ---
@app.route('/predict_satisfied', methods=['POST'])
def predict_satisfied():
    try:
        data = request.get_json(force=True)
    except Exception as e:
        return jsonify({"error": "Formato de JSON inválido.", "details": str(e)}), 400

    input_df = pd.DataFrame([data])
    
    for col in satisfied_numeric_features:
        if col not in input_df.columns:
            input_df[col] = np.nan
        input_df[col] = pd.to_numeric(input_df[col], errors='coerce').fillna(0)
    
    try:
        state_encoded = satisfied_encoder.transform(input_df[satisfied_categorical_features])
        encoded_df = pd.DataFrame(
            state_encoded,
            columns=satisfied_encoder.get_feature_names_out(satisfied_categorical_features)
        )
    except ValueError as e:
        return jsonify({"error": "Valor categórico inválido. O estado deve ser um dos estados do treinamento.", "details": str(e)}), 400

    X_input = pd.concat([input_df[satisfied_numeric_features], encoded_df], axis=1)

    prediction = satisfied_model.predict(X_input)
    prediction_proba = satisfied_model.predict_proba(X_input)

    result = "Satisfeito" if prediction[0] == 1 else "Insatisfeito"

    return jsonify({
        'predicted_satisfaction': result,
        'probability_satisfied': float(prediction_proba[0][1]),
        'probability_not_satisfied': float(prediction_proba[0][0])
    })


# --- Rota para prever o risco de Churn ---
@app.route('/predict_churn', methods=['POST'])
def predict_churn():
    try:
        data = request.get_json(force=True)
        customer_id = data.get('customer_id')
        if not customer_id:
            return jsonify({"error": "customer_id não fornecido no JSON."}), 400
    except Exception as e:
        return jsonify({"error": "Formato de JSON inválido.", "details": str(e)}), 400
    
    if customer_id not in df_customer_segments.index:
        return jsonify({"error": "customer_id não encontrado na base de dados de clientes."}), 404
    
    customer_data = df_customer_segments.loc[customer_id]
    
    X_input_scaled = churn_scaler.transform(pd.DataFrame(customer_data[churn_features]).transpose())

    prediction = churn_model.predict(X_input_scaled)
    prediction_proba = churn_model.predict_proba(X_input_scaled)

    churn_result = "Risco de Churn" if prediction[0] == 1 else "Sem Risco de Churn"
    churn_probability = prediction_proba[0][1]

    return jsonify({
        'predicted_churn': churn_result,
        'probability_of_churn': float(churn_probability),
        'probability_of_no_churn': float(prediction_proba[0][0])
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
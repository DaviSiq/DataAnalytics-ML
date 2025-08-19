from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import OneHotEncoder

# --- Carregando o Modelo e Pré-processadores ---
# Define os caminhos para o modelo de Frete
model_path = os.path.join('models', 'freight_predict', 'rf_regressor_freight.joblib')
encoder_path = os.path.join( 'models', 'freight_predict', 'freight_encoder.joblib')
scaler_path = os.path.join('models', 'freight_predict', 'freight_scaler.joblib')

try:
    freight_model = joblib.load(model_path)
    freight_encoder = joblib.load(encoder_path)
    freight_scaler = joblib.load(scaler_path)
    print("Modelo de Frete e pré-processadores carregados com sucesso!")
except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado. Verifique se os caminhos e os nomes estão corretos: {e}")
    exit()

# Define as listas de features para o modelo de frete
freight_numeric_features = [
    'price', 'product_weight_g', 'product_volume_cm3', 'product_length_cm', 
    'product_height_cm', 'product_width_cm'
]
freight_categorical_features = ['customer_state', 'seller_state']

app = Flask(__name__)

# --- Rota para prever o valor do frete ---
@app.route('/predict_freight', methods=['POST'])
def predict_freight():
    try:
        data = request.get_json(force=True)
    except Exception as e:
        return jsonify({"error": "Formato de JSON inválido.", "details": str(e)}), 400
    
    input_df = pd.DataFrame([data])

    # Pré-processa os dados para o modelo de frete
    for col in freight_numeric_features + freight_categorical_features:
        if col not in input_df.columns:
            if col in freight_numeric_features:
                input_df[col] = np.nan
            else:
                input_df[col] = 'missing' # Placeholder para categoria ausente

    for col in freight_numeric_features:
        input_df[col] = pd.to_numeric(input_df[col], errors='coerce').fillna(0)

    try:
        encoded_features = freight_encoder.transform(input_df[freight_categorical_features])
        encoded_df = pd.DataFrame(
            encoded_features,
            columns=freight_encoder.get_feature_names_out(freight_categorical_features)
        )
    except ValueError as e:
        return jsonify({"error": "Valor categórico inválido.", "details": str(e)}), 400

    X_input = pd.concat([input_df[freight_numeric_features], encoded_df], axis=1)
    
    # Padroniza as features numéricas
    X_input_scaled = X_input.copy()
    X_input_scaled[freight_numeric_features] = freight_scaler.transform(X_input[freight_numeric_features])
    
    # Faz a previsão
    prediction = freight_model.predict(X_input_scaled)

    return jsonify({'predicted_freight_value': float(prediction[0])})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
import os

# Define os caminhos para o seu modelo e encoder
model_path = os.path.join('notebooks','models', 'rf_classifier_satisfied.joblib')
encoder_path = os.path.join('notebooks','models', 'one_hot_encoder.joblib')

try:
    model = joblib.load(model_path)
    one_hot_encoder = joblib.load(encoder_path)
    print("Modelos e encoder carregados com sucesso!")
except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado. Verifique se o caminho e o nome estão corretos: {e}")
    exit()

# 💡 CORREÇÃO: A lista de features deve ser a versão que você usou para treinar o modelo,
# incluindo as features de tempo de entrega que causam vazamento.
numeric_features = [
    'price', 'freight_value', 'payment_installments', 'total_delivery_time_hours',
    'shipping_time_hours', 'product_weight_g', 'product_volume_cm3'
]
categorical_features = ['customer_state']

app = Flask(__name__)

@app.route('/predict_satisfied', methods=['POST'])
def predict_satisfied():
    try:
        data = request.get_json(force=True)
    except Exception as e:
        return jsonify({"error": "Formato de JSON inválido.", "details": str(e)}), 400

    input_df = pd.DataFrame([data])
    
    # Pré-processa os dados
    for col in numeric_features:
        if col not in input_df.columns:
            input_df[col] = np.nan
        input_df[col] = pd.to_numeric(input_df[col], errors='coerce').fillna(0)
    
    try:
        state_encoded = one_hot_encoder.transform(input_df[categorical_features])
        encoded_df = pd.DataFrame(
            state_encoded,
            columns=one_hot_encoder.get_feature_names_out(categorical_features)
        )
    except ValueError as e:
        return jsonify({"error": "Valor categórico inválido. O estado deve ser um dos estados do treinamento.", "details": str(e)}), 400

    X_input = pd.concat([input_df[numeric_features], encoded_df], axis=1)

    prediction = model.predict(X_input)
    prediction_proba = model.predict_proba(X_input)

    result = "Satisfeito" if prediction[0] == 1 else "Insatisfeito"

    return jsonify({
        'predicted_satisfaction': result,
        'probability_satisfied': prediction_proba[0][1],
        'probability_not_satisfied': prediction_proba[0][0]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
import requests
import json

# URL da sua nova API de frete
url = 'http://127.0.0.1:5000/predict_freight'

# Dados de teste para enviar
data = {
    'price': 74.9,
    'product_weight_g': 107.0,
    'product_volume_cm3': 3211.0,
    'product_length_cm': 19.0,
    'product_height_cm': 13.0,
    'product_width_cm': 13.0,
    'customer_state': "SP",
    'seller_state': "PR"
}

headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(url, data=json.dumps(data), headers=headers)
    response.raise_for_status()
    print("Status Code:", response.status_code)
    print("Resultado da Previsão:", response.json())
except requests.exceptions.RequestException as e:
    print(f"Erro ao conectar ou receber resposta: {e}")
    print("Certifique-se de que a API está rodando em outro terminal.")
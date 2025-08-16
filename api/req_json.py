import requests
import json

# URL da sua API
url = 'http://127.0.0.1:5000/predict_satisfied'

# 💡 CORREÇÃO: Adicionados os atributos que o modelo espera.
data = {
  "price": 59.90,
  "freight_value": 15.20,
  "payment_installments": 1,
  "total_delivery_time_hours": 200, 
  "shipping_time_hours": 150,      
  "product_weight_g": 300,
  "product_volume_cm3": 1500,
  "customer_state": "SP"
}

headers = {'Content-Type': 'application/json'}

# Faz a requisição POST
response = requests.post(url, data=json.dumps(data), headers=headers)

# Imprime o resultado
print("Status Code:", response.status_code)
print("Resultado da Previsão:", response.json())
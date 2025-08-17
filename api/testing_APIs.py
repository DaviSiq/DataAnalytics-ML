import requests
import json
import os

# Define a URL base da sua API
base_url = 'http://127.0.0.1:5000'

# 💡 Customer ID de exemplo para os modelos de cliente
# Use um customer_id real do seu dataset de segmentos
customer_id_example = "f88197465ea7920adcdbec7375364d82"

headers = {'Content-Type': 'application/json'}

def test_predict_satisfied():
    print("--- Testando API '/predict_satisfied' ---")
    url = f"{base_url}/predict_satisfied"
    
    # Payload com todas as features necessárias para o modelo de satisfação
    data = {
      "price": 59.90,
      "freight_value": 15.20,
      "payment_installments": 1,
      #"shipping_time_hours": 150,      
      "product_weight_g": 300,
      "product_volume_cm3": 1500,
      "customer_state": "SP"
    }

    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status() # Lança um erro se o status não for 2xx
        print("Status Code:", response.status_code)
        print("Resultado da Previsão:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar ou receber resposta: {e}")
        print("Certifique-se de que a API está rodando em outro terminal.")

def test_predict_churn():
    print("\n--- Testando API '/predict_churn' ---")
    url = f"{base_url}/predict_churn"

    # Payload com o customer_id
    data = {"customer_id": customer_id_example}
    
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        print("Status Code:", response.status_code)
        print("Resultado da Previsão:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar ou receber resposta: {e}")
        print("Certifique-se de que a API está rodando em outro terminal.")


if __name__ == '__main__':
    test_predict_satisfied()
    print("-" * 50)
    print("-" * 50)
    test_predict_churn()
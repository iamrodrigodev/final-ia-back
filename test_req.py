import requests

# Test 1: Datos inválidos (Faltan campos o están fuera de rango)
body_invalido = {
    "estado_civil": 999,  # Fuera de rango (ge=1, le=6)
    "nota_admision": -50.0 # Fuera de rango (ge=0.0, le=200.0)
}

try:
    response = requests.post("http://127.0.0.1:8000/api/prediccion/", json=body_invalido)
    print("STATUS:", response.status_code)
    print("JSON:", response.json())
except Exception as e:
    print("Servidor no corriendo:", e)

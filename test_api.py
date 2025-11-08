import requests

data = {
    'Close': 9.92,
    'Volume': 2612828,
    'SMA_100': 9.22,
    'RSI_14': 64.53,
    'WTI_Close': 59.75
}

print("Enviando...")
response = requests.post("http://localhost:5001/predict", json=data)
print(response.json())
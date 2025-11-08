from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('best_model.pkl')
features = joblib.load('data/features.pkl')

print(f"Features esperadas: {features}")  # DEBUG

def calculate_features(data):
    # --- Recibir solo 5 valores ---
    close = data['Close']
    volume = data['Volume']
    sma_100 = data['SMA_100']
    rsi_14 = data['RSI_14']
    wti_close = data['WTI_Close']
    
    # --- Calcular las derivadas ---
    overbought = 1 if rsi_14 > 70 else 0
    oversold = 1 if rsi_14 < 30 else 0
    below_sma = 1 if close < sma_100 else 0
    high_volume = 1 if volume > 1_000_000 else 0  # Ajusta si necesitas
    wti_change = 0.0
    ec_wti_ratio = close / (wti_close + 1e-8)
    wti_volatility = 2.0  # Valor promedio
    
    # --- CREAR LISTA CON ORDEN EXACTO ---
    row = [
        close, volume, sma_100, rsi_14,
        overbought, oversold, below_sma, high_volume,
        wti_close, wti_change, ec_wti_ratio, wti_volatility
    ]
    
    # --- CREAR DATAFRAME CON ORDEN EXACTO ---
    df = pd.DataFrame([row], columns=features)
    
    return df

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        required = ['Close', 'Volume', 'SMA_100', 'RSI_14', 'WTI_Close']
        if not all(k in data for k in required):
            return jsonify({'error': f'Faltan: {required}'}), 400
            
        df = calculate_features(data)
        pred = int(model.predict(df)[0])
        prob = float(model.predict_proba(df)[0][pred])
        
        return jsonify({
            'prediction': pred,
            'confidence': round(prob, 3),
            'meaning': '0 = SUBE mañana' if pred == 0 else '1 = BAJA mañana'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
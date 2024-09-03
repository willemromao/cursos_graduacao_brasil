from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Carregando o modelo, scaler, encoder e label encoder salvos
model = joblib.load('/app/model/model.joblib')
scaler = joblib.load('/app/model/scaler.joblib')
encoder = joblib.load('/app/model/encoder.joblib')
label_encoder = joblib.load('/app/model/label_encoder.joblib')

# Definindo as colunas que foram codificadas e normalizadas
categorical_features = ['CATEGORIA_ADMINISTRATIVA', 'ORGANIZACAO_ACADEMICA', 'GRAU', 'MODALIDADE', 'REGIAO']
numeric_features = ['QT_VAGAS_AUTORIZADAS', 'CARGA_HORARIA']

# Endpoint para previsão
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Recebendo os dados de entrada em formato JSON
        input_data = request.json
        
        # Convertendo os dados de entrada para um DataFrame
        df = pd.DataFrame([input_data])

        # Aplicando a codificação binária nas colunas categóricas usando o encoder carregado
        df_encoded = encoder.transform(df[categorical_features])

        # Substituindo as colunas originais pelas codificadas
        df = df.drop(columns=categorical_features)
        df_encoded_df = pd.DataFrame(df_encoded, columns=encoder.get_feature_names_out())
        df = pd.concat([df, df_encoded_df], axis=1)

        # Aplicando a normalização nas colunas numéricas usando o scaler carregado
        df[numeric_features] = scaler.transform(df[numeric_features])

        # Convertendo o DataFrame para um array numpy para previsão
        input_array = df.values

        # Fazendo a previsão com o modelo
        prediction = model.predict(input_array)

        # Mapear a previsão para a classe original
        class_label = label_encoder.inverse_transform(prediction)[0]

        # Retornando o resultado
        return jsonify({'prediction': class_label})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


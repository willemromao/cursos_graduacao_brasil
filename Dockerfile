# Imagem base do Python
FROM python:3.10-slim

# Diretório de trabalho
WORKDIR /app

# Copia do arquivo de requirements e instação de dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia dos arquivos da aplicação
COPY app /app/

# Comando padrão para iniciar os serviços
CMD ["sh", "-c", "python flask_app.py & streamlit run streamlit_app.py"]

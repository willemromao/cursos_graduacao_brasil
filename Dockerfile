# Use uma imagem base com Python
FROM python:3.10-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requirements e instale as dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copie os arquivos da aplicação
COPY app /app/

# Defina o comando padrão para iniciar o Flask API
CMD ["sh", "-c", "python flask_app.py & streamlit run streamlit_app.py"]

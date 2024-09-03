# Imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de requisitos e instalar as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos da aplicação
COPY . /app/

# Expor a porta em que o Streamlit vai rodar
EXPOSE 8501

# Comando para rodar a aplicação Streamlit
CMD ["streamlit", "run", "streamlit_app.py"]

# imagem base do Python
FROM python:3.9-slim

# Diretório de trabalho
WORKDIR /app

# Copiar os arquivos de requisitos e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos da aplicação
COPY . /app/

# Expor a porta em que o Flask vai rodar
EXPOSE 5000

# Rodar a aplicação Flask
CMD ["python", "flask_app.py"]

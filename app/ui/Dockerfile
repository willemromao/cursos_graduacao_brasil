FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ui.py .

EXPOSE 8501

CMD ["streamlit", "run", "ui.py", "--server.port=8501", "--server.address=0.0.0.0"]

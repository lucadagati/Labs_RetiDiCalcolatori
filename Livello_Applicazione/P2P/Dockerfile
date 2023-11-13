# Usa un'immagine di base Python
FROM python:3.9

# Copia il tuo codice nella directory dell'applicazione nel container
WORKDIR /app
COPY . /app

# Installa le dipendenze del tuo codice
RUN pip install asyncio

# Comando di esecuzione dell'applicazione
CMD ["python", "main.py"]

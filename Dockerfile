FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Precarga el modelo en la imagen para no descargarlo en cada deploy
RUN python -c "from transformers import pipeline; pipeline('image-classification', model='imzynoxprince/pokemons-image-classifier-gen1-gen9')"

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
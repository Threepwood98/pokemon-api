from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
from PIL import Image
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Luego restringe esto a tu dominio de Astro
    allow_methods=["*"],
    allow_headers=["*"]
)

print("Cargando modelo... (puede tardar 1-2 min la primera vez)")
classifier = pipeline(
    "image-classification",
    model="imzynoxprince/pokemons-image-classifier-gen1-gen9"
)
print("Modelo listo ✅")

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/identificar")
async def identificar_pokemon(file: UploadFile = File(...)):
    contenido = await file.read()
    imagen = Image.open(io.BytesIO(contenido)).convert("RGB")
    resultado = classifier(imagen, top_k=3)
    return {"predicciones": resultado}
```

**`requirements.txt`**
```
fastapi
uvicorn
transformers
torch --index-url https://download.pytorch.org/whl/cpu
Pillow
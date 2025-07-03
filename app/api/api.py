from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict
import joblib
import pickle
import pandas as pd
import uvicorn
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models/trained/best_model_random_forest.joblib"
PREPROCESSOR_PATH = BASE_DIR / "models/pipelines/preprocessor.pkl"

app = FastAPI(
    title="API de Previsão de Extinção de Cursos",
    description="API para previsão da extinção de cursos de graduação no Brasil usando Random Forest",
    version="2.0.0"
)

try:
    model = joblib.load(MODEL_PATH)
    with open(PREPROCESSOR_PATH, "rb") as f:
        preprocessor = pickle.load(f)
    
    # pré-compute máscara para remover todas as colunas de EXTINTO após o transform
    feature_names = preprocessor.get_feature_names_out()
    extinto_mask = ['EXTINTO' not in name for name in feature_names]

except Exception as e:
    print(f"Erro ao carregar modelo ou preprocessor: {e}")
    model = None
    preprocessor = None
    extinto_mask = None

class CourseInput(BaseModel):
    GRAU: str = Field(..., example="Tecnológico")
    MODALIDADE: str = Field(..., example="Educação a Distância")
    CATEGORIA_ADMINISTRATIVA: str = Field(..., example="Privada com fins lucrativos")
    ORGANIZACAO_ACADEMICA: str = Field(..., example="Centro Universitário")
    REGIAO: str = Field(..., example="SUDESTE")
    QT_VAGAS_AUTORIZADAS: str = Field(..., example="101-200")
    CARGA_HORARIA: str = Field(..., example="2001-3000h")

class ExtinctionPrediction(BaseModel):
    extincao_predita: str
    probabilidade: float

@app.get("/", response_model=Dict[str, str])
async def root():
    return {
        "message": "API para previsão de extinção de cursos está online",
        "modelo": "Random Forest",
        "documentação": "/docs"
    }

@app.get("/health")
async def health_check():
    status = "healthy" if model and preprocessor else "unhealthy"
    return {
        "status": status,
        "model_loaded": model is not None,
        "preprocessor_loaded": preprocessor is not None
    }

@app.get("/info")
async def model_info():
    try:
        return {
            "model_type": "Random Forest",
            "variavel_alvo": "EXTINTO (Sim/Não)",
            "input_features": list(CourseInput.__fields__.keys()),
            "processed_features": preprocessor.get_feature_names_out().tolist()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Falha ao obter informações: {e}")

@app.post("/predict", response_model=ExtinctionPrediction)
async def predict(course: CourseInput):
    if model is None or preprocessor is None or extinto_mask is None:
        raise HTTPException(
            status_code=500,
            detail="Modelo ou preprocessor não foi carregado corretamente."
        )

    try:
        input_df = pd.DataFrame([course.dict()])

        # Mantém o dummy 'EXTINTO' apenas para satisfazer o preprocessor
        input_df["EXTINTO"] = "Não"

        # Aplica o pré-processamento
        transformed_df = pd.DataFrame(transformed, columns=feature_names)
        X_for_model = transformed_df.loc[:, extinto_mask]

        # Remove todas as colunas geradas para EXTINTO antes de alimentar o modelo
        X_for_model = transformed[:, extinto_mask]

        # Faz a predição com o modelo
        proba = model.predict_proba(X_for_model)[0][1]
        pred_label = "Sim" if proba >= 0.5 else "Não"

        return ExtinctionPrediction(
            extincao_predita=pred_label,
            probabilidade=round(float(proba), 4)
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar a predição: {e}")

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000)

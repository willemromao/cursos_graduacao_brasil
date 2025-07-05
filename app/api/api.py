import pandas as pd
import pickle
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from typing import Dict, Any
import time
from pathlib import Path
import uvicorn

app = FastAPI(
    title="API de Predição de Extinção de Cursos",
    description="Prediz se um curso de graduação está em risco de extinção",
    version="2.0.0"
)


# Modelos de dados
class Grau(str, Enum):
    TECNOLOGICO = "Tecnológico"
    BACHARELADO = "Bacharelado"
    LICENCIATURA = "Licenciatura"
    SEQUENCIAL = "Sequencial"
    ABI = "Área Básica de Ingresso (ABI)"

class Modalidade(str, Enum):
    EAD = "Educação a Distância"
    PRESENCIAL = "Educação Presencial"

class CategoriaAdministrativa(str, Enum):
    PRIVADA_COM_FINS = "Privada com fins lucrativos"
    PRIVADA_SEM_FINS = "Privada sem fins lucrativos"
    PUBLICA_FEDERAL = "Pública Federal"
    PUBLICA_ESTADUAL = "Pública Estadual"
    PUBLICA_MUNICIPAL = "Pública Municipal"
    ESPECIAL = "Especial"

class OrganizacaoAcademica(str, Enum):
    CENTRO_UNIVERSITARIO = "Centro Universitário"
    UNIVERSIDADE = "Universidade"
    FACULDADE = "Faculdade"
    INSTITUTO_FEDERAL = "Instituto Federal de Educação, Ciência e Tecnologia"
    CEFET = "Centro Federal de Educação Tecnológica"

class Regiao(str, Enum):
    SUDESTE = "SUDESTE"
    SUL = "SUL"
    NORDESTE = "NORDESTE"
    CENTRO_OESTE = "CENTRO-OESTE"
    NORTE = "NORTE"

class VagasAutorizadas(str, Enum):
    MAIS_1000 = "Mais de 1000"
    DE_501_1000 = "501-1000"
    DE_201_500 = "201-500"
    DE_51_100 = "51-100"
    DE_101_200 = "101-200"
    ATE_50 = "Até 50"

class CargaHoraria(str, Enum):
    DE_3001_4000 = "3001-4000h"
    DE_1001_2000 = "1001-2000h"
    DE_2001_3000 = "2001-3000h"
    DE_4001_5000 = "4001-5000h"
    MAIS_5000 = "Mais de 5000h"
    ATE_1000 = "Até 1000h"

class CourseInput(BaseModel):
    GRAU: Grau
    MODALIDADE: Modalidade
    CATEGORIA_ADMINISTRATIVA: CategoriaAdministrativa
    ORGANIZACAO_ACADEMICA: OrganizacaoAcademica
    REGIAO: Regiao
    QT_VAGAS_AUTORIZADAS: VagasAutorizadas
    CARGA_HORARIA: CargaHoraria
    
    class Config:
        json_schema_extra = {
            "example": {
                "GRAU": "Bacharelado",
                "MODALIDADE": "Educação Presencial",
                "CATEGORIA_ADMINISTRATIVA": "Privada com fins lucrativos",
                "ORGANIZACAO_ACADEMICA": "Centro Universitário",
                "REGIAO": "SUDESTE",
                "QT_VAGAS_AUTORIZADAS": "101-200",
                "CARGA_HORARIA": "3001-4000h"
            }
        }

class PredictionOutput(BaseModel):
    predicao: int
    probabilidade: float


# Configurar caminhos para arquivos
BASE_DIR = Path(__file__).resolve().parent
PREPROCESSOR_PATH = BASE_DIR / "models/pipelines/preprocessor.pkl"
MODEL_PATH = BASE_DIR / "models/trained/best_model_random_forest.joblib"


# Carregar modelo e preprocessador
with open(PREPROCESSOR_PATH, 'rb') as file:
    preprocessor = pickle.load(file)

model = joblib.load(MODEL_PATH)

# Definir colunas para processamento
colunas_nominais = ['GRAU', 'MODALIDADE', 'CATEGORIA_ADMINISTRATIVA', 
                    'ORGANIZACAO_ACADEMICA', 'REGIAO']
colunas_ordinais = ['QT_VAGAS_AUTORIZADAS', 'CARGA_HORARIA']

# Definir categorias ordenadas
categorias_vagas = ['Até 50', '51-100', '101-200', '201-500', '501-1000', 'Mais de 1000']
categorias_carga = ['Até 1000h', '1001-2000h', '2001-3000h', '3001-4000h', '4001-5000h', 'Mais de 5000h']


def preprocess_input(input_data: Dict[str, Any]) -> pd.DataFrame:
    """Pré-processa os dados de entrada"""
    try:
        # Converter para DataFrame
        df = pd.DataFrame([input_data])
        
        # Adicionar temporariamente uma coluna EXTINTO para evitar erros de shape
        df['EXTINTO'] = 0
        
        # Aplicar o preprocessador
        X_transformed = preprocessor.transform(df)
        
        # Se o dado transformado tiver 21 colunas, mas o modelo espera 20, remover a última coluna
        if X_transformed.shape[1] == 21:
            # Remover última coluna (que é a coluna EXTINTO processada)
            X_transformed = X_transformed[:, :-1]
        
        # Obter o último estimar para recuperar os nomes das features
        if hasattr(model, 'steps'):
            final_estimator = model.steps[-1][1]
            if hasattr(final_estimator, 'feature_names_in_'):
                feature_names = final_estimator.feature_names_in_.tolist()
                return pd.DataFrame(X_transformed, columns=feature_names[:X_transformed.shape[1]])
        
        return pd.DataFrame(X_transformed)
    except Exception as e:
        print(f"Erro no preprocessamento: {str(e)}")
        raise


@app.get("/")
def root():
    """Status da API"""
    return {
        "status": "online", 
        "message": "API de Predição de Extinção de Cursos de Graduação",
    }


@app.get("/health")
def health_check():
    """Verifica saúde do sistema"""
    try:
        test_data = {
            "GRAU": "Bacharelado",
            "MODALIDADE": "Educação Presencial",
            "CATEGORIA_ADMINISTRATIVA": "Privada com fins lucrativos",
            "ORGANIZACAO_ACADEMICA": "Centro Universitário",
            "REGIAO": "SUDESTE",
            "QT_VAGAS_AUTORIZADAS": "101-200",
            "CARGA_HORARIA": "3001-4000h"
        }
        
        processed = preprocess_input(test_data)
        model.predict(processed)
        
        return {
            "status": "healthy",
            "componentes": {
                "modelo": "ok",
                "preprocessador": "ok"
            }
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e)
        }


@app.post("/predict", response_model=PredictionOutput)
def predict(course: CourseInput):
    """
    Faz uma predição sobre extinção de curso com base nas informações fornecidas.
    """
    try:

        course_data = course.model_dump()
        
        processed_data = preprocess_input(course_data)
        
        prediction = int(model.predict(processed_data)[0])
        probability = float(model.predict_proba(processed_data)[0][1])
                
        print(f"Predição: {prediction} | Prob: {probability:.2f}")
        
        return {
            "predicao": prediction,
            "probabilidade": round(probability, 2)
        }
    
    except Exception as e:
        print(f"ERRO: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro na predição: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
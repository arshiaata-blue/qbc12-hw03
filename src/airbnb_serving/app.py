import os
from contextlib import asynccontextmanager
from .predictor import predict_single, predict_batch  
from .schema import ListingFeatures                                                                                                                                  
from fastapi import FastAPI
import mlflow
import mlflow.sklearn  

model = None
run_id = None 

MODEL_RUN_ID = os.getenv("MODEL_RUN_ID")
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")
MLFLOW_TRACKING_USERNAME = os.getenv("MLFLOW_TRACKING_USERNAME")
MLFLOW_TRACKING_PASSWORD = os.getenv("MLFLOW_TRACKING_PASSWORD")                                                                   
os.environ["MLFLOW_TRACKING_USERNAME"] = os.getenv("MLFLOW_TRACKING_USERNAME", "")
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD", "")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Loading model
    global model, run_id
    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
    model = mlflow.sklearn.load_model(f"runs:/{os.getenv('MODEL_RUN_ID')}/model")
    run_id = os.getenv("MODEL_RUN_ID")
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health():
    return {"status": "ok", "model_run_id": run_id}

@app.post("/predict")
def predict(features: ListingFeatures):
    result = predict_single(features, model, run_id)
    return result

@app.post("/predict/batch")
def predict_batch_endpoint(features_list: list[ListingFeatures]):
    results = predict_batch(features_list, model, run_id)
    return results

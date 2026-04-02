from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
import pandas as pd
from ml.anomaly import detect_anomalies
from ml.clustering import cluster_logs
from services.log_parser import parse_logs
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/test")
def test():
    return {"message": "working"}

@app.get("/ping")
def ping():
    return {"msg": "ok"}

class LogRequest(BaseModel):
    logs: list[str]

@app.post("/analyze")
async def analyze_logs(request: LogRequest):
    #content = await file.read()
    
    #logs = parse_logs(content.decode())
    
    df = pd.DataFrame({"message": request.logs})

    anomalies = detect_anomalies(df)
    clusters = cluster_logs(df)

    return {
        "anomalies": anomalies,
        "clusters": clusters
    }
from fastapi import FastAPI
import requests
app = FastAPI()
@app.get("/")
def root(): return {"status": "payment service is up"}
@app.post("/process")
def process(): return {"message": "payment processed"}

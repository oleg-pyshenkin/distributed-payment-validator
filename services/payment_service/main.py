from fastapi import FastAPI
import requests
import datetime

app = FastAPI()

@app.post("/process")
def process_payment():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounting_url = "http://accounting-service:8001/record"
    payload = {"amount": 500, "currency": "USD"}
    
    try:
        response = requests.post(accounting_url, json=payload)
        return {
            "message": "Payment flow completed",
            "timestamp": timestamp,
            "details": response.json()
        }
    except Exception as e:
        return {"error": str(e)}

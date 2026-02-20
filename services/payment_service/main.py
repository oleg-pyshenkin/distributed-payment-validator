from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/process")
def process_payment():
    accounting_url = "http://accounting-service:8001/record"
    payload = {"amount": 500, "currency": "USD"}
    
    try:
        response = requests.post(accounting_url, json=payload)
        return {
            "message": "Payment flow completed",
            "details": response.json()
        }
    except Exception as e:
        return {"error": str(e)}

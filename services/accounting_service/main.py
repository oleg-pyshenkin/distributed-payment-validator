from fastapi import FastAPI
import uuid

app = FastAPI()

@app.post("/record")
def record_transaction(data: dict):
    transaction_id = str(uuid.uuid4())
    print(f"Recording transaction: {transaction_id} for amount {data.get('amount')}")

    return {
        "status": "SUCCESSFULLY_SAVED",
        "transaction_id": transaction_id,
        "received_amount": data.get("amount")
    }

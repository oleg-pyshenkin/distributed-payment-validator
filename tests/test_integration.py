import requests

def test_payment_flow_integration():
    url = "http://localhost:8000/process"
    response = requests.post(url)
    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Payment flow completed"
    assert "details" in data
    assert data["details"]["status"]== "SUCCESSFULLY_SAVED"

    assert "transaction_id" in data["details"]
    assert len(data["details"]["transaction_id"]) > 0

    print("\n Integration test passed successfully!")
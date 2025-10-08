from fastapi.testclient import TestClient
from main1 import app

client = TestClient(app)
# test 1  # assert->validate/ check
def test_get_all_employees():
    response = client.get("/employees")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

#test 2
def test_add_employee():
    new_emp = {
        "id": 2,
        "name": "Neha",
        "department": "Math",
        "salary": 20000
    }
    response = client.post("/employees", json=new_emp)
    assert response.status_code == 201
    assert response.json()["name"] == "Neha"

    #test 3
def test_get_employee_by_id():
    response = client.get("/employees/1")
    assert response.status_code == 200
    assert response.json()["name"]=="Amit Sharma"

# test 4
def test_get_employee_not_found():
    response = client.get("/employees/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "employee not found"

# test 5
def test_update_employee():
    new_employee={
        "id": 2,
        "name": "Shreya",
        "department": "AI-DS",
        "salary": 50000
    }
    response = client.put("/employees/2", json=new_employee)
    assert response.status_code == 200
    assert response.json()["name"] == "Shreya"

# test 6
def test_delete_employee():
    response = client.delete("/employees/1")
    assert response.status_code == 200
    assert response.json()["message"] == "employee deleted successfully"


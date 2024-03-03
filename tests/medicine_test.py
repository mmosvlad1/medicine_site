from flask_jwt_extended import create_access_token


def test_get_medicines(client, test_user, init_database):
    # Act
    response = client.get("/api/medicine/")

    # Assert
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_create_medicine(client, test_user):
    new_medicine = {
        "name": "Aspirin",
        "description": "Pain reliever",
        "quantity": 100,
        "price": 5.99
    }

    access_token = create_access_token(identity=1, fresh=True)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Act
    response = client.post("/api/medicine/", json=new_medicine, headers=headers)

    # Assert
    assert response.status_code == 201
    assert "id" in response.get_json()


def test_update_medicine(client, test_user, init_database):
    medicine_id = 1  # Assuming there is a medicine with ID 1 in the database

    updated_medicine = {
        "name": "Updated Aspirin",
        "description": "Updated pain reliever",
        "quantity": 120,
        "price": 6.99,
    }

    access_token = create_access_token(identity=1, fresh=True)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Act
    response = client.put(f"/api/medicine/{medicine_id}", json=updated_medicine, headers=headers)

    # Assert
    assert response.status_code == 200
    assert response.get_json()["name"] == updated_medicine["name"]


def test_delete_medicine(client, test_user, init_database):
    medicine_id = 1  # Assuming there is a medicine with ID 1 in the database
    access_token = create_access_token(identity=1, fresh=True)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Act
    response = client.delete(f"/api/medicine/{medicine_id}", headers=headers)

    # Assert
    assert response.status_code == 204

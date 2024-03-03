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


def test_make_purchase(client, test_user, init_database):
    # Assuming there is a medicine with ID 1 in the database
    medicine_id = 1

    # Assuming the user has already been registered and authenticated
    access_token = create_access_token(identity=test_user.id, fresh=True)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Create a purchase request payload
    purchase_data = {
        'quantity': 120  # Adjust the quantity as needed
    }

    # Act
    response = client.post(f"/api/medicine/{medicine_id}/purchase", json=purchase_data, headers=headers)

    # Assert
    assert response.status_code == 201  # Assuming a successful creation status code
    assert 'id' in response.json  # Assuming the response contains the ID of the created purchase
    assert response.json['medicine_id'] == medicine_id
    assert response.json['user_id'] == test_user.id
    assert response.json['quantity'] == purchase_data['quantity']
    assert 'total_amount' in response.json
    assert 'purchase_date' in response.json


def test_get_demand(client, test_user, init_database):
    # Assuming there is a medicine with ID 1 in the database
    medicine_id = 1
    access_token = create_access_token(identity=1, fresh=True)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Act
    response = client.get(f"/api/medicine/{medicine_id}/demand", headers=headers)

    # Assert
    assert response.status_code == 200
    assert "demand" in response.get_json()


def test_increment_demand(client, test_user, init_database):
    # Assuming there is a medicine with ID 1 in the database
    medicine_id = 1
    access_token = create_access_token(identity=1, fresh=True)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Act
    response = client.put(f"/api/medicine/{medicine_id}/demand/plus", headers=headers)

    # Assert
    assert response.status_code == 200
    assert "demand" in response.get_json()
    assert response.get_json()["demand"] > 0


def test_decrement_demand(client, test_user, init_database):
    # Assuming there is a medicine with ID 1 in the database
    medicine_id = 1
    access_token = create_access_token(identity=1, fresh=True)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Act
    response = client.put(f"/api/medicine/{medicine_id}/demand/minus", headers=headers)

    # Assert
    assert response.status_code == 200
    assert "demand" in response.get_json()
    assert response.get_json()["demand"] == 0


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
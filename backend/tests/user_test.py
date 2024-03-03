from flask_jwt_extended import create_access_token


def test_get_user(client, test_user, init_database):
    user_id = test_user.id
    access_token = create_access_token(identity=1, fresh=True)
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Act
    response = client.get(f"/api/users/{user_id}", headers=headers)

    # Assert
    assert response.status_code == 200
    assert response.get_json()["id"] == user_id


def test_update_user(client, test_user, init_database):
    user_id = test_user.id

    updated_user_data = {
        "name": "Updated Name",
        "surname": "Updated Surname",
        "address": "Updated Address"
        # Include other fields you want to update
    }

    # Create an access token for the test user
    access_token = create_access_token(identity=test_user.id, fresh=True)
    headers = {'Authorization': f'Bearer {access_token}'}

    # Act
    response = client.put(f"/api/users/{user_id}", json=updated_user_data, headers=headers)

    # Assert
    assert response.status_code == 200
    assert response.get_json()["name"] == updated_user_data["name"]


def test_delete_user(client, test_user, init_database):
    user_id = test_user.id

    # Create an access token for the test user
    access_token = create_access_token(identity=test_user.id, fresh=True)
    headers = {'Authorization': f'Bearer {access_token}'}

    print(f"Deleting user with ID: {user_id}")

    # Act
    response = client.delete(f"/api/users/{user_id}", headers=headers)

    # Assert
    assert response.status_code == 204





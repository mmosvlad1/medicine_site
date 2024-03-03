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
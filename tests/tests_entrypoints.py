from fastapi import status

def test_create_access(client, usuário, cartão, session):
    response = client.post(
        '/acesso/',
        json = {
            'uid': 1,
            'device_id': 1,
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
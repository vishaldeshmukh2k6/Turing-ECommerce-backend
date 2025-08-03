def test_register(client):
    res = client.post("/api/auth/register", json={
        "username": "testuser",
        "email": "user@example.com",
        "password": "testpass"
    })
    assert res.status_code == 201
    assert res.json["message"] == "User registered successfully"

def test_login(client):
    client.post("/api/auth/register", json={
        "username": "testuser",
        "email": "user@example.com",
        "password": "testpass"
    })

    res = client.post("/api/auth/login", json={
        "email": "user@example.com",
        "password": "testpass"
    })
    assert res.status_code == 200
    assert "access_token" in res.json

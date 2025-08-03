def test_get_user_profile(client, user_headers):
    res = client.get("/api/users/profile", headers=user_headers)
    assert res.status_code == 200
    assert "email" in res.json

def test_update_user_profile(client, user_headers):
    res = client.put("/api/users/profile", headers=user_headers, json={
        "username": "updatedname"
    })
    assert res.status_code == 200
    assert res.json["username"] == "updatedname"

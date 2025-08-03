def test_place_order(client, user_headers, admin_headers):
    client.post("/api/products/", headers=admin_headers, json={
        "name": "Product X",
        "description": "test product",
        "price": 50,
        "stock": 5
    })

    res = client.post("/api/orders/", headers=user_headers, json={
        "products": [
            {"product_id": 1, "quantity": 2}
        ]
    })
    assert res.status_code in [200, 201]

def test_get_user_orders(client, user_headers):
    res = client.get("/api/orders/", headers=user_headers)
    assert res.status_code == 200
    assert isinstance(res.json, list)

def test_create_product_as_admin(client, admin_headers):
    res = client.post("/api/products/", headers=admin_headers, json={
        "name": "Product A",
        "description": "desc",
        "price": 100,
        "stock": 10
    })
    assert res.status_code in [200, 201]

def test_get_all_products(client):
    res = client.get("/api/products/")
    assert res.status_code == 200
    assert isinstance(res.json, list)

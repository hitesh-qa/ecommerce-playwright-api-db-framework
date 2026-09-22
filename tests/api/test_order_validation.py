import pytest

BASE_URL = "http:/127.0.0.1:5000/"

@pytest.mark.regression
@pytest.mark.api
def test_get_nonexistent_order_returns_404(page):
    response = page.request.get(f"{BASE_URL}/orders/99999")
    assert response.status == 404

@pytest.mark.regression
@pytest.mark.api
def test_create_order_invalid_product_returns_404(page):
    response = page.request.post(
        f"{BASE_URL}/api/orders",
        data={"product_id": 99999, "quantity": 1},
    )
    assert response.status ==404

@pytest.mark.regression
@pytest.mark.api
def test_create_order_zero_quantity_is_rejected(page):
    response = page.request.post(
        f"{BASE_URL}/api/orders",
        data={"product_id": 1, "quantity": 0},
    )
    # An order with 0 quantity should NOT be accepted as a valid order
    assert response.status == 400
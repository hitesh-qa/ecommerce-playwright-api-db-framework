import pytest

BASE_URL = "http://127.0.0.1:5000"

@pytest.mark.regression
@pytest.mark.api
def test_get_nonexistent_order_returns_404(page):
    response = page.request.get(f"{BASE_URL}/api/orders/99999")
    assert response.status == 404
    assert response.json()["error"] == "Order not found"
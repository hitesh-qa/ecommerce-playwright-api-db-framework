import pytest

BASE_URL = "http://127.0.0.1:5000/"

@pytest.mark.regression
@pytest.mark.api
def test_get_nonexistent_order_returns_404():
    response = page.request.get(f"{BASE_URL}/orders/99999")
    assert response.status == 404
def test_homepage_load(page):
    page.goto("http://127.0.0.1:5000/")
    assert "Wireless Mouse" in page.content()
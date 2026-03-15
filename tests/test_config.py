def test_asgi():
    import myproject.asgi
    assert myproject.asgi is not None

def test_wsgi():
    import myproject.wsgi
    assert myproject.wsgi is not None

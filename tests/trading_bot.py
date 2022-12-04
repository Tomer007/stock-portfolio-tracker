from geo_location.app import hello_world


def test_hello_world() -> None:
    assert hello_world() == "Hello, World!"

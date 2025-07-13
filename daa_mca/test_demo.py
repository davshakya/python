import pytest

# Fixture accepts a parameter
@pytest.fixture
def greet(request):
    name = request.param
    return name

# Parametrize the test and pass value to the fixture
@pytest.mark.parametrize("greet", ["Alice", "Bob"], indirect=True)
def test_greeting(greet):
    assert greet in ['Alice', "Bob"] 


import pytest

@pytest.mark.smoke    
def test_login():
    print("Login to application")

@pytest.mark.blackbox    
def test_checkout():
    print("check into application")

@pytest.mark.smoke    
def test_logout():
    print("Logout from the application")
    
    
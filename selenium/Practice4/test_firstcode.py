import pytest

@pytest.mark.usefixtures("setup")
class Test_login1:
    def test_1st_test(self):
        print("My first pytest case ")
    def test_3rd_test(self):
        print("My 3rd pytest case ")
    
@pytest.mark.usefixtures("setup")
class Test_login2:
    def test_4thtest(self):
        print("My first pytest case ")
    def test_5thtest(self):
        print("My 3rd pytest case ")

 



import pytest
from test_logfile import LogClass
class TestLogs(LogClass):
    def test_log(self):
        log = self.getTheLogsFun()
        log.info("Test-log case 1")
        log.info("Test-log case 2")
        if "dev" in "devendra":
            assert True
            log.info("Test Case has been passed")
        else:
            log.error("Test case has been failed")
            assert False

# @pytest.mark.usefixtures("setup")
# class TestLogin:

#     def test_demo1(self):
#         print("My first pytest program...")


# def test_demo2(self):
#     print("My second pytest program...")

#
# @pytest.mark.runthis
# def test_demo3(self):
#     print("Third Program")
#     assert 2 == 3, "It is example of assert"
#
#
# @pytest.mark.skip
# def test_demo4():
#     print("rh Demo Program")
#     assert 2 == 3, "It is example of assert"
#
#
# @pytest.mark.xfail
# def test_demo5():
#     print("5th Demo Program")
#     assert 2 == 3, "It is example of assert"

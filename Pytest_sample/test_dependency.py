import pytest


class TestDepends:
    @pytest.mark.dependency()  # You should give this statement main dependency
    def test_method1(self):
        print("method 1 is called")
        assert 1+2 == 4

    @pytest.mark.dependency(depends=['TestDepends::test_method1'])
    # If method 1 is pass this method will run, If fail skipped
    def test_method2(self):
        print("method 2 is called")

    def test_method3(self):
        print("test method 3")

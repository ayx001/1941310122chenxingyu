import pytest
class Test_Demo2():
    @pytest.mark.demo
    def test_demo(self):
        a=5
        b=-1
        assert a!=b
        pring("demo")
    @pytest.mark.smoke
    def test_two(self):
        a=2
        b=-1
        assert a!=b
        print("smoke")
    @pytest.mark.demo
    @pytest.mark.smoke
    def test_three(self):
        b=2
        assert b==0
        print("smoke demo")

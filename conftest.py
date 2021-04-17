import pytest
@pytest.fixture(params=["1","2"])
def myfixture():
    print("执行myfixture,带参数%s"%request.param)

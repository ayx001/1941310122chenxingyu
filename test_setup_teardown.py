def setup_module():
    print("\n整个模块开始只执行一次")
def teardown_module():
    print("\n整个模块结束只执行一次")
def setup_function():
    print("\ndetup function:不在类中的用例开始前执行")
def teardown_function():
    print("\nteardown function:不在类中的用例结束后执行")
def test_one():
    print("\n正在执行测试模块：test one")
def test_two():
    print("\n正在执行测试模块：test two")
class TestCase():
    def stup_class(self):
        print("\nsetup class:class类里用例执行前执行")
    def teardown_class(self):
        print("\nteardown class:class类里用例执行后执行")
    def setup(self):
        print("\nsetup:每个用例开始前执行")
    def teardown(self):
        print("\nteardown:每个用例结束后执行")
    def test_three(self):
        print("\n正在执行测试模块：test three")
    def test_four(self):
        print("\n正在执行测试模块：test four")


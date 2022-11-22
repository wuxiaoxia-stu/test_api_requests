import pytest

from utils.common_util import CommonUtil


# @pytest.mark.other
class TestExam(CommonUtil):

    @pytest.mark.run(order=2)
    def test_01_exam(self):
        print("测试执行标记用例")
        raise Exception("抛出异常，表示用例失败")

    @pytest.mark.run(order=1)
    def test_02_exam(self):
        print("测试执行标记用例")
        raise Exception("抛出异常，表示用例失败")

    def test_03_exam(self):
        print("测试执行标记用例")
        try:
            print("try:是否符合预期")
        except:
            print("except:解决/捕获异常")

    def test_04_exam(self):
        print("测试执行标记用例")
        try:
            print("try:是否符合预期")
        except:
            print("except:解决/捕获异常")

    def test_04_exam(self):
        print("测试执行标记用例")
        try:
            print("try:是否符合预期")
        except:
            print("except:解决/捕获异常")
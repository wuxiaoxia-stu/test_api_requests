import pytest
from utils.common_util import CommonUtil

# 读取数据据方法
from utils.read_yaml import ReadYaml


#@pytest.mark.usefixtures("exe_database_sql")    #作用域为class的手动调用方法
# @pytest.mark.other
class TestExample(CommonUtil):
    version = 505

    @pytest.mark.skip(reason="无条件跳过")
    def test_01(self):
        print("测试无条件跳过")

    @pytest.mark.skipif(version < 503, reason="version大于503跳过")
    def test_02(self):
        print("测试有条件跳过")

    # @pytest.mark.other
    def test_03(self):
        print("测试执行标记用例")

    # @pytest.mark.other
    def test_04(self, exe_database_sql):
        print("测试fixtrue实现前后置的用例", exe_database_sql)

    # @pytest.mark.other
    @pytest.mark.parametrize("info", ReadYaml().read_yaml("ve.yaml"))
    def test_05_read_yaml(self, info):
        print("测试read_yaml的用例", info)

    @pytest.mark.other
    def test_05_read_yaml(self, db):
        print("测试fixture通过params实现参数化的用例\n", str(db))


# @pytest.mark.usefixtures("exe_database_sql")
class TestFixture:

    # @pytest.mark.other
    def test_fixture_01(self):
        print("测试fixture在类中调用")

    # @pytest.mark.other
    def test_fixture_02(self):
        print("测试fixture在类中调用")


import pytest
from utils.read_yaml import ReadYaml


@pytest.fixture(scope="session", autouse=True, params=ReadYaml().read_yaml("user_login.yaml"), name='login')
def get_leader(request):
    # print("执行用户登录")
    yield request.param   # 将数据传到用例中
    # print("执行用户登录完成")

#
@pytest.fixture(scope="function", autouse=False, params=ReadYaml().read_yaml("example.yaml"), ids=['info'], name='db')
def exe_database_sql(request):
    """
    ids:参数的别名
    :param request:
    :return:
    """
    # print(request.param)
    print("执行SQL查询")
    # yield类似return，但是还会继续执行后面的语句，实现后置操作
    # return "sucess" #不再执行其后面的语句
    # yield "sucess"
    yield request.param  #将数据传到用例中
    print("关闭数据库连接")

@pytest.fixture(scope="function", autouse=False, params=ReadYaml().read_yaml("example.yaml"), ids=['info'], name='db2')
def exe_database_sql_2(request):
    """
    ids:参数的别名
    :param request:
    :return:
    """
    # print(request.param)
    print("执行SQL查询2")
    # yield类似return，但是还会继续执行后面的语句，实现后置操作
    # return "sucess" #不再执行其后面的语句
    # yield "sucess"
    yield request.param  #将数据传到用例中
    print("关闭数据库连接2")
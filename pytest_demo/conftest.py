import json
import logging
import allure
import pytest
import requests

from utils.yaml_util import YamlUtil
log = logging.getLogger(__name__)


@allure.step("用户登录")
@pytest.fixture(scope="session", autouse=False, params=YamlUtil().read_yaml("user_login.yaml"), name='get_token')
def get_token(request):
    url = request.param['url']
    payload = request.param['payload']
    headers = request.param['headers']

    response = requests.request("POST", url, headers=headers, json=payload)

    assert 'token' in response.text
    token = response.json()['data']['token']
    log.info("登录成功，返回结果为："+response.text)
    yield token  # 将token数据设置为变量
    print("执行用户登录完成")




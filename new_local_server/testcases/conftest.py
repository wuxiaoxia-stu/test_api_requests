# -*- coding: utf-8 -*-
import logging
import allure
import pytest
import requests

from utils.request_util import RequestUtil
from utils.yaml_util import YamlUtil
log = logging.getLogger(__name__)


# @allure.step("用户登录")
# @pytest.fixture(scope="session", autouse=True, params=YamlUtil().yaml_util("user_api.yaml"), name='get_token')
# def get_token(request):
#     # 获取token
#     url = request.param['host'] + request.param['login']['url']
#     name = request.param['login']['name']
#     method = request.param['login']['method']
#     payload = request.param['login']['payload']
#     headers = request.param['login']['headers']
#     validate = request.param['login']['validate']
#     response = requests.request(method, url, headers=headers, json=payload)
#
#     assert validate in response.text
#     token = response.json()['data']['token']
#     log.info(name + " 接口返回结果为："+response.text)
#     yield token  # 将token数据设置为变量
#     YamlUtil().write_yaml(token, "token.yaml")  # 将token写入yaml文件,供其他接口调用
#     print("执行用户登录完成")


# 在执行所有用例之前先执行登录接口，获取token
@allure.step("用户登录")
@pytest.fixture(scope="session", autouse=None)
def get_token():
    # 账号和密码登录
    log.info("\n ========生成token ========")
    response = RequestUtil().send_request("login", "user_api.yaml")
    log.info(response)
    validate = RequestUtil().get_validate("login", "user_api.yaml")
    assert validate in response['data']




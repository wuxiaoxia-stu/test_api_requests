# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_user_api
# Time       ：2022/8/25 16:58
# Author     ：xiaoxia
# version    ：python 3.9
# Description：用于测试用户模块
"""
import allure
import pytest
import logging

from utils.request_util import RequestUtil

log = logging.getLogger(__name__)


@allure.epic("本地服务接口测试")
@allure.feature("用户管理模块")
@allure.severity("critical")
@pytest.mark.user
@pytest.mark.run(order=3)
class TestUserApi:

    @allure.story('刷新用户token')
    @pytest.mark.parametrize('api_name, filename', [('refresh_token', 'user_api.yaml')])
    def test_user_refresh_token(self, api_name, filename):
        log.info('刷新用户token')
        response = RequestUtil().send_request(api_name, filename)
        log.info(response)
        # print(response)
        validate = RequestUtil().get_validate(api_name, filename)
        # print(validate)
        assert validate in response['data']

    @allure.story('保存用户信息')
    @pytest.mark.parametrize('api_name, filename', [('save', 'user_api.yaml')])
    def test_user_save(self, api_name, filename):
        log.info('保存用户信息')
        response = RequestUtil().send_request(api_name, filename)
        log.info(response)
        # print(response)
        validate = RequestUtil().get_validate(api_name, filename)
        # print(validate)
        assert validate in response['msg']

    @allure.story('用户退出')
    @pytest.mark.parametrize('api_name, filename', [('logout', 'user_api.yaml')])
    def test_user_logout(self, api_name, filename):
        log.info('用户退出')
        response = RequestUtil().send_request(api_name, filename)
        log.info(response)
        # print(response)
        validate = RequestUtil().get_validate(api_name, filename)
        # print(validate)
        assert validate in response['msg']
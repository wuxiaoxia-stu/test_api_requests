# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_leader_api
# Time       ：2022/8/25 18:14
# Author     ：xiaoxia
# version    ：python 3.9
# Description：
"""
import allure
import pytest
import logging

from utils.request_util import RequestUtil

log = logging.getLogger(__name__)


@allure.epic("本地服务接口测试")
@allure.feature("主任密钥模块")
@allure.severity("critical")
@pytest.mark.leader
@pytest.mark.run(order=2)
class TestLeaderApi:

    @allure.story('获取主任密钥用户信息列表')
    @pytest.mark.parametrize('api_name, filename', [('list', 'leader_api.yaml')])
    def test_leader_list(self, api_name, filename):
        log.info('获取主任密钥用户信息列表')
        response = RequestUtil().send_request(api_name, filename)
        log.info(response)
        # print(response)
        validate = RequestUtil().get_validate(api_name, filename)
        # print(validate)
        assert validate in response['msg']

    @allure.story('绑定主任密钥')
    @pytest.mark.parametrize('api_name, filename', [('bind', 'leader_api.yaml')])
    def test_leader_bind(self, api_name, filename):
        log.info('绑定主任密钥')
        response = RequestUtil().send_request(api_name, filename)
        log.info(response)
        # print(response)
        validate = RequestUtil().get_validate(api_name, filename)
        # print(validate)
        assert validate in response['msg']

    @allure.story('获取主任密钥绑定状态')
    @pytest.mark.parametrize('api_name, filename', [('status', 'leader_api.yaml')])
    def test_leader_status(self, api_name, filename):
        log.info('获取主任密钥绑定状态')
        response = RequestUtil().send_request(api_name, filename)
        log.info(response)
        # print(response)
        validate = RequestUtil().get_validate(api_name, filename)
        # print(validate)
        assert validate in response['msg']

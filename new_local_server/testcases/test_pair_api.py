# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_pair_api
# Time       ：2022/8/25 16:58
# Author     ：xiaoxia
# version    ：python 3.9
# Description：用于测试配对模块
"""
import allure
import pytest
import logging

from utils.request_util import RequestUtil

log = logging.getLogger(__name__)


@allure.epic("本地服务接口测试")
@allure.feature("配对模块")
@allure.severity("critical")
@pytest.mark.pair
@pytest.mark.run(order=1)
class TestPairApi:

    @allure.story('查询配对状态')
    @pytest.mark.parametrize('api_name, filename', [('status', 'pair_api.yaml')])
    def test_pair_status(self, api_name, filename):
        log.info('查询配对状态')
        response = RequestUtil().send_request(api_name, filename)
        log.info(response)
        # print(response)
        validate = RequestUtil().get_validate(api_name, filename)
        # print(validate)
        assert validate == response['code']

    @allure.story('解除配对')
    @pytest.mark.parametrize('api_name, filename', [('break', 'pair_api.yaml')])
    def test_pair_break(self, api_name, filename):
        log.info('解除配对')
        response = RequestUtil().send_request(api_name, filename)
        log.info(response)
        # print(response)
        validate = RequestUtil().get_validate(api_name, filename)
        # print(validate)
        assert validate == response['code']

    @allure.story('申请配对')
    @pytest.mark.parametrize('api_name, filename', [('apply', 'pair_api.yaml')])
    def test_pair_apply(self, api_name, filename):
        log.info('申请配对')
        response = RequestUtil().send_request(api_name, filename)
        log.info(response)
        # print(response)
        validate = RequestUtil().get_validate(api_name, filename)
        # print(validate)
        assert validate == response['code']
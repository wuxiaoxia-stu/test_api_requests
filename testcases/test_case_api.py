# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# File       : test_case_api
# Time       ：2022/8/24 14:53
# Author     ：xiaoxia
# version    ：python 3.9
# Description：用户测试病例相关的接口
"""
import allure
import pytest
import requests
from utils.yaml_util import YamlUtil


@allure.epic("本地服务接口测试")
@allure.feature("病例管理模块")
@allure.severity("critical")
@pytest.mark.case
@pytest.mark.run(order=4)
class TestCaseApi:

    @pytest.mark.parametrize('api_name, filename', [('get_check_options', 'case_api.yaml')])
    def test_getCheckOption(self, api_name, filename):
        """获取实时分析的检查配置信息"""
        # url = YamlUtil()
        print("test_getCheckOption")






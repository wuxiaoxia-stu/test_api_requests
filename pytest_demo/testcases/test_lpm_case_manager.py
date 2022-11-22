"""
# File       : test_case
# Time       ：2022/8/23 18:21
# Author     ：xiaoxia
# version    ：python 3.9
# Description：用于测试病例管理相关接口
"""
import pytest
import allure
import requests
import json
import logging


@pytest.mark.case
class TestLpmCaseMgr:

    @allure.step("获取实时分析的检查配置信息")
    def test_getAiCheck(self):
        url = 'http://127.0.0.1:9006/api/check/options?type=1'
        headers = {
            'author-number': 'C_22060015',
            'Authorization': get_token,
            'Content-Type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers)
        print(response.text)





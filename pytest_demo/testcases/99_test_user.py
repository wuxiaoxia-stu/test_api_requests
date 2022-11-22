import pytest
import allure
import requests
import json
import logging
from utils.read_yaml import ReadYaml

log = logging.getLogger(__name__)


# @pytest.mark.user
# @pytest.mark.usefixtures("db") #代表这个类里面所有用例都会调用该fixture
# @pytest.mark.usefixtures("db2")  # 可以叠加多个，先执行的放底层，后执行的放上层，先执行fixture_name2，再执行fixture_name1
@allure.epic("本地服务系统接口测试")
@allure.feature("用户管理模块")
class TestUser:
    """
    用户管理模块接口
    """
    @pytest.mark.user
    @allure.step("用户登录")
    # def test_01_login(self, user_login, db, db2):
    def test_01_login(self, user_login):
        """
        用户登录
        使用conftest.py中的login的装饰函数
        :return:
        """
        # print('token的值', user_login)
        log.info('token的值:' + user_login)

    # @pytest.mark.user
    @pytest.mark.parametrize('leader_data', ReadYaml().read_yaml('user_get_leader.yaml'))
    def test_02_get_leader(self, leader_data):
        """获取主任密钥"""
        method = leader_data['method']
        url = leader_data['url']
        headers = leader_data['headers']
        payload = leader_data['payload']
        response = requests.request(method, url, headers=headers, data=payload)

        print(response.text)
        # print(response.json()['code'])
        try:
            assert leader_data['validate'] == response.json()['code']
            log.info("获取主任密钥测试用例成功, 返回的结果："+response.text)
        except:
            log.error("获取主任密钥测试用例失败, 返回的结果："+response.text)

    def test_03_get_userinfo(self):
        """
        获取用户列表信息
        :return:
        """
        url = "http://127.0.0.1:8007/api/lv1/customer/list/?limit=100&page=1"

        payload = {}
        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjAwMDIwMDAyIiwidXVpZCI6IjJlMTRjOGVlLTIxYTctNDM0Ni04MmE2LWE1YzQxOGE0NWRiNSIsInVpZCI6MCwic3RhdGUiOjEsImF1dGhvcl9udW1iZXIiOiIyMjAzMDAzMV9DIiwidGVhbSI6MywiZXhwIjoxNjQ4NDc1MjQ5LCJpc3MiOiJnaW4tYmxvZyJ9.WC3K2d1xqlfjMg43-cZieJ5EKEgdtSJ4VTsVFQX3nlE',
            'author-number': '21120001_C'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

    def test_04_adduser(self):
        """
        新增用户
        :return:
        """

        url = "http://127.0.0.1:8007/api/lv1/customer/add/"

        payload = json.dumps({
            "signature": "",
            "password": "4ebe7c58bc215459085a6bb82be27110"
        })
        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjAwMDIwMDAyIiwidXVpZCI6IjJlMTRjOGVlLTIxYTctNDM0Ni04MmE2LWE1YzQxOGE0NWRiNSIsInVpZCI6MCwic3RhdGUiOjEsImF1dGhvcl9udW1iZXIiOiIyMjAzMDAzMV9DIiwidGVhbSI6MywiZXhwIjoxNjQ4NDc1MjQ5LCJpc3MiOiJnaW4tYmxvZyJ9.WC3K2d1xqlfjMg43-cZieJ5EKEgdtSJ4VTsVFQX3nlE',
            'author-number': '21120001_C'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def test_05_modify_user_name(self):
        """
        修改用户名
        :return:
        """
        url = "http://127.0.0.1:8007/api/lv1/customer/update/00020006/"

        payload = json.dumps({
            "name": "000200061"
        })
        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': '{{usertoken}}',
            'author-number': '21120001_C'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def test_06_modify_user_password(self):
        """
        修改用户密码
        :return:
        """
        url = "http://127.0.0.1:8007/api/lv1/customer/update/00020006/"

        payload = json.dumps({
            "password": "4ebe7c58bc215459085a6bb82be271c0"
        })
        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': '{{usertoken}}',
            'author-number': '21120001_C'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def test_07_delete_user(self):
        """
        删除用户
        :return:
        """
        url = "http://127.0.0.1:8007/api/lv1/customer/00020006/"

        payload = {}
        headers = {
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjAwMDIwMDAyIiwidXVpZCI6IjJlMTRjOGVlLTIxYTctNDM0Ni04MmE2LWE1YzQxOGE0NWRiNSIsInVpZCI6MCwic3RhdGUiOjEsImF1dGhvcl9udW1iZXIiOiIyMjAzMDAzMV9DIiwidGVhbSI6MywiZXhwIjoxNjQ4NDc1MjQ5LCJpc3MiOiJnaW4tYmxvZyJ9.WC3K2d1xqlfjMg43-cZieJ5EKEgdtSJ4VTsVFQX3nlE',
            'author-number': '21120001_C'
        }

        response = requests.request("DELETE", url, headers=headers, data=payload)

        print(response.text)

    def test_08_save_userinfo(self):
        """
        保存用户信息
        :return:
        """

        url = "http://127.0.0.1:8007/api/lv1/customer/save/"

        payload = json.dumps({
            "status": 1
        })
        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': '{{usertoken}}',
            'author-number': '21120001_C'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)




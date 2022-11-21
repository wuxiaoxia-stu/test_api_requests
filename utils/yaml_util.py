# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# File       : yaml_util
# Time       ：2022/8/24 14:36
# Author     ：xiaoxia
# version    ：python 3.9
# Description：用于读写yaml文件
"""
import os
import yaml


class YamlUtil:

    # 读取测试用例的yml文件
    def read_yaml(self, filename):
        # 获取配置文件路径
        curPath = os.path.abspath(os.path.dirname(__file__))
        yamlPath = os.path.abspath(os.path.dirname(curPath) + os.path.sep + "/apis/" + filename)
        with open(yamlPath, 'r', encoding='utf-8') as f:
            content = yaml.load(f, Loader=yaml.FullLoader)
        return content

    # 获取接口的URL
    def get_url(self, api_name, filename):
        content = self.read_yaml(filename)
        host = self.read_yaml("common.yaml")['host']
        new_url = host + content[api_name]['url']
        # print(new_url)
        return new_url

    # 获取接口的method
    def get_method(self, api_name, filename):
        content = self.read_yaml(filename)
        # print(content[api_name]['method'])
        return content[api_name]['method']

    # 获取接口的payload
    def get_payload(self, api_name, filename):
        content = self.read_yaml(filename)
        # print(content[api_name]['payload'])
        return content[api_name]['payload']

    # 获取接口的headers
    def get_headers(self, api_name, filename):
        content = self.read_yaml(filename)
        # print(content[api_name]['headers'])
        if api_name == "login":
            # print(content[api_name]['headers'])
            return content[api_name]['headers']
        elif filename == "leader_api.yaml" or filename == "pair_api.yaml":
            return None
        else:
            content[api_name]['headers']['Authorization'] = self.read_yaml("token.yaml")
            # print(content[api_name]['headers'])
            return content[api_name]['headers']

    # 写入yam文件
    def write_yaml(self, data, filename):
        with open(os.getcwd() + "/apis/" + filename, 'w', encoding='utf-8') as f:
            yaml.dump(data, f)

    # # 修改yaml文件
    # def update_yaml(self, data, filename):
    #     with open(os.getcwd() + "/apis/" + filename, encoding="utf-8") as f:
    #         content = yaml.load(f, Loader=yaml.RoundTripLoader)
    #     # 修改yml文件中的参数
    #     content[0]['headers']['Authorization'] = data
    #     with open(os.getcwd() + "/apis/" + filename, 'w', encoding="utf-8") as nf:
    #         yaml.dump(content, nf, Dumper=yaml.RoundTripDumper)

    # 清除yaml文件
    def clear_yaml(self, filename):
        with open(os.getcwd() + "/apis/" + filename, 'w', encoding='utf-8') as f:
            f.truncate()


if __name__ == '__main__':
    YamlUtil().get_url("get_check_options", "case_api.yaml")
    YamlUtil().get_method("get_check_options", "case_api.yaml")
    YamlUtil().get_payload("get_check_options", "case_api.yaml")
    YamlUtil().get_headers("login", "user_api.yaml")
    # YamlUtil().get_validate("login", "user_api.yaml")


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# fileName: request_util.py

import logging
from utils.run_method import RunMethod
from utils.yaml_util import YamlUtil
log = logging.getLogger(__name__)


class RequestUtil:

    def __init__(self):
        self.run = RunMethod()
        self.yaml_util = YamlUtil()

    # 接口请求封装
    def send_request(self, api_name, filename):
        try:
            # 获取接口请求参数
            method = self.yaml_util.get_method(api_name, filename)
            url = self.yaml_util.get_url(api_name, filename)
            headers = self.yaml_util.get_headers(api_name, filename)
            # 区分Get和Post方法
            if method == "GET":
                response = self.run.run_main(method, url, headers)
            elif method == "POST":
                payload = self.yaml_util.get_payload(api_name, filename)
                response = self.run.run_main(method, url, headers, payload)
            # 针对登录接口，把token值写到配置文件token.yml中，供其他接口调用
            if "/api/user/login" in url:
                token = response['data']['token']
                # print(token)
                self.yaml_util.write_yaml(token, 'token.yaml')
            return response
        except Exception as e:
            log.info("接口访问出错啦~ %s" % e)

    # 获取接口的validate
    def get_validate(self, api_name, filename):
        try:
            content = self.yaml_util.read_yaml(filename)
            # print(content[api_name]['validate'])
            return content[api_name]['validate']
        except Exception as e:
            log.info("获取预期结果出错啦~ %s" % e)


if __name__ == "__main__":
    request_util = RequestUtil()
    request_util.send_request("login", "user_api.yaml")


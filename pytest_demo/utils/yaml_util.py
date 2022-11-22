#!/usr/bin/env python3
import os
import yaml


class YamlUtil:
    @staticmethod
    def read_yaml(filename):
        """
        1、路径，如果是执行run文件，filename路径为os.getcwd() + "/data/" + filename
        2、如果是单独执行某个test.py文件，路径为"../../data/" + filename
        """
        with open(os.getcwd() + "/data/" + filename, 'r', encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            # print(data['video_name1'])
        return data


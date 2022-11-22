# -*- encoding=utf8 -*-

__author__ = "PAICS"

import pytest
# import sys
# 将上级目录加入python系统路径
# sys.path.append(r'../')
# from 包名.文件名 import 类名
from utils.read_yaml import ReadYaml


class TestPaics:

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def test_read_yaml(self):
        data = ReadYaml().read_yaml('ve.yaml')
        print(data['video_name1'])

    @pytest.mark.parametrize('videoinfo', ReadYaml().read_yaml('ve.yaml'))
    def test_01(self, videoinfo):
        self.video_name1 = videoinfo['video_name1']
        self.video_name2 = videoinfo['video_name2']
        self.video_length = videoinfo['video_length']
        print(self.video_name2)

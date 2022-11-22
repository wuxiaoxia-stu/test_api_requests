import csv
import os


class CsvUtil:
    """
    用于读取csv格式的数据文件
    1、路径，如果是执行run文件，filename路径为os.getcwd() + "/data/" + filename
    2、如果是单独执行某个test.py文件，路径为"../../data/" + filename
    """
    def read_csv(self, filename):

        print(os.getcwd())
        video_list = []
        with open(os.getcwd() + "/data/" + filename, 'r', encoding='utf-8') as f:
            data = csv.DictReader(f)
            for row in data:
                # print(row['video_name1'], row['video_name2'], row['video_length'])
                video_list.append([row['video_name1'], row['video_name2'], row['video_length']])
        # print(video_list)
        return video_list

# if __name__ == '__main__':
#     # CsvUtil().get_object_path()
#     CsvUtil().read_csv('video_early.csv')

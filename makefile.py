import os
import json
import random

#{
#     "VLOG视频001": [
#         "VLOG",
#         "生活"
#     ],
#     "游戏视频003": [
#         "游戏",
#         "娱乐"
#     ],
#     "学习视频005": [
#         "学习",
#         "生活"
#     ],
#     ......
# }
#
# 运行程序是，随机100000个生成类似上述的JSON数据，并写入到文件中
# 每个数据（在此示例中代表视频）都有一个ID
# 视频类型标签不止上述列出的那么多
all_data = {}
video_type_labels = ["生活", "娱乐", "体育", "教育", "科技", "军事", "汽车", "财经", "游戏", "旅游", "美食",
                             "宠物", "其他", "二次元", "美女", "搞笑", "时尚", "电影", "音乐", "综艺", "电视剧", "电影"]

def generate_json_data(file_path):
    global all_data
    """
    生成JSON数据
    :param file_path: 文件路径
    :return:
    """
    # all_data = {}
    for i in range(100000):
        video_id = i
        video_data = {}

        video_data["id"] = video_id
        video_data["labels"] = video_type_labels[random.randint(0, len(video_type_labels) - 1)]

        # add to add_data
        all_data[video_id] = video_data

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)



def read_data():
    global all_data
    if os.path.exists("data.json"):
        # read 'all_data' dict from data.json
        with open("data.json", "r", encoding="utf-8") as f:
            all_data = json.load(f)
            print("[Makefile] Read data successfully! ")
    else:
        print("[Makefile] No data.json file! ")
        generate_json_data("data.json")
        print("[Makefile] Generate data successfully! ")
        with open("data.json", "r", encoding="utf-8") as f:
            all_data = json.load(f)
            print("[Makefile] Read data successfully! ")


if __name__ == "__main__":
    generate_json_data("data.json")
    print("[Makefile] Generate data successfully! ")












































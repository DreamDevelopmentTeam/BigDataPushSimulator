import os
import random
import sys
import time
import consts
import bdcount
import makefile

debug = False

makefile.read_data()
bdcount.load_data()

videos = makefile.all_data

print("[Main] 即将启动大数据模拟！输入debug开启详细输出模式！")
ipt = input("Input: ")
if ipt == "debug":
    debug = True
    print("[Main.Debug] 详细输出模式已开启！")

print("[Main] 短视频大数据模拟已启动！")

for k, v in videos.items():
    # 根据bdcount中的喜好数据（例如{"数码": 90, "生活": -1}）推送视频。如果数据小于0则修正为20。
    bdf = bdcount.get_count(v['labels'])
    if bdf < -100:
        #bdcount.set_count(v['labels'], 0)
        if debug:
            print(f"==> 根据喜好算法忽略推送视频： ID = {k} / 标签: {v['labels']}")
        continue
    bdl = bdcount.data
    # data格式：
    # {"数码": 90, "生活": -1}
    # 根据上述的数字大小占比，计算推荐到该视频的概率（小于1的数值不计算）
    all_count = 0
    for label, count in bdl.items():
        if count < 1:
            continue
        all_count = all_count + count
        #print(all_count)

    gailv = bdf /  all_count
    gailv_r = random.random()
    if debug:
        print(f"====> 概率 {gailv} -> {gailv_r} / {all_count} == {bdf}")
    if gailv_r >= gailv:
        if debug:
            print(f"==> 根据喜好算法忽略推送视频： ID = {k} / 标签: {v['labels']}")
        continue

    t1 = time.time()
    # 获取用户观看视频的时间（模拟）
    print("")
    print(f">>> 视频ID: {k} / 标签: {v['labels']}")
    if debug:
        print(f">> d = 不喜欢, l = 喜欢, s = 收藏, c = 分享, e = 退出模拟, a = 强制增加权重(100), g = 输出分数")
    else:
        print(f">> d = 不喜欢, l = 喜欢, s = 收藏, c = 分享, e = 退出模拟")
    ip = input("Input: ")
    t2 = time.time()
    if debug:
        print(f"=> 您观看了 {int(((t2 - t1) * 1000))} 毫秒")
        bdcount.w_normal_move(v['labels'], int(((t2 - t1) * 1000)),debug=debug)
    if ip.find("d") != -1:
        bdcount.w_dont_like(v['labels'],debug=debug)
    if ip.find("l") != -1:
        bdcount.w_click_like(v['labels'],debug=debug)
    if ip.find("s") != -1:
        bdcount.w_collection(v['labels'],debug=debug)
    if ip.find("c") != -1:
        bdcount.w_share(v['labels'],debug=debug)
    if ip.find("g") != -1:
        print(bdcount.data)
    if ip.find("a") != -1:
        print(f"==> 已为标签 {v['labels']} 增加 100 推送权重")
        bdcount.add_count(v['labels'], 100)
    if ip.find("e") != -1:
        bdcount.save_data()
        break
import json
import os
import sys
import random




data = {}
default_count = 100

def load_data():
    global data
    if os.path.exists('bdc.json'):
        # load 'data' dist from bdc.json
        with open('bdc.json', 'r', encoding="utf-8") as f:
            data = json.load(f)
        return data
    else:
        data = {}

def save_data():
    global data
    # save 'data' dist to bdc.json
    with open('bdc.json', 'w', encoding="utf-8") as f:
        json.dump(data, f)


def get_data():
    global data
    return data

def set_count(label:str, count:int):
    global data
    data[label] = count
def add_count(label:str, count:int):
    set_count(label,get_count(label) + count)

def get_count(label:str):
    global data
    if not label in data.keys():
        data[label] = default_count
        return data[label]
    return data[label]


#####################################################

def w_click_like(label:str, debug=False):
    add_count(label, 5)
    if debug:
        print(f"[BDC]> Click Like: {label}, Count = {get_count(label)}")


def w_normal_move(label:str,time:int, debug=False):
    if time > 8000:
        set_count(label, get_count(label) + 1)
        if debug:
            print(f"[BDC]> Time Like: {label}, Count = {get_count(label)}")
        return

def w_dont_like(label:str, debug=False):
    set_count(label,get_count(label) - 15)
    if debug:
        print(f"[BDC]> Click Don't Like: {label}, Count = {get_count(label)}")

def w_share(label:str, debug=False):
    set_count(label,get_count(label) + 1)
    if debug:
        print(f"[BDC]> Click Share: {label}, Count = {get_count(label)}")

def w_collection(label:str, debug=False):
    set_count(label,get_count(label) + 6)
    if debug:
        print(f"[BDC]> Click Collection: {label}, Count = {get_count(label)}")

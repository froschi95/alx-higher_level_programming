#!/usr/bin/python3
"""module to load and save"""


import json
import sys
import os

save_to_j_f = __import__('5-save_to_json_file').save_to_json_file
load_from_j_f = __import__('6-load_from_json_file').load_from_json_file

f_name = 'add_item.json'
num_args = len(sys.argv)

if not os.path.isfile(f_name):
    with open(f_name, 'w', encoding='utf-8') as f:
        f.write('[]')

if num_args > 1:
    obj = load_from_j_f(f_name)
    for i in range(1, num_args):
        obj.append(sys.argv[i])
    save_to_j_f(obj, f_name)

if __name__ == '__main__':
    print(f'Usage: ./7-add_item.py <*args>')

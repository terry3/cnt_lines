#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Just count lines.
"""
import sys
import os

t_cnt_file_l = []

def cnt_lines(file_name):
    global t_cnt
    t_cnt_curr = 0
    t_file = open(file_name)
    for line in t_file:
        t_cnt_curr += 1
    t_file.close()
    print file_name, ":", t_cnt_curr
    t_cnt += t_cnt_curr

def cnt_lines_config():
    t_config_file_name = "cnt_lines.conf"
    t_config = open(t_config_file_name)
    t_cnt_file_l.append(os.path.abspath(t_config_file_name).strip())
    for line in t_config:
        path = os.path.abspath(line)
        t_cnt_file_l.append(path.strip())
    t_config.close()

def cnt_lines_traverse(t_dir="./"):
    for lists in os.listdir(t_dir):
        path = os.path.join(t_dir, lists)
        if os.path.isdir(path):
            if not os.path.abspath(path) in t_cnt_file_l:
                cnt_lines_traverse(path)
        else:
            abs_path = os.path.abspath(path)
            if not abs_path in t_cnt_file_l:
                cnt_lines(abs_path)

if __name__ == '__main__':
    t_cnt = 0
    os.chdir(sys.argv[1])
    cnt_lines_config()
    cnt_lines_traverse()
    print "total:", t_cnt

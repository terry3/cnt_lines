#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Just count lines.
"""
import sys
import os
import os.path

t_cnt_file_l = []
t_cnt_wldc_l = []
t_cnt_wldc_w_l = []
t_white_toggle = False
t_config_file_name = "cntl_ign.conf"

def cnt_lines(file_name):
    global t_cnt
    t_cnt_curr = 0
    t_file = open(file_name)
    for line in t_file:
        t_cnt_curr += 1
    t_file.close()
    print "%-52s, %-7s" % (file_name, t_cnt_curr)
    t_cnt += t_cnt_curr

def cnt_lines_config_wildcard_add(t_suffix):
    t_cnt_wldc_l.append(t_suffix);

def cnt_lines_config_add(file_name):
    path = os.path.abspath(file_name).strip()
    t_cnt_file_l.append(path)

def cnt_lines_config_default():
    global t_config_file_name
    cnt_lines_config_add(t_config_file_name)
    cnt_lines_config_add(".svn")
    cnt_lines_config_add(".git")
    cnt_lines_config_add("LICENSE")
    cnt_lines_config_add("README.md")
    cnt_lines_config_add(".gitignore")
    cnt_lines_config_wildcard_add(".obj")
    cnt_lines_config_wildcard_add(".o")
    cnt_lines_config_wildcard_add(".class")
    cnt_lines_config_wildcard_add(".out")

def cnt_lines_config():
    global t_config_file_name
    cnt_lines_config_default()
    try:
        t_config = open(t_config_file_name)
        for line in t_config:
            # filter the wilcard suffix
            if line[0] == '*' :
                t_cnt_wldc_l.append(line[1:]);
            else:
                path = os.path.abspath(line)
                t_cnt_file_l.append(path.strip())
        t_config.close()
    except IOError as e:
        pass

def cnt_lines_traverse(t_dir="./"):
    for lists in os.listdir(t_dir):
        path = os.path.join(t_dir, lists)
        if os.path.isdir(path):
            if not os.path.abspath(path) in t_cnt_file_l:
                cnt_lines_traverse(path)
        else:
            abs_path = os.path.abspath(path)
            extension = os.path.splitext(path)[1]
            if not abs_path in t_cnt_file_l and not extension in t_cnt_wldc_l:
                if t_white_toggle:
                    if extension in t_cnt_wldc_w_l:
                        cnt_lines(abs_path)
                else:
                    cnt_lines(abs_path)

if __name__ == '__main__':
    t_cnt = 0
    base_dir = sys.argv[1]
    os.chdir(base_dir)
    cnt_lines_config()
    for var in sys.argv:
        if var[0] == '*':
            t_cnt_wldc_w_l.append(var[1:])
    if len(t_cnt_wldc_w_l):
        t_white_toggle = True
    cnt_lines_traverse(t_dir=base_dir)
    print "total:", t_cnt

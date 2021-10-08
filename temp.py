#!/usr/bin/python3
# Author:Alkaidcc
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23 20:19
# @Author  : Alkaidcc
# @File    : autocheck.py
# @Software: PyCharm

import os
import re
import sys


def solve(file_dir):
    for key, value in stu_information1.items():
        stu_information2[value] = key

    stu_list = []

    files = [files for root, dirs, files in os.walk(file_dir)]
    roots = [root for root,dirs,files in os.walk(file_dir)]
    for it in files[0]:
        stu_id = re.findall(r'\d{12}', it)[0]
        if stu_id not in list(stu_information2.keys()):
            print('未知的学号')
            print(stu_id)
            print("---------")
        else:
            stu_list.append(stu_id)
    if len(stu_list) == 37:
        print(os.path.split(roots[0])[1]+"已收齐~")
    else:
        m_cnt = 0
        print(os.path.split(roots[0])[1]+"未交: ")
        print("---------")
        for x in stu_information2:
            if x not in stu_list:
                m_cnt = m_cnt + 1
                print(stu_information2[x])
        print("---------")
        print("共计"+str(m_cnt)+"人\n")
def solve_path(paths_list):
    for path in paths_list:
        solve(path)
    MyFun()
def MyFun():
    try:
        print('● 1.检查作业上交情况(default)')
        print('○ 2.退出')
        print('> ',end='')
        temp = input()
        if temp == '':
            num = 1
        else:
            num = int(temp)
        if num == 1:
            print('● 1.读取配置文件(default)')
            print('○ 2.手动输入目录')
            print('> ',end='')
            temp1 = input()
            if temp1 == '':
                choice = 1
            else:
                choice = int(temp1)
            if choice == 1:
                solve_path(LoadConfig())
            elif choice == 2:
                paths = [input("请输入扫描目录：")]
                solve_path(paths)
            else:                
                print('\n')
                MyFun()
        elif num == 2:
            print("Exit!")
            os._exit(0)
        else:
            print("Error!")
            MyFun()
    except KeyboardInterrupt:
        print("Exit")

def LoadConfig():
    m_root = os.path.dirname(os.path.realpath(sys.executable))
    m_files = [file.name for file in os.scandir(m_root)]
    
    if "Conf.p" in m_files:
        return pickle.load(open(str(m_root)+os.sep+"Conf.p","rb"))
    else:
        print("Created Conf.p")
        path_list = input("Input your check path (split by ',')").split(',')
        pickle.dump(path_list,open(str(m_root)+os.sep+"Conf.p","wb"))
        return path_list


if(__name__=="__main__"):
    MyFun()

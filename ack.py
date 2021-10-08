# -*- coding: utf-8 -*-
import os
import re
from xlsx import xlsxParser
from Config import Config


class Ack:
    def __init__(self, config: Config, parser: xlsxParser) -> None:
        self.config = config
        self.parser = parser
        self.stuInfo = {}
    def loadConfig(self):
        self.paths = self.config.getScanDirFromToml()

    def getStuInfo(self):
        stuId, stuName = self.parser.parse()
        for index, (id, name) in enumerate(zip(stuId, stuName)):
            if index != 0:
                self.stuInfo[id] = name
        return self.stuInfo

    def getPath(self):
        return self.paths

    def run(self):
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
                    self.check(self.paths)
                elif choice == 2:
                    paths = [input("请输入扫描目录：")]
                    self.check(paths)
                else:                
                    print('\n')
                    self.run()
            elif num == 2:
                print("Exit!")
                os._exit(0)
            else:
                print("Error!")
                self.run()
        except KeyboardInterrupt:
            print("Exit")

    def check(self,path_list):
        for path in path_list:
            # file list
            files = [files for root, dirs, files in os.walk(path)]
            # directory name
            roots = [root for root,dirs,files in os.walk(path)]
            check_stuId = []
            # read files and get file stuId
            for it in files[0]:
                # get student id
                stu_id = re.findall(r'\d{12}', it)[0]
                if stu_id not in self.stuInfo.keys():
                    print('未知的学号')
                    # TODO warning color
                    print(stu_id)
                    print("---------")
                else:
                    check_stuId.append(stu_id)
            
            if len(check_stuId) == 37:
                # optimizer 
                print('\033[42m'+os.path.split(roots[0])[1]+"已收齐~"+'\033[0m')
            else:
                # count
                m_cnt = 0
                print(os.path.split(roots[0])[1]+"未交: ")
                print("---------")
                for x in self.stuInfo.keys():
                    if x not in check_stuId:
                        m_cnt = m_cnt + 1
                        print(self.stuInfo[x])
                print("---------")
                print("共计"+str(m_cnt)+"人\n")
        self.run()



configPath = 'pyproject.toml'
xlsxPath = 'test.xlsx'

if __name__ == "__main__":
    ack = Ack(Config(configPath), xlsxParser(xlsxPath))
    ack.loadConfig()
    ack.getStuInfo()
    ack.getPath()
    ack.run()

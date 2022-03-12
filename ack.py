from pathlib import Path
import toml
import os
from stu import Stu
from typing import List
from utils.util import CONFIG_PATH, _init_config_file, _init_stu_info


class Ack:

    def __init__(self):
        self.path = Path(CONFIG_PATH)
        if not self.path.exists():
            _init_config_file()
        # Get PATH
        config = toml.load(CONFIG_PATH)
        self.xlsx_path = config.get('xlsx_path')
        self.scan_path = config.get('scan_path')
        # Get STU by xlsx_path
        self.stu:List[Stu] = _init_stu_info(self.xlsx_path)
    def loop(self):
        try:
            print('● 1.检查作业上交情况(default)')
            print('○ 2.退出')
            print('> ',end='')
            key1 = input()
            if key1 == '1' or key1 == '':
                print('● 1.读取配置文件(default)')
                print('○ 2.手动输入目录')
                print('> ',end='')
                key2 = input()
                if key2 == '1' or key2 == '':
                    pass
                    # TODO scan for config file
                elif key2 == '2':
                    path = Path(input("请输入扫描目录："))
                    if path.exists():
                        pass
                        # TODO
                    else:
                        self.loop()
                else:                
                    print('\n')
                    self.loop()
            elif key1 == '2':
                print("Exit!")
                os._exit(0)
            else:
                print("Error!")
                self.loop()

        except KeyboardInterrupt:
            print("Exit")
    

if __name__ == '__main__':
    ack = Ack()
    ack.loop()
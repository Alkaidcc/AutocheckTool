from pathlib import Path
import toml
import os
import re
from stu import Stu
from typing import List
from utils.util import CONFIG_PATH, STU_ID_LEN, _init_config_file, _init_stu_info, get_stu_len, trim_quote


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
        self.stu: List[Stu] = _init_stu_info(self.xlsx_path)

    def loop(self):
        try:
            print('● 1.检查作业上交情况(default)')
            print('○ 2.退出')
            print('> ', end='')
            key1 = input()
            if key1 == '1' or key1 == '':
                print('● 1.读取配置文件(default)')
                print('○ 2.手动输入目录')
                print('> ', end='')
                key2 = input()
                if key2 == '1' or key2 == '':
                    self.check_directory_recursive(self.scan_path)
                elif key2 == '2':
                    path = Path(trim_quote(input("请输入扫描目录：")))
                    if path.exists():
                        self.check_single_directory(path)
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

    def check_stu_id(self, stu_name, stu_id):
        for stu in self.stu:
            if stu.stu_name == stu_name:
                if stu.stu_id != stu_id:
                    print('学号不一致：', stu.stu_name, stu_id)

    def check_single_directory(self, path: Path):
        self.reset_data()
        check_count = 0
        for item in path.iterdir():
            id_from_file = re.findall('\d{'+str(STU_ID_LEN)+'}', item.name)
            for stu in self.stu:
                if stu.stu_name in item.name:
                    if stu.stu_status == '已提交':
                        print('重复提交：', stu.stu_name)
                        return
                    check_count += 1
                    stu.stu_status = '已提交'
                    
                    if id_from_file:
                        self.check_stu_id(stu.stu_name, id_from_file[0])
        for stu in self.stu:
            if stu.stu_status == '未提交':
                print(stu.stu_name, stu.stu_status)
        if check_count == get_stu_len():
            print("已收齐")
        if check_count > get_stu_len():
            print("收齐数量大于学生数量")

    def check_directory_recursive(self, path):
        path = Path(path)
        for item in path.iterdir():
            if item.is_dir():
                self.check_directory_recursive(item)
            elif item.match('*.docx'):
                print('\n')
                print(item.parent.name)
                self.check_single_directory(item.parent)
                break

    def reset_data(self):
        for stu in self.stu:
            stu.stu_status = '未提交'


if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    ack = Ack()
    ack.loop()

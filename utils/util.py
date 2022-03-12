import toml
from typing import List
from stu import Stu
from pathlib import Path
import os
from openpyxl import load_workbook

CONFIG_PATH = './config.toml'
xlsx_path = None
scan_path = None
result: List[Stu] = []

def _init_config_file():
    Path(CONFIG_PATH).touch()
    _init_config_by_user(CONFIG_PATH)

def _init_config_by_user(file_path):
    xlsx_path:Path = get_xlsx_path()
    scan_path:Path = get_scan_path()
    config = {
        'xlsx_path': str(xlsx_path),
        'scan_path': str(scan_path)
    }
    with open(file_path, 'w') as f:
        toml.dump(config, f)

def _init_stu_info(xlsx_path) -> List[Stu]:
    stu_id,stu_name = get_data_from_xlsx(xlsx_path)
    for index,(id,name) in enumerate(zip(stu_id,stu_name)):
        if index != 0:
            result.append(Stu(id,name))
    return result

def get_stu_len():
    return len(result)

def get_data_from_xlsx(xlsx_path):
    try:
        data = load_workbook(xlsx_path)
        sheet = data.worksheets[0]
        col1 = []
        col2 = []
        for col in sheet['A']:
            if col.value == '' or col.value is None:
                break
            col1.append(col.value)
        for col in sheet['B']:
            if col.value == '' or col.value is None:
                break
            col2.append(col.value)
        return col1, col2
    except FileNotFoundError:
        print("Not found xlsx file. Please check config file.")
        os._exit(0)

def xlsx_valid(xlsx_path: Path):
    if xlsx_path.exists():
        if xlsx_path.is_dir():
            for file in xlsx_path.iterdir():
                if file.suffix == '.xlsx':
                    return file
            else:
                print("Error: xlsx file not found")
                xlsx_path = get_xlsx_path()
                return xlsx_path
        else:
            if xlsx_path.suffix == '.xlsx':
                return xlsx_path
            else:
                print("Error: not a xlsx file")
                xlsx_path = get_xlsx_path()
                return xlsx_path
    else:
        print("Error: xlsx path is not exist!")
        xlsx_path = get_xlsx_path()
        return xlsx_path

def get_xlsx_path() -> Path:
    xlsx_path = Path(trim_quote(input("Please input your xlsx path:")))
    xlsx_path = xlsx_valid(xlsx_path)
    return xlsx_path

def get_scan_path() -> Path:
    scan_path = Path(trim_quote(input("Please input your scan path:")))
    if scan_path.exists():
        return scan_path
    else:
        print("Error: scan path is not exist!")
        scan_path = get_scan_path()
        return scan_path

def trim_quote(s: str) -> str:
    return s.replace("'",'').replace('"','')
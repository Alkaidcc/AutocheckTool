from typing import List, Optional
import toml
from pathlib import Path


xlsx_path = None

def _init_config_file():
    Path('./config.toml').touch()
    _init_config_by_user('./config.toml')


def _init_config_by_user(file_path):
    xlsx_path:Path = get_xlsx_path()
    print("xlsx path:",xlsx_path)
    scan_path:Path = get_scan_path()
    print("scan path:",scan_path)
    config = {
        'xlsx_path': str(xlsx_path),
        'scan_path': str(scan_path)
    }
    with open(file_path, 'w') as f:
        toml.dump(config, f)


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
    path = input("Please input your xlsx path:")
    # if path contains """" or ''' or " or ' get rid of them
    path = path.replace("'",'').replace('"','')
    xlsx_path = Path(path)
    xlsx_path = xlsx_valid(xlsx_path)
    return xlsx_path

def get_scan_path() -> Path:
    scan_path = Path(input("Please input your scan path:"))
    if scan_path.exists():
        return scan_path
    else:
        print("Error: scan path is not exist!")
        scan_path = get_scan_path()
        return scan_path
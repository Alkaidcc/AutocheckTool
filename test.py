from pathlib import Path
import tomlkit
from utils.util import _init_config_file


class Test:

    def __init__(self):
        self.path = Path('./config.toml')
        if not self.path.exists():
            _init_config_file()


if __name__ == '__main__':
    test = Test()

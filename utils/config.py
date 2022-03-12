import tomlkit
import os
class Config:
    def __init__(self,path) -> None:
        self.tomlPath = path
        self.scanPath,self.xlsxPath = self.ParsePath(self.tomlPath)
        if self.xlsxPath == '':
            self.xlsxPath = self.get_file_name()
    @staticmethod
    def get_file_name():
        dirs = os.listdir()
        for i in dirs:
            if i.split('.')[-1] == 'xlsx':
                return i
    def ParsePath(self,path):
        with open(path,'r',encoding='utf-8') as f:
            data = tomlkit.parse(f.read())
        config = data.get("tool",{}).get("config")
        if not config:
            raise ValueError("Cannot find '[tool.config]' in given toml file!")
        return config.get("ScanPath",[]), config.get("XlsxPath")
import tomlkit

class Config:
    def __init__(self,path) -> None:
        self.tomlPath = path
        self.scanPath,self.xlsxPath = self.ParsePath(self.tomlPath)
    def ParsePath(self,path):
        with open(path,'r',encoding='utf-8') as f:
            data = tomlkit.parse(f.read())
        config = data.get("tool",{}).get("config")
        if not config:
            raise ValueError("Cannot find '[tool.config]' in given toml file!")
        return config.get("ScanPath",[]), config.get("XlsxPath")
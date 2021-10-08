import toml
import tomlkit

class Config:
    def __init__(self,path) -> None:
        self.tomlPath = path
    def getScanDirFromToml(self):
        with open(self.tomlPath,'r',encoding='utf-8') as f:
            data = tomlkit.parse(f.read())
        config = data.get("tool",{}).get("config")
        if not config:
            raise ValueError("Cannot find '[tool.config]' in given toml file!")
        return config.get("path",[])
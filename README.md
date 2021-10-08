# AutoCheckTool

这个项目主要是为了解决收作业时繁杂的检查步骤。我经常遇到以下情况：

1. 对着班级名单（Excel）挨个检查每位同学是否提交了文件。
2. 每次收作业都要反复进行（1），十分浪费时间。

于是，就有了这个项目。

## Description

已经实现的功能有：

- [x] 根据`名单.xlsx`来某同学是否交作业了。
- [x] 根据`pyproject.toml`中的`path`来扫描需要检查的文件夹
- [x] 基础的shell交互
- [x] 手动输入path来扫描文件夹

未来可能会实现的功能有：

- [ ] 更友好的shell交互
- [ ] GUI界面
- [ ] 指定根目录扫描所有子目录
- [ ] 用NLP对学号姓名匹配进行校验



## 开始

### 依赖

* Package: `toml`，`tomlkit`，`openpyxl`
* Environment: Windows 10+，Python3.9

### 安装

```python
pip install -r requirements.txt
```

### 修改配置文件

- `pyproject.toml`中的`path`改为需要扫描的路径
- `ack.py`中的`configPath`和`xlsxPath`改为`pyproject.toml`和`名单.xlsx`的路径

### 启动

```shell
git clone https://github.com/Alkaidcc/AutocheckTool.git
python ack.py
```

## Help

欢迎提出pr和issues。

## Authors

@Alkaidcc

## License

This project is licensed under the [MIT] License - see the `LICENSE` file for details

* https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)

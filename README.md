# AutoCheckTool

这个项目主要是为了解决收作业时繁杂的检查步骤。我经常遇到以下情况：

1. 对着班级名单（Excel）挨个检查每位同学是否提交了文件。
2. 每次收作业都要反复进行（1），十分浪费时间。

于是，就有了这个项目。

## Description

已经实现的功能有：

- [x] 根据`名单.xlsx`来确定某同学是否交作业了。
- [x] 根据`pyproject.toml`中的`path`来扫描需要检查的文件夹
- [x] 基础的shell交互
- [x] 手动输入path来扫描文件夹
- [x] 打包成可执行文件并加入环境变量
- [x] 指定根目录扫描所有子目录
- [x] 根据姓名校验学号 
- [x] 添加了Linux支持 

未来可能会实现的功能有：

- [ ] 更友好的shell交互
- [ ] GUI界面




## 开始

### 依赖

* Package: `toml`，`openpyxl`
* Environment: Windows 10+，Python3.9

### 可执行文件
~~[下载地址](https://github.com/Alkaidcc/AutocheckTool/releases/tag/v0.0.1)~~ 不是最新版本，部分功能不可用。

下载`ack.exe`和pyproject.toml后，只需修改配置文件即可运行

### 将exe添加到环境变量

按下快捷键`win+Q` -> 搜索 path -> 点击「编辑系统环境变量」 -> 环境变量 -> 在「系统变量」这一栏中找到`PATHEXT` -> 在最前面加上`.EXE;`


在「系统变量」这一栏找到`Path` -> 双击 -> 点击新建 -> 将`ack.exe`文件所在目录填写进去 -> 确定

在做完以上操作以后，即可在任意地方打开命令行执行`ack`命令来运行exe文件了

---
### 自己构建

```shell
git clone https://github.com/Alkaidcc/AutocheckTool.git
```

```python
pip install -r requirements.txt
```

### 初始化设置
![image](https://user-images.githubusercontent.com/54631354/158011047-4449c264-264d-412e-83b7-d84fb4f2360b.png)
这里分别填写你的名单文件的路径和需要扫描文件夹的根路径。注意：默认（直接回车）为当前路径。
初始化后会在本地生成`config.toml`文件，请保证其在根目录下，否则无法正常工作。切换目录可以自行修改。



#### test.xlsx格式

| ID    | NAME  |
| ----- | ----- |
| 学号1 | 姓名1 |
| 学号2 | 姓名2 |
| ...   | ...   |

### 启动

```shell
python ack.py
```

## Tips
使用递归扫描请使用以下目录结构，`homework`作为扫描的根目录，其他为具体作业的文件夹。
```
└── homework
    ├── java
    │   ├── aaa.docx
    │   └── bbb.docx
    ├── machinelearning
    │   └── ccc.docx
    └── python
        └── ddd.docx
```
## Help

欢迎提出pr和issues。

## Authors

[@Alkaidcc](https://github.com/Alkaidcc)

## License

This project is licensed under the [MIT] License - see the `LICENSE` file for details

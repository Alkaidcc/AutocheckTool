from openpyxl import load_workbook

class xlsxParser:
    def __init__(self,path) -> None:
        self.data = load_workbook(path)
        self.sheet = self.data.worksheets[0]
        self.col1 = []
        self.col2 = []
    def parse(self):
        for col in self.sheet['A']:
            if col.value == '' or col.value is None:
                break
            self.col1.append(col.value)
        for col in self.sheet['B']:
            if col.value == '' or col.value is None:
                break
            self.col2.append(col.value)
        return self.col1, self.col2


from openpyxl import load_workbook

class ExcelImporter:

    def __init__(self, filePath):
        self.filePath=filePath
        self.excelFile = load_workbook(filePath)

    def readData(self):
        return 1.0

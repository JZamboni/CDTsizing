from openpyxl import load_workbook

class ExcelImporter:

    def __init__(self, filePath):
        self.filePath=filePath

    def excelFile(self):
        return load_workbook(self.filePath)


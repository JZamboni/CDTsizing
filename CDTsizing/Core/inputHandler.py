import os
from Tkinter import *
from tkFileDialog import askopenfilename
from CDTsizing.Core.Importers.ExcelImporter import ExcelImporter


class inputHandler:

    '''
    Handler that takes care of opening different format files.
    Supperted files are :
        *txt
        *excel
        *csv
        *matlab
        *xml
    '''

    def callback():
        '''
        GUI to open a desired file.
        '''
        name = askopenfilename()
        return name

    errmsg = 'Error!'
    Button(text='File Open', command=callback).pack(fill=X)

    filePath = callback()
    filename, file_extension = os.path.splitext(filePath)  # File extension for use in the rest of input file.

    def importCaller(self):
        if self.file_extension == ".xlsx":
            spam = ExcelImporter(filePath=self.filePath)

        else:
            print ("File type is not supported in this application. Please choose a different format")



import os
from openpyxl import load_workbook
from Tkinter import *
from tkFileDialog import askopenfilename


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

    if file_extension == ".xlsx":
        print('file type Excel')
        var=readExcel()
    else:
        print('file type is not supported')

    def readExcel():
        return 1.0


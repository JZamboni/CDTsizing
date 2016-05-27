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
        name = askopenfilename()
        print name

    errmsg = 'Error!'
    Button(text='File Open', command=callback).pack(fill=X)
    mainloop()

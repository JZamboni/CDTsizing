from MainFolder.Core.parameter import parameter
from parapy.core import *
from parapy.geom import *

class variabili(GeomBase):
    
    def __init__(self, inputVar1=0.0, inputVar2=0.0):
        self.var1=inputVar1
        self.var2=inputVar2


    def somma(self):
        return self.var1+self.var2

    def differenza(self):
        return self.var1-self.var2

    @Input
    def var(self):
        return 17.0
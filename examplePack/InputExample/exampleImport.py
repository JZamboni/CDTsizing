from parapy.core import *
from examplePack.InputExample.mainEX import Airplane

class Imp(Base):

    aereo = Airplane()

    @Attribute
    def variabile(self):
        var = self.aereo.preghiamo
        return var *10



if __name__ == '__main__':
    from parapy.gui import display
    obj = Imp()
    display(obj)
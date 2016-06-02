from parapy.core import *
from MainFolder.Components.Fuselage.FuselageEX import fuselage
from MainFolder.Components.Fuselage.Geometry.fuselageLength import fuselageLength

class Airplane(Base):


    fuselage = fuselageLength()

    @Input
    def fuselage_Length(self):
        return 32.

    addizione = fuselage_Length+2

    @Attribute
    def addit(self):
        return self.addizione
    fuselage.setValue(value=fuselage_Length)

    @Attribute
    def preghiamo(self):
        return self.fuselage.getValue()

if __name__ == '__main__':
    from parapy.gui import display
    obj = Airplane()
    display(obj)
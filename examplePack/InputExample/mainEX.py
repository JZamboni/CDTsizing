from parapy.core import *
from MainFolder.Components.Fuselage.Geometry.fuselageLength import fuselageLength

class Airplane(Base):


    @Input
    def fuselage_Length(self):
        return 32.
    valore = fuselage_Length
    fus = fuselageLength()
    fuselage = fuselageLength()

    @Attribute
    def addit(self):
        return self.fuselage_Length*2

    @Attribute
    def preghiamo(self):
        add=self.fuselage_Length*2
        self.fuselage.setValue(value=add)
        return self.fuselage.getValue()

    @Part
    def imp(self):
        return Imp

if __name__ == '__main__':
    from parapy.gui import display
    obj = Airplane()
    display(obj)
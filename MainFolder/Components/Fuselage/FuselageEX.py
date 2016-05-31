from parapy.core import *
from Geometry.fuselageLength import fuselageLength

class fuselage(Base):

    @Input
    def fuselageLengthBASE(self):
        var = Airplane.variabile
        return 6.0

if __name__ == '__main__':
    from parapy.gui import display
    obj=fuselage()
    display(obj)
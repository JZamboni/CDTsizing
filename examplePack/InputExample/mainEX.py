from parapy.core import *
from MainFolder.Components.Fuselage.FuselageEX import fuselage

class Airplane(Base):

    @Input
    def variabile(self):
        return 4.0


if __name__ == '__main__':
    from parapy.gui import display
    obj = Airplane()
    display(obj)
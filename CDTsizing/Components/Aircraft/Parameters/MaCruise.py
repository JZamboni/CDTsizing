from CDTsizing.Core.parameter import Parameter
from parapy.core import *


class MaCruise(Parameter):
    '''
    The cruise Mach number.

    :Unit: []
    '''

    def __init__(self, value=0.78, unit='', parent='Aircraft.Parameters'):
        super(MaCruise, self).__init__(value=value, unit=unit, status='default', parent=parent)

    @Input
    def Mach(self):
        return 1.0

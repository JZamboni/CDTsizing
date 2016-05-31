from MainFolder.Core.Parameter import parameter

class fuselageLength(parameter):
    '''
    Aircraft fuselage length

    :Unit: [m]
    '''

    def __init__(self, name='Fuselage Length', value=30.0, unit='m', status='default',
                 parent=None, discipline='Aircraft', upperBound=None, lowerBound=0.0, boundaryCheck=False, **kwargs):
        super(fuselageLength, self).__init__(name=name, value=value, unit=unit, status=status, parent=parent,
                                             discipline=discipline, upperBound=upperBound, lowerBound=lowerBound,
                                             boundaryCheck=boundaryCheck, **kwargs)
        print(value)

        ###################################################################################################
        # EOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFEOFE#
        ###################################################################################################
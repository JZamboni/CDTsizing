class parameter(dict):
    '''
    **Superclass for all Parameters**

    A parameter holds the design knowledge. All parameters in the model need to inherit this class.

    Each parameter holds several attributes:

    * value

      The value of the parameter in the corresponding unit.

    * unit

      The unit of the parameter in SI units.

    * type

        The type of the parameter (e.g. int, float, str...)

    * status

      The status of a parameter influences the actions taken during the calculation. It can have different values:

        * "given"  by user input, may not be changed
        * "default" either a default value or a calculated value depending on the method used by the parameter

    * boundary

        The boundary of the parameter. It has both an upper and lower bound.

    * parent

        Indicates the parent of the parameter.

    * discipline

        Indicates the discipline of the parameter.

    * boundaryCheck

        Boolean value to signal if the user input is outside of the boundary.

    '''

    def __init__(self, name='', value=0.0, unit='', status='default',
                 parent=None, discipline=None, upperBound=None, lowerBound=None, boundaryCheck=False, **kwargs):

        self.name = name
        self.value = value
        self.unit = unit
        self.status = status
        self.parent = parent
        self.discipline = discipline
        self.upperBound = upperBound
        self.lowerBound = lowerBound
        self.boundaryCheck = boundaryCheck

    def restrictToBounds(self, value):
        too_small = False
        too_big = False
        if self.lowerBound is not None and value < self.lowerBound:
            too_small = True
        if self.upperBound is not None and value > self.upperBound:
            too_big = True

    #### Getter ####

    def getUnit(self):
        '''
        Returns the unit of the parameter
        '''
        return self.unit

    def getName(self):
        '''
        Returns the name of the parameter
        '''
        return self.name

    def getDiscipline(self):
        '''
        Returns the discipline of the parameter
        '''
        return self.discipline

    def getStatus(self):
        '''
        Returns the status of the parameter
        '''
        return self.status

    def getValue(self):
        '''
        Returns the value of the parameter
        '''
        return self.value

    # Setters
    def setUnit(self, unit=''):
        '''
        Sets the unit of the parameter
        '''
        self.unit = unit
        return self.unit

    def setName(self, name=''):
        '''
        Sets the name of the parameter
        '''
        self.name = name
        return self.name

    def setDiscipline(self, discipline=''):
        '''
        Sets the discipline of the parameter
        '''
        self.discipline = discipline
        return self.discipline

    def setStatus(self, status=''):
        '''
        Sets the status of the parameter
        '''
        self.status = status
        return self.status

    def setValue(self, value=''):
        '''
        Sets the value for a parameter.
        '''
        self.value=value
        return self.value
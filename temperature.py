class Temperature:
    def __init__(self, degree, unit = 'C'):
        self._degree = degree
        self._unit = unit
        if type(self._degree) not in {int, float}:
            raise TypeError('degree should be an int or float type')
        if self._unit.upper() not in {'C', 'F'}:
            raise ValueError('unit shoeld be C or F')
    def __repr__(self):
        return f'{self._degree:.1f} {self._unit}'
    def get_temp(self, unit_of_temp = 'C'):
        if unit_of_temp == self._unit:
            return (self._degree, self._unit)
        else:
            if unit_of_temp == 'F':
                return (self._degree * 1.8 + 32, unit_of_temp)
            else:
                return ((self._degree - 32) / 1.8, unit_of_temp)

        

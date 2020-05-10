def check_range(field_name, field_value, L, U):
    if not (L <= field_value <= U):
        raise ValueError(f'{field_name} must be {L} .. {U}')

class DateTime:
    def __init__(self, year, month, day, hour, minute, second):
        self.set_year(year)
        self.set_month(month)
        self.set_day(day)
        self.set_hour(hour)
        self.set_minute(minute)
        self.set_second(second)
    def set_year(self, year):
        if type(year) != int:
            raise TypeError('year must be int')
        self._year = year
    def set_month(self, month):
        check_range('month', month, 1, 12)
        self._month = month
    def set_day(self, day):
        if self._month in {1, 3, 5, 7, 8, 10, 12}:
            check_range('day', day, 1, 31)
        elif self._month in {4, 6, 9, 11}:
            check_range('day', day, 1, 30)
        elif leap(self._year):
            check_range('day', day, 1, 29)
        else:
            check_range('day', day, 1, 28)
        self._day = day
    def set_hour(self, hour):
        check_range('hour', hour, 0, 23)
        self._hour = hour
    def set_minute(self, minute):
        check_range('minute', minute, 0, 59)
        self._minute = minute
    def set_second(self, second):
        check_range('second', second, 0, 59)
        self._second = second


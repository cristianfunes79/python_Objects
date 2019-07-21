class Employer:

    emp_counter = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@embbit.com'

    def getFullname(self):
        return '{} {}'.format( self.first, self.last )

    @classmethod
    def createEmployer(cls, first, last,pay):
        cls.emp_counter = cls.emp_counter + 1
        return cls( first, last, pay )

    @staticmethod
    def printsomething(value):
        print('value: ' + value)

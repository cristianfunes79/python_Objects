class Employer:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@embbit.com'

    def getFullname(self):
        return '{} {}'.format( self.first, self.last )

class MathClass:

    def __init__(self, arg, arg1=0):
        self.arg = arg

    def double(self):
        print( self.arg * 2)

    def mult(self, arg1):
        self.arg1 = arg1
        print( self.arg * self.arg1 )

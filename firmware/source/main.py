from mathClass import *
from employerClass import *

#this is working!
clase_aux = MathClass(2)
clase_aux.double()
clase_aux.mult(5)

emp1 = Employer('cristian', 'funes', 120000)
print(emp1)
print('{} {}'.format(emp1.first, emp1.last))

print(' fullname: ' + emp1.getFullname())

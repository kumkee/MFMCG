from hamiltonian import ham
from drawing import *
from edensity import *
from sympy import *
from copy import deepcopy

U, J, d, o, a, s = symbols('U J d o a s')
h = ham(width=4,length=5,boundary='p',holes=[[2,2]],
	coulomb=U, spincoupling=J, Ed=d, vibration=o, ssh=a)
c = eden(h)
#drawgraphene(h.g,output='hg.eps')
print "h:", h
print "c:", c
b = deepcopy(c)
b.eden = array(map(lambda x:x+(-1)**x*0.9, c.eden))
mt = array([h.Ht([i,j]) for j in range(h.dim) for i in range(h.dim)])
mt.shape = h.dim, h.dim

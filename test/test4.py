from hamiltonian import ham
from drawing import *
from edensity import *
from sympy import *
from copy import deepcopy

U, J, d, o, a, V0, V1, V2, s = symbols('U J d o a V0 V1 V2 s')
h = ham(width=4,length=5,boundary='p',holes=[[2,2]],
	coulomb=U, spincoupling=J, Ed=d, vibration=o, ssh=a)
c = eden(h)
c.V = [V0, V1, V2]
#drawgraphene(h.g,output='hg.eps')
print "h:", h
print "c:", c
b = deepcopy(c)
s = .9
b.eden = array(map(lambda x:x+(-1)**x*s, c.eden))
mt = array([h.Ht([i,j]) for j in range(h.dim) for i in range(h.dim)]);mt.shape = h.dim, h.dim
mo = array([h.Ho([i,j]) for j in range(h.dim) for i in range(h.dim)]);mo.shape = h.dim, h.dim
h.displace(1,[.01,.01])
mt = array([h.Ht([i,j]) for j in range(h.dim) for i in range(h.dim)]);mt.shape = h.dim, h.dim
mo = array([h.Ho([i,j]) for j in range(h.dim) for i in range(h.dim)]);mo.shape = h.dim, h.dim
h.displace(6,[0.,-.02])
mt = array([h.Ht([i,j]) for j in range(h.dim) for i in range(h.dim)]);mt.shape = h.dim, h.dim
mo = array([h.Ho([i,j]) for j in range(h.dim) for i in range(h.dim)]);mo.shape = h.dim, h.dim
h.displace(4,[0.,.02])
mt = array([h.Ht([i,j]) for j in range(h.dim) for i in range(h.dim)]);mt.shape = h.dim, h.dim
mo = array([h.Ho([i,j]) for j in range(h.dim) for i in range(h.dim)]);mo.shape = h.dim, h.dim
mu0 = array([h.Hu(0,c,[i,j]) for j in range(h.dim) for i in range(h.dim)]);mu0.shape = h.dim, h.dim
mu1 = array([h.Hu(1,c,[i,j]) for j in range(h.dim) for i in range(h.dim)]);mu1.shape = h.dim, h.dim
mu0b = array([h.Hu(0,b,[i,j]) for j in range(h.dim) for i in range(h.dim)]);mu0b.shape = h.dim, h.dim
mu1b = array([h.Hu(0,b,[i,j]) for j in range(h.dim) for i in range(h.dim)]);mu1b.shape = h.dim, h.dim
mj0 = array([h.Hj(0,c,[i,j]) for j in range(h.dim) for i in range(h.dim)]);mj0.shape = h.dim, h.dim
mj1b = array([h.Hj(1,b,[i,j]) for j in range(h.dim) for i in range(h.dim)]);mj1b.shape = h.dim, h.dim
mj0b = array([h.Hj(0,b,[i,j]) for j in range(h.dim) for i in range(h.dim)]);mj0b.shape = h.dim, h.dim
mj1 = array([h.Hj(1,c,[i,j]) for j in range(h.dim) for i in range(h.dim)]);mj1.shape = h.dim, h.dim
m0 = array([h.Hall(0,c,[i,j]) for j in range(h.dim) for i in range(h.dim)]);m0.shape = h.dim, h.dim


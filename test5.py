from hamiltonian import *
from numpy import *
from scipy.sparse import *
from scipy import *

h = ham(width=4,length=5,boundary='p',holes=[[2,2]])
c = eden(h)
m = [[],[]]
mc = [[],[]]
mcsr = [[],[]]
s = 0
m[s] = array([ h.Hall(s,c,[i,j]) for j in xrange(h.dim) for i in xrange(h.dim) ])
m[s].shape = h.dim,h.dim
mcsr[s] = h.matcsr(s,c)
mc[s] = mcsr[s].todense()
s = 1
m[s] = array([ h.Hall(s,c,[i,j]) for j in xrange(h.dim) for i in xrange(h.dim) ])
m[s].shape = h.dim,h.dim 
mcsr[s] = h.matcsr(s,c)
mc[s] = mcsr[s].todense()
print 'm[s] = array([ h.Hall(s,c,[i,j]) for j in xrange(h.dim) for i in xrange(h.dim) ])'
print 'mc[s] = h.matcsr(s,c).todense()'
print 'product(m[0]==mc[0]):', product(m[0]==mc[0])
print 'product(m[1]==mc[1]):', product(m[1]==mc[1])


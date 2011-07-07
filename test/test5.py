from hamiltonian import *
from numpy import *
from scipy.sparse import *
from scipy import *
from scipy.linalg import eigh
from time import clock

#print 'h = ham(width=20,length=40,boundary=\'p\',holes=[[2,2]])'
h = ham(width=20,length=40,boundary='p',holes=[[2,2]])
c = eden(h)
m = [[],[]]
mc = [[],[]]
mcoo = [[],[]]
s = 0
t = clock();print t #------------------------------------------------------
#m[s] = array([ h.Hall(s,c,[i,j]) for j in xrange(h.dim) for i in xrange(h.dim) ])
#m[s].shape = h.dim,h.dim
#print 'm[s] = array([ h.Hall(s,c,[i,j]) for j in xrange(h.dim) for i in xrange(h.dim) ])'
#print clock()-t;t = clock() #------------------------------------------------------
mcoo[s] = h.matcoo(s,c)
print clock()-t;t = clock() #------------------------------------------------------
mc[s] = mcoo[s].todense()
print 'mc[s] = h.matcoo(s,c).todense()'
print clock()-t;t = clock() #------------------------------------------------------
s = 1
#m[s] = array([ h.Hall(s,c,[i,j]) for j in xrange(h.dim) for i in xrange(h.dim) ])
#m[s].shape = h.dim,h.dim 
#print 'm[s] = array([ h.Hall(s,c,[i,j]) for j in xrange(h.dim) for i in xrange(h.dim) ])'
#print clock()-t;t = clock() #------------------------------------------------------
mcoo[s] = h.matcoo(s,c)
print clock()-t;t = clock() #------------------------------------------------------
mc[s] = mcoo[s].todense()
print 'mc[s] = h.matcoo(s,c).todense()'
print clock()-t;t = clock() #------------------------------------------------------
#print 'product(m[0]==mc[0]):', product(m[0]==mc[0])
#print 'product(m[1]==mc[1]):', product(m[1]==mc[1])
w, v = eigh(mc[0])
#print w
print clock()-t #------------------------------------------------------


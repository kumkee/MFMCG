#test for contrution of mfiter
from hamiltonian import *
from edensity import *
from scipy.linalg import *
from scipy.optimize import newton
from mfiter import *
h = ham()
c = eden(h)
T = RT
N = map(sum,c.den)
m =map(lambda s:h.mat(s,c), [0,1])
w, v= [[],[]], [[],[]]
(w[0],v[0]), (w[1],v[1]) = map(eigh, m)
d = map(lambda s:array(map(lambda x:x**2, v[s].T)), [0,1])
d0 = map(lambda s:mat(map(lambda i:v[s][:,i]**2, xrange(h.dim))), [0,1])
def eqfermi(mu,N,w,T=RT):
   return N - sum( fermi(w,mu,T) )
   #return map( lambda s: N[s] - sum( vfermi(w[s],mu[s],T) ), [0,1] )
def chempot(N,energy,temp,mu0):
   return newton(eqfermi,mu0,args=(N,energy,temp))

mu = [[],[]]
mu[0] = chempot(N[0],w[0],T,w[0][33])
mu[1] = chempot(N[1],w[1],T,mu[0])
print mu
print map(lambda s:eqfermi(mu[s],N[s],w[s]), [0,1])
n = mat(map(lambda s: map(lambda i:sum(fermi(w[s][:],mu[s],T)*d[s][:,i]),
						xrange(h.dim)), xrange(2)))
c.den = n

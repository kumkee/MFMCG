from hamiltonian import *
from scipy.linalg import *
from scipy.optimize import newton

RT = 1.034e-2

#@tc.parallel()
def fermi(energy,chempot,temp=RT):
   return 1./( exp((energy-chempot)/temp) + 1. )

vfermi = vectorize(fermi)


def chempot(N,energy,temp,mu0):
   return newton(eqfermi,mu0,args=(N,energy,temp))


def eqfermi(mu,N,w,T):
   return N - sum( fermi(w,mu,T) )


def mfiter(hamiltonian,eden,temp=RT,mu0=None):
   h = hamiltonian
   c = eden
   T = temp
   N = map(sum,c.den)
   w, v, mu = [[],[]], [[],[]], [[], []]

   m = map(lambda s: h.mat(s,c), [0,1])
   (w[0],v[0]), (w[1],v[1]) = map(eigh, m)
   d = map(lambda s:array(map(lambda x:x**2, v[s].T)), [0,1])

   if(mu0==None): mu0 = w[0][N[0]]
   mu[0] = chempot(N[0],w[0],T,mu0)
   mu[1] = chempot(N[1],w[1],T,mu[0]) 

   n = mat(map(lambda s: map(lambda i:sum(fermi(w[s][:],mu[s],T)*d[s][:,i]),
						xrange(h.dim)), xrange(2)))
   
   V = 0

   return n, V

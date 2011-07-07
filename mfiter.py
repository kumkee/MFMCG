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

def mindiff(c,d):
   r = min(map(min, abs(c.den-d.den)))
   if(c.V!=[]):
      t = min(abs(c.V-d.V))
      r = min(r,t)
   return r

def meanfield(h,c,tol=1e-8):
   d = 1.
   i = 0
   while(d>=tol):
      n = mfiter(h,c)
      d = mindiff(n,c)
      c = deepcopy(n)
      i += 1
      print i, d
   return n

def mfiter(hamiltonian,eden,temp=RT,mu0=None):
   h = hamiltonian
   c = eden
   T = temp
   N = map(sum,c.den)
   n = deepcopy(c)
   w, v, mu = [[],[]], [[],[]], [[], []]

   m = map(lambda s: h.mat(s,c), [0,1])
   #mat only contains the upper triangle part of the matrix
   (w[0],v[0]), (w[1],v[1]) = map(eigh, m)
   #w[s][j]: eigenergies for single-particle state j with spin s
   #v[s][:,j]: the coresponding eigenstate j,s
   d = map(lambda s:array(map(lambda x:x**2, v[s].T)), [0,1])
   #d[s][j,i]: density distribution of state j,s at site i

   if(mu0==None): mu0 = w[0][N[0]]
   mu[0] = chempot(N[0],w[0],T,mu0)
   mu[1] = chempot(N[1],w[1],T,mu[0]) 

   n.den = array(map(lambda s: map(lambda i:sum(fermi(w[s][:],mu[s],T)*d[s][:,i]),
						xrange(h.dim)), xrange(2)))
   
   if(h.g.ndvertex()!=0):
      V = [ sum([ -fermi(w[s][j],mu[s],T) * v[s][i,j] * v[s][h.id2i(i),j] 
		for j in xrange(h.dim) for s in xrange(2) ])
			for i in xrange(h.g.nvertex(),h.dim) ]
      n.V = array(V)

   return n

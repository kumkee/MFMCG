from hamiltonian import *
from scipy.linalg import *
from scipy.optimize import brentq#newton, fsolve

RT = 1.034e-2

#@tc.parallel()
def fermi(energy,chempot,temp=RT):
   return 1./( exp((energy-chempot)/temp) + 1. )

vfermi = vectorize(fermi)

def chempot(N,levels,temp):
   def f(x):
      return eqfermi(x,N,levels,temp)
   w0, wn = levels[0], levels[-1]
   if(wn<w0): w0, wn = wn, w0
   while(f(wn)*f(w0)>0):
      w0, wn = w0-(wn-w0), wn+(wn-w0)
   return brentq(eqfermi,w0,wn,args=(N,levels,temp))

def eqfermi(mu,N,w,T):
   return N - sum( vfermi(w,mu,T) )

def maxdiff(c,d):
   r = max(map(max, abs(c.eden-d.eden)))
   #if(c.V!=[]):
   #   t = min(abs(c.V-d.V))
   #   r = min(r,t)
   return r

def meanfield(h,c,tol=1e-7):
   d = 1.
   i = 0
   while(d>=tol):
      n, mu0 = mfiter(h,c)
      d = maxdiff(n,c)
      c = deepcopy(n)
      i += 1
      print i, d
   return n

def mfiter(hamiltonian,eden,temp=RT,mu0=None):
   h = hamiltonian
   c = eden
   T = temp
   N = map(sum,c.eden)
   n = deepcopy(c)
   w, v = [[],[]], [[],[]]

   m = map(lambda s: h.mat(s,c), [0,1])
   #mat only contains the upper triangle part of the matrix
   (w[0],v[0]), (w[1],v[1]) = map(eigh, m)
   #w[s][j]: eigenergies for single-particle state j with spin s
   #v[s][:,j]: the coresponding eigenstate j,s
   d = map(lambda s:array(map(lambda x:x**2, v[s].T)), [0,1])
   #d[s][j,i]: density distribution of state j,s at site i

   mu = map(lambda s: chempot(N[s],w[s],T), [0,1])

   n.eden = array(map(lambda s: map(lambda i:sum(fermi(w[s][:],mu[s],T)*d[s][:,i]),
						xrange(h.dim)), xrange(2)))
   
   '''if(h.g.ndvertex()!=0):
      V = [ sum([ -fermi(w[s][j],mu[s],T) * v[s][i,j] * v[s][h.id2i(i),j] 
		for j in xrange(h.dim) for s in xrange(2) ])
			for i in xrange(h.g.nvertex(),h.dim) ]
      n.V = array(V)'''

   return n, mu

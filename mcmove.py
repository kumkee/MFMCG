from numpy import array
from numpy.random.mtrand import RandomState
from mfiter import RT, mfiter
from copy import deepcopy
from math import exp

dfseed = 31415927

class myrand(object):
   @property
   def dxy(self): return self.__dxy
   @property
   def site(self): return self.__site
   @property
   def acc(self): return self.__acc
   def __init__(self,h,cutoff=0.2,seed=dfseed):
      dummy = RandomState(seed)
      s1, s2, s3 = 0,0,0
      while(s1==s2 or s1==s3 or s2==s3):
	s1, s2, s3 = dummy.randint(low=4294967296,size=3)
      self.__dxy = randxy(s1,cutoff)
      self.__site = randsite(s2,h.dim)
      self.__acc = randgen(s3)

def mcmove(h0,T=RT,den=None,cutoff=0.2,tol=1.e-7):
   count = 0 
   accept = True
   disp = (0,[0,0])
   r = myrand(h0,cutoff,seed=h0.g.size(1)+h0.g.holes())

   n0, en0 = mfiter(h0,den=den,temp=T,tol=tol)

   while(True):
      yield disp, n0, en0, accept
      count += 1

      h1 = deepcopy(h0)
      disp = (r.site.next(),r.dxy.next())
      h1.displacei(disp[0],disp[1])
      n1, en1 = mfiter(h1,den=n0,temp=T,tol=tol)
      accept = (r.acc.next() < exp(-(en1-en0)/T))

      if(accept):
	h0 = deepcopy(h1)
	n0.eden = n1.eden
        en0 = en1
      #else:
	#disp = None


def randxy(seed,cutoff=1.0):
   r = RandomState(seed)
   while(True):
      yield array(r.uniform(-cutoff,cutoff,2))

def randsite(seed,dim):
   r = RandomState(seed)
   while(True):
      yield r.randint(dim)

def randgen(seed):
   r = RandomState(seed)
   while(True):
      yield r.rand()



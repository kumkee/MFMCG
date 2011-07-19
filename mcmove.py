from numpy import array
from numpy.random.mtrand import RandomState

dfseed = 31415927

class myrand(object):
   @property
   def dxy(self): return self.__dxy
   @property
   def site(self): return self.__site
   def __init__(self,h,cutoff=0.2,seed=dfseed):
      dummy = RandomState(seed)
      s1, s2 = dummy.randint(low=4294967296,size=2)
      self.__dxy = randxy(s1,cutoff)
      self.__site = randsite(s2,h.dim)

def randxy(seed,cutoff=1.0):
   r = RandomState(seed)
   while(True):
      yield array(r.uniform(-cutoff,cutoff,2))

def randsite(seed,dim):
   r = RandomState(seed)
   while(True):
      yield r.randint(dim)

#def mcmove(h0):

from mcmove import mcmove
from numpy import zeros
from mfiter import RT

dc = 0.003

def metropolis(h,T=RT,cutoff=dc):
   mc = mcmove(h,T=RT,cutoff=cutoff)
   Ssize = h.dim * 10
   while(True):
      count = 0
      Sd = zeros((h.dim,2),dtype=float)
      Sn = zeros((2,h.dim),dtype=float)
      Sen = 0
      for i in xrange(Ssize):
	d, n, en, a = mc.next()
	if(a):
	   Sd[d[0]] = d[1]
	   count += 1
	Sen += en
	Sn += n.eden
      yield Sd/Ssize, Sn/Ssize, Sen/Ssize, float(count)/Ssize

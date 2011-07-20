from hamiltonian import *
from mcmove import mcmove

cutoff=0.003
h = ham(length=5,width=4,holes=[[2,1]])
mc = mcmove(h,cutoff=cutoff)
d, n, en, a = mc.next()
count = 0
a=False
for i in xrange(20000):
   print i, a
   d, n, en, a = mc.next()
   if(a): count += 1
print 'cutoff =', cutoff
print 'holes =', h.g.holes()
print (count+1.)/(i+1.)

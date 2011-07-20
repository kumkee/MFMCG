from hamiltonian import ham
from metropolis import metropolis

cutoff=0.003
h = ham(length=5,width=4,holes=[[2,1]])
mt = metropolis(h,cutoff=cutoff)
for i in xrange(10):
   d, n, en, a = mt.next()
   print ''
   print '*****************'
   print '   Cycle %s      ' % (i)
   print '*****************'
   print ''
   print 'Acceptance rate:', a
   print ''
   print 'Average particle densities:'
   print n
   print ''
   print 'Average displacements:'
   print d

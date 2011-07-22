from os import mkdir, getcwd
from cPickle import dump
from math import log10
from hamiltonian import ham
from metropolis import metropolis
from mfiter import RT

cutoff=0.0032
h = ham(width=10,length=21,boundary='o',holes=[[5,8],[5,12]])
ncir = 110
T = 2.

lcir = int(log10(ncir)) + 1
dpath = 'data/'
ddir = dpath + str(h.g)# + '/'
if(T!=1.0):
   ddir += '_' + str(T) + 'RT'
ddir += '/'

print 'data stored in', ddir
try:
   mkdir(dpath)
except:
   print dpath,'exist'
try:
   mkdir(ddir)
except:
   raise OSError('Directory ' + ddir + ' exists.')

mt = metropolis(h,T=T*RT,cutoff=cutoff)
for i in xrange(ncir):
   df = open(ddir + 'c' + str(i).zfill(lcir) + '.dat', 'w')
   d, n, en, a = mt.next()
   dump((i,d,n,en,a), df, -1)
   print ''
   print '*****************'
   print '   Cycle %s      ' % (i)
   print '*****************'
   print ''
   print 'Acceptance rate:', a
   print ''
   print 'Average energies:', en
   print ''
   df.close()

from cPickle import load
def datname(T,g):
   ddir = str(g)
   if(float(T) != 1.0):
      ddir += '_' + str(T) + 'RT'
   return ddir + '/'

def drender(ddir,flist):
   for fstr in flist:
      f = open(ddir+fstr,'r')
      yield load(f)
      f.close()


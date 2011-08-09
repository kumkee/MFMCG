from sympy import *
from mfiter import *
import time
#from multiprocessing import Pool

if __name__ == '__main__':
   h = ham(width=10,length=20,holes=[[1,2]])
   t = time.time()
   #p = Pool(processes=2)
   n, etot = mfiter(h)#,pool=p)
   print etot
   #n = meanfield(h)
   print time.time()-t

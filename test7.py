from sympy import *
from mfiter import *
import time

h = ham(width=10,length=20,holes=[[1,2]])
t = time.time()
n = meanfield(h)
print time.time()-t

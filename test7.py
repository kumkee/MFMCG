from mfiter import *

h = ham(width=4,length=5,holes=[[1,2]])
#h = ham(width=8,length=11)
#h = ham()
c = eden(h)
n = mfiter(h,c)
#n = meanfield(h,c)

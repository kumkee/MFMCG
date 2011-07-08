from sympy import *
from mfiter import *

h = ham(width=10,length=20,holes=[[1,2]])
#U, J, d, o, a, V0, V1, V2, s = symbols('U J d o a V0 V1 V2 s')
#h = ham(width=4,length=5,boundary='p',holes=[[1,2]],
#	coulomb=U, spincoupling=J, Ed=d, vibration=o, ssh=a)
#h = ham(width=8,length=11)
#h = ham()
c = eden(h)
'''n = mfiter(h,c)
d = mfiter(h,n)
n = mfiter(h,d)'''
#n = mfiter(h,c)
n = meanfield(h,c)
#m0 = h.mat(0,c)
#m1 = h.mat(1,c)
#m0 = mat([h.Hall(0,c,[i,j]) for i in xrange(h.dim) for j in xrange(h.dim)])

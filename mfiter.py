from hamiltonian import *

def fermi(energy,temp,champot):
   return 1./( exp((energy-champot)/temp) + 1. )

def mfiter(hamiltonian,eden):
   h = hamiltioan
   c = eden
   w, v = [[],[]], [[],[]]
   for s in [0,1]:
      w[s], v[s] = h.mat(s,c)

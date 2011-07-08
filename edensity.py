from numpy import *

def flip(x):
   return (not x)*1
   
def spinud(d,u):
   return (u-d)/2.

class eden(object):
   @property
   def g(self): return self.__g
   @property
   def h(self): return self.__h
   @property
   def den(self): return self.__den
   @den.setter
   def den(self,newd):
    try:
      if(self.__den.shape==newd.shape):
	self.__den = newd
      else:
	try: 1/0
	except:
	   print "den shapes not match"
	raise
    except:
      print "den require an array"
      raise
   @property
   def eden(self): return self.__den[:,:self.__nc]
   @eden.setter
   def eden(self,newd):
      self.__den[:,:self.__nc] = newd
   @property
   def dden(self):
      if(self.__nd!=0):
	return self.__den[:,-self.__nd:]
      else:
	return []
   @dden.setter
   def dden(self,newd):
      if(self.__nd!=0):
	self.__den[:,-self.__nd:] = newd
   @property
   def V(self): return self.__V
   @V.setter
   def V(self,newv):
      self.__V = newv
   def __init__(self,h,density=None,vinit=None,dspin=None):
      self.__g = h.g
      self.__h = h
      self.__nd = self.g.ndanglingc()
      self.__nc = self.g.nvertex()
      self.__den = zeros((2,self.__nc+self.__nd),dtype=float)
      if(vinit==None):
	self.__V = ones(self.__nd,dtype=float)*(-1. if h.J>0 else 1.)
      else:
	self.__V = ones(self.__nd,dtype=float)*vinit
      if(density==None):
	for i in xrange(self.__nc):
	   sl = self.g.sublat( self.h.i2p(i,'1d') )
	   self.den[:,i] = [sl, flip(sl)]
      else:
	self.eden = density
      if(self.__nd!=0):
	if(dspin==None):
	   self.dden[1,:] = 1.
	else:
	   sf = map(flip,density)
	   for i in xrange(self.__nd):
	      self.dden[:,i] = [flip(sf[i]),sf[i]]
   def spin(self,i):
      return reduce(spinud, self.den[:,i])#(self.den[1,i] - self.den[0,i]) /2.
   def Vi(self,i):
      if(self.h.iind(i)):
	return self.V[i-self.__nc]
      elif(self.h.iinC(i)):
	if(self.h.iind(self.h.i2id(i))):
	   return self.V[self.h.i2id(i)-self.__nc]
      else:
	try: 1/0
	except:
	   print "ERROR: i not a dangling C or spin"
	   raise

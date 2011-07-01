import graphene as grap
from numpy.linalg import norm
from numpy import *

class ham(object):
   @property
   def t0(self):return self.__t0
   @property
   def g(self): return self.__g
   @property
   def U(self): return self.__U
   @property
   def J(self): return self.__J
   @property
   def ed(self):return self.__ed
   @property
   def omg(self):return self.__omg
   @property
   def alp(self):return self.__alp
   @property
   def osc(self):return self.__osc
   def __init__(self,width=6,length=10,boundary="open",holes=[],ledge=1.,
			graphene=None, hopping=-1.0,coulomb=2.0,
			spincoupling=0.1, Ed=1.0, vibration=20.0, ssh=2.0 ):
      if(graphene==None):
	self.__g = grap.graphene(width,length,boundary,holes,ledge)
      else:
	self.__g = graphene
      self.__t0 = hopping
      self.__U = coulomb
      self.__J = spincoupling
      self.__ed = Ed
      self.__omg = vibration
      self.__alp = ssh
      self.__osc = 0. 
      for i,j in self.g.lslinks('1d'):
	p = self.g.dispm(i)
	q = self.g.dispm(j)
	print "i: %s, j: %s	p,q: %s,%s" % (i,j,p,q)
	self.__osc += norm(p-q)**2
      self.__osc *= self.omg
      #def tmp(x): 
	#return norm(self.g.dispm(x.item(0))-self.g.dispm(x.item(1)))**2
      #self.__osc = self.__omg * sum(map(tmp,self.g.lslinks('1d')))
 
   def lmd(self): return self.alp**2/self.t0/self.omg

   def tij(self,ppair):
      d = map(self.g.dispm,ppair)
      return self.t0 * (1.0 - self.alp*norm(d[0]-d[1])) \
		* self.g.isC(ppair[0]) * self.g.isC(ppair[1]) \
			* self.g.link(ppair[0],ppair[1])

   def oscp(self,pp=0):
      return 1

import graphene as grap
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
      self.__osc = reduce(lambda x,y:x+y, 
		      map(lambda x:reduce(self.g.ddispm,x)**2, self.g.lslinks('1d')))
 
   def lmd(self): return self.alp**2/self.t0/self.omg
   
   def displace(self,p,d):
      def f(x):
	return self.g.isC(p) * self.g.ddispm(p,x)**2
      pnb = self.g.pbneighb(p,'1d')
      self.__osc -= reduce(lambda x,y:x+y, map(f,pnb))
      self.g._displace(p,d)
      self.__osc += reduce(lambda x,y:x+y, map(f,pnb))

   def diag(self,pp):
      return 1 if self.g.pnt(pp[0],'1d')==self.g.pnt(pp[1],'1d') else 0

   def tij(self,ppair):
      return self.t0 * (1.0 - self.alp*reduce(self.g.ddistance,ppair)) \
			* self.g.allC(ppair) * reduce(self.g.link,ppair)
   def oscp(self,pp):
      return self.omg * self.osc * self.diag(pp) * self.g.allC(pp)

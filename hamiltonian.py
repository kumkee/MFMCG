from graphene import *

class ham(object):
   def __init__(self,width=6,length=10,boundary="open",holes=[],ledge=1.,hopping=1.0,coulomb=2.0,
			spincoupling=0.1, Ed=1.0, vibration=20, ssh=2 ):
      self.__g = graphene(width,length,boundary,holes,ledge)
      self.__t0 = hopping
      self.__U = coulomb
      self.__J = spincoupling
      self.__ed = Ed
      self.__omg = vibration
      self.__alp = ssh
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
 
   def lmd(self): return self.alp**2/self.t0/self.omg

import graphene as grap
from numpy import *
from edensity import *

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
      self.__osc = sum( 
		      map(lambda x:reduce(self.g.ddispm,x)**2, self.g.lslinks('1d')))
      self.__nd = self.g.ndanglingc()
      self.__nc = self.g.nvertex()
      self.__dim = self.__nc + self.__nd
 
   def lmd(self): return self.alp**2/self.t0/self.omg
   
   def displace(self,p,d):
      def f(x):
	return self.g.isC(p) * self.g.ddispm(p,x)**2
      pnb = self.g.pbneighb(p,'1d')
      self.__osc -= sum(map(f,pnb))
      self.g._displace(p,d)
      self.__osc += sum(map(f,pnb))

   def diag(self,ip):
      if(ip[0]!=ip[1]):
	return 0
      elif(self.iinC(ip[0]) or self.iind(ip[1])):
        return 1
      else:
	return 0

   def tij(self,ppair):
      return self.t0 * (1.0 - self.alp*reduce(self.g.ddistance,ppair)) \
			* self.g.allC(ppair) * reduce(self.g.link,ppair)
   def oscp(self,pp):
      return self.omg * self.osc * self.diag(pp) * self.g.allC(pp)

   def Hu(self,spin,eden,ip):
      if(product(map(self.iinC,ip))==0):
	return 0
      elif(self.diag(map(self.i2p,ip))==0):
	return 0
      else:
	i = ip[0]
	tmp = 0
	if(self.iinC(i)):
	   tmp = eden.eden[flip(spin),i]
	tmp -= dot(eden.eden[0], eden.eden[1])
	return self.U * tmp

   def Hj(self,spin,eden,ip):
      tmp = 0.
      if( not(product(self.iinCd))):
	return tmp
      else:
	di = map(self.p2i, self.g.danglingc('1d'))
	dd = range(self.__nc,self.__dim)
	if(self.diag(ip)):
	   tmp += dot( map( eden.spin, di ),
			   map(eden.spin, dd) )   #<S><S> term
	   tmp -= sum(map(lambda x:x**2, eden.V)) /2.			# V^2 term
	   i = ip[0]
	   if(i in di):
	      tmp -= (-1)**(spin+1) * eden.spin(self.i2id(i))
	   if(i in dd):
	      tmp -= (-1)**(spin+1) * eden.spin(self.id2i(i))
	i = ip[0]
	if(i in di):
	   tmp -= (-1)**(spin+1) * eden.spin(self.i2id(i))
	if(i in dd):
	   tmp -= (-1)**(spin+1) * eden.spin(self.id2i(i))
        return tmp

#---------------------------------------------------------------#
   def p2i(self,p):
      p = self.g.pnt(p,'1d')
      h = self.g.holes('1d')
      if(p in h):
	return None
      else:
	return p - len(filter(lambda x:x<p,h))
   def i2p(self,i,form='1d'):
      h = self.g.holes('1d')
      lenh = self.g.nholes()
      if(h[0]>i):
	p = i
      elif(h[-1]-lenh<i):
	p = i+lenh
      else:
	k = 0
	while(not(h[k]-k<i+1 and i+1<=h[k+1]-k-1)):
	   k += 1
	p = i + k+1
      return self.g.pnt(p,form)
   def iinC(self,i):
      return 1 if(0<=i and i<self.__nc) else 0
   def iind(self,i):
      return 1 if(self.__nc<=i and i<self.__nc+self.__nd) else 0
   def iinCd(self,i):
      return 1 if(self.iinC(i) or self.iind(i)) else 0
   def id2p(self,i,form='1d'):
      if not self.iind(i):
	try: 1/0
	except: print "id2p: i not a dangling point"
	raise
      else:
	return self.g.danglingc(form)[i-self.__nc]
   def id2i(self,i):
      return self.p2i(self.id2p(i))
   def p2id(self,d):
      d = self.g.pnt(d,'1d')
      i = list(self.g.danglingc('1d')).index(d)
      return i + self.__nc
   def i2id(self,i):
      return self.p2id(self.i2p(i))

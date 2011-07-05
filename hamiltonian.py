from numpy import *
from copy import deepcopy
import graphene as grap
from edensity import *
from scipy.sparse import *
from scipy import *

def redand(bl):
   return reduce(lambda x,y:x and y, bl)

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
   @property
   def dim(self):return self.__dim
   @property
   def lstij(self):return self.__lstij
   def __init__(self,width=6,length=10,boundary="open",holes=[],ledge=1.,
			graphene=None, hopping=1.0,coulomb=1.3,
			spincoupling=0.1, Ed=1.0, vibration=40.0, ssh=3.5 ):
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
			map(lambda x:reduce(self.g.ddispm,x)**2,
						self.g.lslinks('1d')))
      self.__nd = self.g.ndanglingc()
      self.__nc = self.g.nvertex()
      self.__dim = self.__nc + self.__nd
      self.__lstij = array(map( lambda x:map(self.p2i,x), self.g.lslinks('1d') ))
 
   def lmd(self): return self.alp**2/self.t0/self.omg
   
   def displace(self,p,d):
      def f(x):
	return self.g.isC(p) * self.g.ddispm(p,x)**2
      pnb = self.g.pbneighb(p,'1d')
      self.__osc -= sum(map(f,pnb))
      self.g._displace(p,d)
      self.__osc += sum(map(f,pnb))
   def displacei(self,i,d):
      p = self.i2p(i)
      self.displace(p,d)

   def diag(self,ip):	#ip: index-pair of the matrix
      if(not reduce(lambda x,y:x==y, ip)):
	return 0
      elif(redand(map(self.iinCd,ip))):
        return 1
      else:
	return 0

   def Ht(self,ip):
      if( redand(map(self.iinC,ip)) ):
        pp = map(self.i2p,ip)
	if( reduce(self.g.link,pp) ):
	   return -self.t0 * (1.0 - self.alp*reduce(self.g.ddistance,pp))
	return 0.
      else:
	return 0.

   def Hu(self,spin,eden,ip):
      if(not redand(map(self.iinCd,ip))):
	return 0
      elif(self.diag(ip)):
	i = ip[0]
	tmp = 0
	if(self.iinC(i)):
	   tmp = eden.eden[flip(spin),i] #<n>n term
	tmp -= reduce(dot,eden.eden)	 #<n><n> term
	return self.U * tmp
      else:
	return 0

   def Hj(self,spin,eden,ip):
      tmp = 0.
      if( not(reduce(lambda x,y:x and y, (map(self.iinCd,ip))) )):
	return tmp
      else:
	i = ip[0]
	j = ip[1]
	di = map(self.p2i, self.g.danglingc('1d')) #dangling vertece
	dd = xrange(self.__nc,self.__dim)	   #dangling spins
	if(self.diag(ip)):
	   tmp += dot( map(eden.spin, di), map(eden.spin, dd) )  # <S><S> term
	   tmp -= sum(map(lambda x:x**2, eden.V)) /2.		 # V^2 term
	   spin = 1 if spin else 0
	   if(i in di):
	      tmp -= (-1)**(spin+1) * eden.spin(self.i2id(i))/2. # <S>Sd terms
	   if(i in dd):
	      tmp -= (-1)**(spin+1) * eden.spin(self.id2i(i))/2. # <Sd>S terms
	else:
	   if(i in di):
	      if(self.i2id(i)==j):
		tmp -= eden.V[j-self.__nc]/2.
	   elif(i in dd):
	      if(self.id2i(i)==j):
		tmp -= eden.V[i-self.__nc]/2.
        return self.J * tmp

   def Hd(self,ip):
      if(redand(map(self.iind,ip)) and self.diag(ip) ):
	return self.ed
      else:
	return 0.

   def Ho(self,ip):
      if(redand(map(self.iinCd,ip)) and self.diag(ip)):
	return self.omg * self.osc
      else:
	return 0.

   def Hall(self,spin,eden,ip):
      return self.Ht(ip) + self.Hu(spin,eden,ip) + self.Hj(spin,eden,ip) \
		+ self.Hd(ip) + self.Ho(ip)

   def matcsr(self,spin,eden):
      return self.matcoo(spin,eden).tocsr()

   def mat(self,spin,eden):
      return self.matcoo(spin,eden).todense()

   def matcoo(self,spin,eden):
      #----initialization-----
      ll = len(self.lstij)
      n = self.dim + 2*ll + self.__nd*2
      row = zeros(n,dtype=int)
      dat = zeros(n,dtype=float)

      #---------Hdia-----------
      row[:self.dim] = xrange(self.dim)
      col = deepcopy(row)
      dat[:self.dim] = [self.Hall(spin,eden,[i,i]) for i in xrange(self.dim)]

      #----------Ht------------
      row[self.dim:self.dim+ll], col[self.dim:self.dim+ll] = self.lstij.transpose()
      col[self.dim+ll:self.dim+2*ll], row[self.dim+ll:self.dim+2*ll] = self.lstij.transpose()
      tmp = map(self.Ht, self.lstij)
      dat[self.dim : self.dim+ll] = tmp
      dat[self.dim+ll : self.dim+2*ll] = tmp

      #----------Hjo-----------
      di = map(self.p2i, self.g.danglingc('1d')) #dangling vertece
      dd = xrange(self.__nc,self.__dim)	   #dangling spins
      row[self.dim + 2*ll : self.dim + 2*ll + self.__nd] = di
      row[-self.__nd:] = dd
      col[self.dim + 2*ll : self.dim + 2*ll + self.__nd] = dd
      col[-self.__nd:] = di
      tmp = [self.Hall(spin,eden,[di[i],dd[i]]) for i in xrange(self.__nd)]
      dat[self.dim + 2*ll : self.dim + 2*ll + self.__nd] = tmp 
      dat[-self.__nd:] = tmp

      return coo_matrix( (dat,(row,col)), shape=(self.dim,self.dim) )

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
      return 1 if(0<=i and i<self.__dim) else 0
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

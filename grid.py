import inspect
from copy import deepcopy
from numpy import *

def whoami():
    return inspect.stack()[1][3]
def whosdaddy():
    return inspect.stack()[2][3]

def myabs(x):
   return x if(x>=0) else -x

erstr="ERROR: Point-index out of range -- FUNCTON: %s.%s called from %s"
funcn="(self.__class__, whoami(), whosdaddy())"

class raw(object):
   def __init__(self,width,length):
      self.__w = int(width if width>0 else -width)
      self.__l = int(length if length>0 else -length)
      #self._n = self.w * self.l
   @property
   def w(self): return self.__w
   @property
   def l(self): return self.__l
   def size(self,dimension=0):
      if(dimension==0):
	return self.w * self.l
      else:
	return [self.w, self.l]
   def inrange(self,p):
      tp = 0
      if(isinstance(p,(list,ndarray))):
	if(isinstance(p[0],(int,float))):
	   tp = 2 if (len(p)==2 and 0<=p[0] and p[0]<self.w and 0<=p[1] and p[1]<self.l) else 0
      elif(isinstance(p, (int,float))):
	tp = 1 if ( 0<=p and p<self.size()) else 0 
      try:
	1/tp
	return tp
      except:
	print erstr % eval(funcn)
	raise
   def pntind(self,p):
      return self(p)
   def __call__(self,p):
      tp = self.inrange(p)
      if(tp==2):
	return int(p[0])*self.l + int(p[1])
      elif(tp==1):
	myp = int(p)
	return [ myp/self.l, myp%self.l ]

hsqrt3 = 0.86602540378443859659

class honeycomb(raw):
   def __init__(self,width=1,length=1,holes=[],ledge=1.0):
      raw.__init__(self,width,length)
      self.__loe = ledge
      if len(holes)==0: self._holes = holes
      else:
	self._holes = map(lambda x: self.pnt(x,'1d'), holes)
   @property
   def loe(self): return self.__loe
   def sublat(self,p):
      p = self.pnt(p,'2d')
      return sum(p)%2
   def line(self,p,q):
      p,q = map(lambda x:self.pnt(x,'2d'),(p,q))
      if(p[0]==q[0]):
	return 1 if(myabs(p[1]-q[1])==1) else 0
      elif(p[1]==q[1]):
	return 1 if( (p[0]-q[0]==1 and self.sublat(p)==1) or (q[0]-p[0]==1 and self.sublat(q)==1) ) else 0
      else:
	return 0
   def holes(self,form='1d'):
      if(form=='2d'):
	return map(self,self._holes)
      else:
	return self._holes
   def neighb(self,p,form='2d'):
      if(self.inrange(p)==1):
	p = self(p)
      nb = []
      if(self.sublat(p)==1 and p[0]-1>=0):      nb.append( [p[0]-1, p[1]] )
      if(p[1]-1>=0):				nb.append( [p[0], p[1]-1] )
      if(p[1]+1<self.l):			nb.append( [p[0], p[1]+1] )
      if(self.sublat(p)==0 and p[0]+1<self.w):  nb.append( [p[0]+1, p[1]] )
      if(form=='2d'):	return nb
      else:		return map(self, nb)
   def dvertex(self,form='2d',relation='line',neighbtype='neighb'):
      ss = 'self.'
      reln = eval(ss+relation)
      fneighb = eval(ss+neighbtype)
      hn = []
      lh = list(set([x for y in self.linedholepairs(reln) for x in y]))
      for h in self._holes:
	hn.extend(fneighb(h,form='1d'))
      hn = list(set(hn))
      for h in lh:
	hn.remove(h)
      if(form=='2d'):
	hn = map(self,hn)
      return hn
   def nholes(self):
      return len(self._holes)
   def ndvertex(self):
      return len(self.dvertex(form='1d'))
   def nvertex(self):
      return self.size() - self.nholes()
   def pnt(self,p,form='2d'):
      tp = self.inrange(p)
      if((form=='2d' and tp==1) or (form=='1d' and tp==2)):
	return self(p)
      elif((form=='2d' and tp==2) or (form=='1d' and tp==1)):
      	return p
      elif(form=='xy'):
	return self.coord(p)
      else:
	return p
   def linkedholepairs(self,relatn):
      hs = deepcopy(self._holes)
      lhp = []		#lined-hole pairs
      while(hs!=[]):
	h1 = hs.pop()
	for h2 in hs:
	   if(relatn(h1,h2)): lhp.append([h1,h2])
      return lhp
   def linedholepairs(self,relation):
      return self.linkedholepairs(relation)
   def nlinedhp(self):
      return len(self.linedholepairs(self.line))
   def nlines(self):
      w = int(self.w); l = int(self.l)
      return w*(l-1) + ((l-1)/2+1)*(w/2) + (w-1)/2*(l/2) - self.ndvertex() + self.nlinedhp()
   def pointpairsinit(self,n,form='2d'):
      if(form=='xy'):	pp = zeros((n,2,2),dtype=float)
      elif(form=='2d'):	pp = zeros((n,2,2),dtype=int)
      else:		pp = zeros((n,2),dtype=int)
      return pp
   def lslines(self,form='2d',outype='array'):
      lines = self.pointpairsinit(self.nlines(),form)
      k = 0
      for i in xrange(self.w):
	for j in xrange(self.l):
	   if(j<self.l-1 and not self([i,j]) in self._holes and not self([i,j+1]) in self._holes):
	      lines[k] = [self.pnt([i,j],form), self.pnt([i,j+1],form)]
	      k += 1
	   if(self.sublat([i,j])==0 and i<self.w-1 and
			 not self([i,j]) in self._holes and not self([i+1,j]) in self._holes):
	      lines[k] = [self.pnt([i,j],form), self.pnt([i+1,j],form)]
	      k += 1
      return lines
   def coord(self,p):
      p = self.pnt(p,'2d')
      s = self.sublat(p)
      x = p[1] * hsqrt3
      y = -p[0]/2.0 * 3.0 + s*0.5
      return array([ x*self.loe, y*self.loe ])

class square(raw):
   def __init__(self,width):
      raw.__init__(self,width,width)

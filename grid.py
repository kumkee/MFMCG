import inspect
from copy import deepcopy
from numpy import *

def whoami():
    return inspect.stack()[1][3]
def whosdaddy():
    return inspect.stack()[2][3]

def myabs(x):
   return x if(x>=0) else -x

erstr="ERROR: Points out of range -- FUNCTON: %s.%s called from %s"

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
      if(isinstance(p,(list,ndarray)) and isinstance(p[0],(int,float))):
	return 2 if (len(p)==2 and 0<=p[0] and p[0]<self.w and 0<=p[1] and p[1]<self.l) else 0
      elif(isinstance(p, (int,float))):
	return 1 if ( 0<=p and p<self.size()) else 0 
      else:
	print erstr % (self.__class__, whoami(), whosdaddy())
	return 0
   def pntind(self,p):
      return self(p)
   def __call__(self,p):
      tp = self.inrange(p)
      if(tp==2):
	return int(p[0])*self.l + int(p[1])
      elif(tp==1):
	myp = int(p)
	return [ myp/self.l, myp%self.l ]
      else:
	print "ERROR: Index(ices) out of range -- FUNCTON: %s.%s called from %s" % (self.__class__, whoami(), whosdaddy())
	quit(2)

hsqrt3 = 0.86602540378443859659

class honeycomb(raw):
   def __init__(self,width=1,length=1,holes=[],ledge=1.0):
      raw.__init__(self,width,length)
      self.__loe = ledge
      if len(holes)==0: self._holes = holes
      else:
	th = self.inrange(holes[0])
	for h in holes:
	   if(self.inrange(h)==0): print erstr % (self.__class__, whoami(), whosdaddy()); quit(2)
	   elif(self.inrange(h)!=th):
	      print "holes type do not match -- FUNCTON: %s.%s called from %s" % (self.__class__, whoami(), whosdaddy()); quit(2)
	if(th==2): self._holes = map(self,holes)
	else: self._holes = holes
   @property
   def loe(self): return self.__loe
   def sublat(self,p):
      tp = self.inrange(p)
      if(tp==1):
	return self.sublat(self(p))
      elif(tp==2):
	return sum(p)%2
      else:
	quit(2)
   def line(self,p,q):
      tp = self.inrange(p)
      tq = self.inrange(q)
      if(tp==tq and tp!=0):
	if(tp==2):
	   if(p[0]==q[0]):
		return 1 if(myabs(p[1]-q[1])==1) else 0
	   elif(p[1]==q[1]):
		return 1 if( (p[0]-q[0]==1 and self.sublat(p)==1) or (q[0]-p[0]==1 and self.sublat(q)==1) ) else 0
	   else:
		return 0
	elif(tp==1):
	   return self.line(self(p),self(q))
      else:
	print erstr % (self.__class__, whoami(), whosdaddy()); quit(2)
   def holes(self,form='1d'):
      if(form=='2d'):
	return map(self,self._holes)
      else:
	return self._holes
   def neighb(self,p,form='2d'):
      #print 'from: ', whosdaddy() ##############
      if(self.inrange(p)==1):
	p = self(p)
      nb = []
      if(self.sublat(p)==1 and p[0]-1>=0):      nb.append( [p[0]-1, p[1]] )
      if(p[1]-1>=0):				  nb.append( [p[0], p[1]-1] )
      if(p[1]+1<self.l):			  nb.append( [p[0], p[1]+1] )
      if(self.sublat(p)==0 and p[0]+1<self.w): nb.append( [p[0]+1, p[1]] )
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
   def _pnt(self,i,j,form='2d'):
      if(form=='2d'):	return [i,j]
      elif(form=='xy'): return self.coord([i,j])
      else:		return self([i,j])
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
	      lines[k] = [self._pnt(i,j,form), self._pnt(i,j+1,form)]
	      k += 1
	   if(self.sublat([i,j])==0 and i<self.w-1 and
			 not self([i,j]) in self._holes and not self([i+1,j]) in self._holes):
	      lines[k] = [self._pnt(i,j,form), self._pnt(i+1,j,form)]
	      k += 1
      return lines
   def coord(self,p):
      tp = self.inrange(p)
      if(tp==1):
	return self.coord(self(p))
      elif(tp==2):
	s = self.sublat(p)
	x = p[1] * hsqrt3
	y = -p[0]/2.0 * 3.0 + s*0.5
	return array([ x*self.loe, y*self.loe ])
      else:
	print erstr % (self.__class__, whoami(), whosdaddy()); quit(2)

class square(raw):
   def __init__(self,width):
      raw.__init__(self,width,width)

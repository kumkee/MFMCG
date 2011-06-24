import inspect
from numpy import *
def whoami():
    return inspect.stack()[1][3]
def whosdaddy():
    return inspect.stack()[2][3]

def myabs(x):
   return x if(x>=0) else -x

class raw:
   def __init__(self,width,length):
      self._w = int(width if width>0 else -width)
      self._l = int(length if length>0 else -length)
      self._n = self._w * self._l
   def size(self,dimension=0):
      if(dimension==0):
	return self._n
      else:
	return [self._w, self._l]
   def inrange(self,p):
      if(isinstance(p,(list,ndarray)) and isinstance(p[0],(int,float))):
	return 2 if (len(p)==2 and 0<=p[0] and p[0]<self._w and 0<=p[1] and p[1]<self._l) else 0
      elif(isinstance(p, (int,float))):
	return 1 if ( 0<=p and p<self._n) else 0 
      else:
	return 0
   def pntind(self,p):
      return self(p)
   def __call__(self,p):
      tp = self.inrange(p)
      if(tp==2):
	return int(p[0])*self._l + int(p[1])
      elif(tp==1):
	myp = int(p)
	return array([ myp/self._l, myp%self._l ])
      else:
	print "ERROR: Index(ices) out of range -- FUNCTON: %s.%s called from %s" % (self.__class__, whoami(), whosdaddy())
	quit(2)

hsqrt3 = 0.86602540378443859659

class honeycomb(raw):
   erstr="ERROR: Points out of range -- FUNCTON: %s.%s called from %s"
   def __init__(self,width=1,length=1,ledge=1):
      raw.__init__(self,width,length)
      self._loe = ledge
   def sublat(self,p):
      tp = self.inrange(p)
      if(tp==1):
	return self.sublat(self(p))
      elif(tp==2):
	return sum(p)%2
      else:
	print erstr % (self.__class__, whoami(), whosdaddy())
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
   '''def fwdneighb(self,p,form='2d'):
      tp = self.inrange(p)
      if(tp==2):
	nb = []
	if(p[1]+1<self._l):			  nb.append( [p[0], p[1]+1] )
	if(self.sublat(p)==0 and p[0]+1<self._w): nb.append( [p[0]+1, p[1]] )
	if(form=='2d'):	return nb
	else:		return map(self, nb)
      elif(tp==1):
	return self.fwdneighb(self(p),form)
      else:
	print erstr % (self.__class__, whoami(), whosdaddy()); quit(2)'''
   def neighb(self,p,form='2d'):
      tp = self.inrange(p)
      if(tp==2):
	#nb = self.fwdneighb(p)
	nb = []
	if(self.sublat(p)==1 and p[0]-1>=0):      nb.append( [p[0]-1, p[1]] )
	if(p[1]-1>=0):				  nb.append( [p[0], p[1]-1] )
	if(p[1]+1<self._l):			  nb.append( [p[0], p[1]+1] )
	if(self.sublat(p)==0 and p[0]+1<self._w): nb.append( [p[0]+1, p[1]] )
	if(form=='2d'):	return nb
	else:		return map(self, nb)
      elif(tp==1):
	return self.neighb(self(p),form)
      else:
	print erstr % (self.__class__, whoami(), whosdaddy()); quit(2)
   def _pnt(self,i,j,form='2d'):
      if(form=='2d'): return [i,j]
      else:	      return self([i,j])
   def lslinks(self,form='2d',outype='array'):
      links = []
      for i in xrange(self._w):
	for j in xrange(self._l):
	   if(j<self._l-1): links.append( [self._pnt(i,j,form), self._pnt(i,j+1,form)] )
	   if(self.sublat([i,j])==0 and i<self._w-1): links.append( [self._pnt(i,j,form), self._pnt(i+1,j,form)] )
      if(outype=='array'): return array(links)
      else:		   return links
   def coord(self,p):
      tp = self.inrange(p)
      if(tp==1):
	return self.coord(self(p))
      elif(tp==2):
	s = self.sublat(p)
	x = p[1] * hsqrt3
	y = -p[0]/2.0 * 3.0 + s*0.5
	return array([ x*self._loe, y*self._loe ])
      else:
	print erstr % (self.__class__, whoami(), whosdaddy()); quit(2)
   def test(self):
      print "honeycomb Test.", self._l

class square(raw):
   def __init__(self,width):
      raw.__init__(self,width,width)

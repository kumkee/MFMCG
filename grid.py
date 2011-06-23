import inspect
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
      if(type(p) is list):
	return 2 if (len(p)==2 and 0<=p[0] and p[0]<self._w and 0<=p[1] and p[1]<self._l) else 0
      else:
	return 1 if ( isinstance(p, (int,float)) and 0<=p and p<self._n) else 0
   def pntind(self,p):
      tp = self.inrange(p)
      if(tp==2):
	return int(p[0])*self._l + int(p[1])
      elif(tp==1):
	myp = int(p)
	return [ myp/self._l, myp%self._l ]
      else:
	print "ERROR: Index(ices) out of range -- FUNCTON: %s.%s" % (self.__class__, whoami())
	quit(2)

hsqrt3 = 0.86602540378443859659

class honeycomb(raw):
   erstr="ERROR: Points out of range -- FUNCTON: %s.%s"
   def __init__(self,width=1,length=1,ledge=1):
      raw.__init__(self,width,length)
      self._loe = ledge
   def sublat(self,p):
      tp = self.inrange(p)
      if(tp==1):
	return self.sublat(self.pntind(p))
      elif(tp==2):
	return sum(p)%2
      else:
	print erstr % (self.__class__, whoami())
	quit(2)
   def line(self,p,q):
      tp = self.inrange(p)
      tq = self.inrange(q)
      if(tp==tq and tp):
	if(tp==2):
	   if(p[0]==q[0]):
		return 1 if(myabs(p[1]-q[1])==1) else 0
	   elif(p[1]==q[1]):
		return 1 if( (p[0]-q[0]==1 and self.sublat(p)==1) or (q[0]-p[0]==1 and self.sublat(q)==1) ) else 0
	   else:
		return 0
	elif(tp==1):
	   return self.line(self.pntind(p),self.pntind(q))
      else:
	print erstr % (self.__class__, whoami()); quit(2)
   def coord(self,p):
      tp = self.inrange(p)
      if(tp==1):
	return self.coord(self.pntind(p))
      elif(tp==2):
	s = self.sublat(p)
	x = p[1] * hsqrt3
	y = -p[0]/2.0 * 3.0 + s*0.5
	return [ x*self._loe, y*self._loe ]
      else:
	print erstr % (self.__class__, whoami()); quit(2)
   def test(self):
      print "honeycomb Test.", self._l

class square(raw):
   def __init__(self,width):
      raw.__init__(self,width,width)

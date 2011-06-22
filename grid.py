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
	return 1 if ((type(p) is int or type(p) is float) and 0<=p and p<self._n) else 0
   def pointindex(self,p):
      tp = self.inrange(p)
      if(tp==2):
	return int(p[0])*self._l + int(p[1])
      elif(tp==1):
	myp = int(p)
	return [ myp/self._l, myp%self._l ]
      else:
	print "ERROR: Index(ices) out of range -- FUNCTON: %s.%s" % (self.__class__, whoami())
	quit(2)

sqrt3 = 1.732050807568877293527

class honeycomb(raw):
   def line(self,p,q):
      erstr='print "ERROR: Points out of range -- FUNCTON: %s.%s" % (self.__class__, whoami())'
      tp = self.inrange(p)
      tq = self.inrange(q)
      if(tp==tq and tp):
	if(tp==2):
	   if(p[0]==q[0]):
		return 1 if(myabs(p[1]-q[1])==1) else 0
	   elif(p[1]==q[1]):
		return 1 if( (p[0]-q[0]==1 and (p[0]+p[1])%2==1) or (q[0]-p[0]==1 and (q[0]+q[1])%2==1) ) else 0
	   else:
		return 0
	elif(tp==1):
	   return self.line(self.pointindex(p),self.pointindex(q))
      else:
	print "ERROR: Points out of range -- FUNCTON: %s.%s" % (self.__class__, whoami())
	quit(2)
   def test(self):
      print "honeycomb Test.", self._l

class square(raw):
   def __init__(self,width):
      raw.__init__(self,width,width)

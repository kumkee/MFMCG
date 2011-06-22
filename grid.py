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
   '''def pointtest(self,p):
      if(type(p) is list):
	if(len(p)==2):
	   return 2
	else:
	   return 0
      elif(type(p) is int or type(p) is float):
	return 1
      else:
	return 0'''
   def position(self,p):
      tp = self.inrange(p)
      if(tp==2):
	return int(p[0])*self._l + int(p[1])
      elif(tp==1):
	myp = int(p)
	return [ myp/self._l, myp%self._l ]
      else:
	print "ERROR: Coordinates out of range -- CLASS:", self.__class__
	quit(2)
   '''def position(self,r,c):
      if(self.inrange([r,c])):
	myr = int(r)
	myc = int(c)
	return myr*self._l + myc
      else:
	print "ERROR: Coordinates out of range -- CLASS:", self.__class__
	quit(2)
   def coor(self,p):
      if(self.inrange(p)):
	myp = int(p)
	return [ myp/self._l, myp%self._l ]
      else:
	print "ERROR: Position out of range -- CLASS:", self.__class__
	quit(2)'''

sqrt3 = 1.732050807568877293527

class honeycomb(raw):
   def test(self):
      print "honeycomb Test.", self._l

class square(raw):
   def __init__(self,width):
      raw.__init__(self,width,width)

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
   def inrange2d(self,r,c):
      return (0<=r and r<self._w and 0<=c and c<self._l)
   def inrange1d(self,p):
      return (0<=p and p<self._n)
   def position(self,r,c):
      if(self.inrange2d(r,c)):
	myr = int(r)
	myc = int(c)
	return myr*self._l + myc
      else:
	print "ERROR: Coordinates out of range -- CLASS:", self.__class__
	quit(2)
   def coor(self,p):
      if(self.inrange1d(p)):
	myp = int(p)
	return [ myp/self._l, myp%self._l ]
      else:
	print "ERROR: Position out of range -- CLASS:", self.__class__
	quit(2)

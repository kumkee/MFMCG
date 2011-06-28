from numpy import *
from grid import *

#erstr="ERROR: Points out of range -- FUNCTON: %s.%s called from %s"

class graphene(honeycomb):
   def __init__(self,width=2,length=3,boundary="open",holes=[],ledge=1.0):
      if(boundary=="open" or boundary=="o"):
	w = width/2 * 2
	l = length/2 * 2 +1
	self._pbc = 0
      elif(boundary=="zigzag" or boundary=="z"):
	l = length/2 * 2
	self._pbc = 2
      elif(boundary=="armchair" or boundary=="a"):
	w = width/2 * 2
	self._pbc = 1
      honeycomb.__init__(self,width,length,ledge)
      if len(holes)==0: self._holes = holes
      else:
	th = self.inrange(holes[0])
	for h in holes:
	   if(self.inrange(h)==0): print erstr % (self.__class__, whoami(), whosdaddy()); quit(2)
	   elif(self.inrange(h)!=th):
	      print "holes type do not match -- FUNCTON: %s.%s called from %s" % (self.__class__, whoami(), whosdaddy()); quit(2)
	if(th==2): self._holes = map(self,holes)
	else: self._holes = holes
      self.dispm = zeros( (self.nCatoms(),2) )
   def nCatoms(self):
      return self.size() - len(self._holes)

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
      honeycomb.__init__(self,width,length,holes,ledge)
      self.dispm = zeros( (self.nvertex(),2) )

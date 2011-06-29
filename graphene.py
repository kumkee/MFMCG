from numpy import *
from grid import *

#erstr="ERROR: Points out of range -- FUNCTON: %s.%s called from %s"

class graphene(honeycomb):
   def __init__(self,width=2,length=3,boundary="open",holes=[],ledge=1.0):
      w = width; l = length
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
      honeycomb.__init__(self,w,l,holes,ledge)
      self.dispm = zeros( (self.size(),2) )
   def ptype1(self,p):
      if(self.inrange(p)==1):
	p = self(p)
      zf = ((p[0]==0 or p[0]==self._w-1) and p[1]%2==1)
      af = (p[1]==0 or p[1]==self._l-1)
      if(zf):	return 2 #zigzag edges
      elif(af):	return 1 #armchair edges
      else:	return 0
   def ptype0(self,p):
      if(self.inrange(p)==2):
	p = self(p)
      if(p in self._holes):		 return 0 #holes
      elif(p in self.dvertex(form='1d')):return 1 #dangling
      else:				 return 2
   def brokenedges(self,etype=2):
      h = array(self._holes)
      f = map(lambda p:self.ptype1(p)==etype, h)
      return list(h[f])
   def nbrokenedges(self,etype=2):
      return len(self.brokenedges(etype))
   def link(self,p,q):
     if(self.line(p,q)):
	return 1 
     else:
	tp = self.inrange(p)
	if(tp==1):
	   p = self(p)
	   q = self(q)
	if(self._pbc==1):
	   if( p[1]==q[1] and p[1]%2==1 and ([p[0],q[0]]==[0,self._w-1] or [q[0],p[0]]==[0,self._w-1]) ):
	      return 1
	   else:
	      return 0
	elif(self._pbc==2):
	   if( p[0]==q[0] and ([p[1],q[1]]==[0,self._l-1] or [q[1],p[1]]==[0,self._l-1]) ):
	      return 1
	   else:
	      return 0
	else:
	   return 0
   def lspblinks(self,form='2d'):
      if(self._pbc==2):
	links = self.pointpairsinit(self._w-self.nbrokenedges(2),form)
	print "links init:", links ##################
	be = self.brokenedges(2)
	j = 0
	for i in xrange(self._w):
	   if  not self([i,0]) in be and not self([i,self._l-1]) in be:
	      links[j] = [self._pnt(i,0,form), self._pnt(i,self._l-1,form)]
	      j += 1
	return links
      elif(self._pbc==1):
	links = self.pointpairsinit(self._l/2-self.nbrokenedges(1),form)
	be = self.brokenedges(1)
	j = 0 
	for i in xrange(self._l/2):
	   if  not self([0,2*i+1]) in be and not self([self._w-1,2*i+1]) in be:
	      links[j] = [self._pnt(0,2*i+1,form), self._pnt(self._w-1,2*i+1,form)]
	      j += 1
	return links
      else: return []
   def lslinks(self,form='1d'):
      return vstack((self.lslines(form),self.lspblinks(form)))
   def displace(self,p,d):
      tp = self.inrange(p)
      if(tp==0):
	print erstr % (self.__class__, whoami(), whosdaddy()); quit(2)
      elif(tp==2):
	p = self(p)
      ch = 0 if p in self._holes else 1
      self.dispm[p] += array(d)*self._loe*ch
		


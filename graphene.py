from numpy import *
from grid import *

#erstr="ERROR: Points out of range -- FUNCTON: %s.%s called from %s"

class graphene(honeycomb):
   def __init__(self,width=2,length=3,boundary="open",holes=[],ledge=1.0):
      w = width; l = length
      if(boundary=="open" or boundary=="o"):
	w = width/2 * 2
	l = length/2 * 2 +1
	self.__pbc = 0
      elif(boundary=="zigzag" or boundary=="z"):
	l = length/2 * 2
	self.__pbc = 2
      elif(boundary=="armchair" or boundary=="a"):
	w = width/2 * 2
	self.__pbc = 1
      elif(boundary=="periodic" or boundary=="p"):
	w = width/2 * 2
	l = length/2 * 2
	self.__pbc = 3
      else:
	self.__pbc = 0
      honeycomb.__init__(self,w,l,holes,ledge)
      self.dispm = zeros( (self.size(),2) )
   @property
   def pbc(self):
      return self.__pbc
   def ptype1(self,p):
      if(self.inrange(p)==1):
	p = self(p)
      zf = ((p[0]==0 or p[0]==self.w-1) and p[1]%2==1)
      af = (p[1]==0 or p[1]==self.l-1)
      if(zf and af): return 3 #both kinds
      elif(zf):	return 2 #zigzag edges
      elif(af):	return 1 #armchair edges
      else:	return 0
   def ptype0(self,p):
      if(self.inrange(p)==2):
	p = self(p)
      if(p in self._holes):		 return 0 #holes
      elif(p in self.dvertex(form='1d')):return 1 #dangling
      else:				 return 2
   def brokenedges(self,etype=2):
      #print 'etype =', etype, whoami(), whosdaddy() ###############
      h = array(self._holes)
      f = array(map(lambda p:self.ptype1(p)==etype or self.ptype1(p)==3, h))
      return list(h[f])
   def nbrokenedges(self,etype=2):
      return len(self.brokenedges(etype))
   def edgelink(self,p,q):
      tp = self.inrange(p)
      if(tp==1):
	p = self(p)
	q = self(q)
      Zl = ( p[1]==q[1] and p[1]%2==1 and ([p[0],q[0]]==[0,self.w-1] or [q[0],p[0]]==[0,self.w-1]) )
      Al = ( p[0]==q[0] and ([p[1],q[1]]==[0,self.l-1] or [q[1],p[1]]==[0,self.l-1]) )
      if(self.pbc==1):
	return 1 if Zl else 0
      elif(self.pbc==2):
	return 1 if Al else 0
      elif(self.pbc==3):
	return 1 if (Zl or Al) else 0
      else:
	return 0
   def link(self,p,q):
     if(self.edgelink(p,q)):
	return 1 
     else:
	return self.line(p,q)
   def linkedbrokenedges(self):
      return self.linkedholepairs(self.edgelink)
   def pbneighb(self,p,form='2d'): #periodic boundary neighbor
      if(self.inrange(p)==1):
	p = self(p)
      pbn = []
      #af = (p[1]==0 or p[1]==self.l-1)
      if(self.pbc==2 or self.pbc==3):
	if(p[1]==0):
	   pbn.append([p[0],self.l-1])
	elif(p[1]==self.l-1):
	   pbn.append([p[0],0])
      #zf = ((p[0]==0 or p[0]==self.w-1) and p[1]%2==1)
      if(self.pbc==1 or self.pbc==3):
	if(p[0]==0 and p[1]%2==1):
	   pbn.append([self.w-1,p[1]])
	elif(p[0]==self.w-1 and p[1]%2==1):
	   pbn.append([0,p[1]])
      pbn.extend(self.neighb(p,form='2d'))
      if(form=='2d'):	return pbn
      else:		return map(self,pbn)
   def danglingc(self,form='2d'):
      return self.dvertex(form,relation='link',neighbtype='pbneighb')
   def lspblinks(self,form='2d'):
      def alinks():
	be = self.brokenedges(1)
	bel = self.linkedbrokenedges()
	links = self.pointpairsinit(self.w-len(bel),form)
	j = 0
	for i in xrange(self.w):
	   if  not self([i,0]) in be and not self([i,self.l-1]) in be:
	      links[j] = [self._pnt(i,0,form), self._pnt(i,self.l-1,form)]
	      j += 1
	return links
      def zlinks():
	be = self.brokenedges(2)
	bel = self.linkedbrokenedges()
	links = self.pointpairsinit(self.l/2-len(bel),form)
	j = 0 
	for i in xrange(self.l/2):
	   if  not self([0,2*i+1]) in be and not self([self.w-1,2*i+1]) in be:
	      links[j] = [self._pnt(0,2*i+1,form), self._pnt(self.w-1,2*i+1,form)]
	      j += 1
	return links
      if(self.pbc==2):
	return alinks()
      elif(self.pbc==1):
	return zlinks()
      elif(self.pbc==3):
	return vstack([alinks(),zlinks()])
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
      self.dispm[p] += array(d)*self.loe*ch
		


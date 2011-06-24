import pylab
from numpy import *

def jtwop(p1,p2,sty='g-'):
   try:
      X = [p1.item(0),p2.item(0)]
      Y = [p1.item(1),p2.item(1)]
      pylab.plot(X, Y, sty)
   except:
      print "error: jtwop(p1,p1): p1 and/or p1 are not 2D points."

def savefig(output='sample.eps'):
   pylab.xticks([])
   pylab.yticks([])
   pylab.axis('scaled')
   pylab.savefig(output)

def jmultp(ppairs,sty='g-',output=None):
   for pp in ppairs:
      jtwop(pp[0],pp[1],sty)
   if output != None:
      savefig(output)

def drawhoneycomb(honeycomb,sty='g-',output=None):
   pp = honeycomb.lslinks()
   '''	array([ array([honeycomb.coord(x), honeycomb.coord(y)]) for x in xrange(honeycomb.size())  
			for y in xrange(honeycomb.size()) if honeycomb.line(x,y) and x<=y ])
		# this 2D iteration is very time-consuming '''
   jmultp(pp,sty,output)

import pylab

def jtwop(p1,p2,sty='g-'):
   try:
      X = [p1[0],p2[0]]
      Y = [p1[1],p2[1]]
      pylab.plot(X, Y, sty)
   except:
      print "error: jtwop(p1,p1): p1 and/or p1 are not 2D points."

def jmultp(ppairs,sty='g-',output='sample.eps'):
   for pp in ppairs:
      jtwop(pp[0],pp[1],sty)
   pylab.axis('scaled')
   pylab.savefig(output)

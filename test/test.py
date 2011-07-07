#!/usr/bin/env python
import grid
import platform

print platform.python_version()
a = grid.honeycomb(4,5)
print a.size(1)
print a.pntind([3,4])
print a.pntind(a.size()-1)
print a.__class__
b = grid.square(3.5)
print b.size(1)
a.test()
p = [ [x,y] for x in range(a.size()) for y in range(a.size()) if(a.line(x,y) and x<=y) ]
print p
print "-----------"
p = [ [a.pntind(x),a.pntind(y)] for x in range(a.size()) for y in range(a.size()) if(a.line(x,y) and x<=y) ]
#print p
print "-----------"
q = [ a.pntind(x) for x in range(a.size()) ]
z = [ [a.pntind(x),a.coord(x)] for x in range(a.size()) ]
print z
print "-----------"
print p
print "-----------"
#print b.pntind([3,3])
ppset = [ [a.coord(pp[0]), a.coord(pp[1])] for pp in p ]
import drawing
drawing.jmultp(ppset,sty='g--')
c = grid.honeycomb(20,41,ledge=0.9)
drawing.drawhoneycomb(c,sty='b-')
drawing.savefig('test.eps')

#!/usr/bin/env python
import grid
import platform

print platform.python_version()
a = grid.honeycomb(4,5)
print a.size(1)
print a.pointindex([3,4])
print a.pointindex(a.size()-1)
print a.__class__
b = grid.square(3.5)
print b.size(1)
a.test()
print a.line([1,1],[3,4])
print a.line([0,0],[1,0])
print a.line([0,1],[1,0])
print a.line([0,1],[1,1])
print a.line([1,1],[2,1])
print a.line([1,2],[2,2])
#print b.pointindex([3,3])

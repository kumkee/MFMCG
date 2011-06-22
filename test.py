#!/usr/bin/env python
import grid
import platform

print platform.python_version()
a = grid.honeycomb(4,5)
print a.size(1)
print a.position([3,4])
print a.position(a.size()-1)
print a.__class__
b = grid.square(3.5)
print b.size(1)
a.test()
print b.position([3,3])

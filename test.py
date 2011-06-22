#!/usr/bin/env python
import grid
import platform
print platform.python_version()
a = grid.raw(4,5)
print a.size(1)
print a.position(3,4)
print a.coor(a.size()-1)

from graphene import graphene
a = graphene(width=4,length=5,boundary='z',holes=[8])
print a.dvertex()
print a.nlines()
print a.size(1)
b = a.lslines()
print len(b)
print a.brokenedges(2)
from drawing import *
drawhoneycomb(a,output="h.eps")
drawgraphene(a,output="g.eps")

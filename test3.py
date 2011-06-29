from graphene import graphene
a = graphene(width=4,length=7,ledge=1.42,boundary='o',holes=[9,10])
print "holes:",a.holes('2d')
print "lined hole-pairs:", a.linedholepairs()
print "dvertex:",a.dvertex('2d')
print a.nlines()
print a.size(1)
b = a.lslines()
print len(b)
print a.brokenedges(2)
from drawing import *
#drawhoneycomb(a,output="h.eps")
drawgraphene(a,output="g.eps")

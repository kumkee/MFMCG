from graphene import graphene
a = graphene(width=4,length=7,ledge=1.42,boundary='z',holes=[[0,0],[0,5]])
print "holes:",a.holes('2d')
print "lined hole-pairs:", a.linedholepairs()
print "dvertex:",a.dvertex('2d')
print "ndvertex:",a.ndvertex()
print a.nlines()
print a.size(1)
b = a.lslines()
print len(b)
from drawing import *
drawhoneycomb(a,output="h.eps")
drawgraphene(a,output="g.eps")

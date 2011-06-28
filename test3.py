from graphene import graphene
a = graphene(width=4,length=5,holes=[[1,2]])
print a.dvertex()
print a.nlines()
b = a.lslines()
print len(b)
from drawing import drawhoneycomb
drawhoneycomb(a,output="g.eps")

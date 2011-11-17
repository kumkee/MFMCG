from os import listdir
from graphene import graphene
from datrendering import *

T = 0.1
g = graphene(width=4,length=5,boundary='o',holes=[11])

ddir = 'data/' + datname(T,g)

fl = listdir(ddir)
fl.sort()
dd = drender(ddir,fl)
i, d, n, en, a = dd.next()
totspin = sum(n[0]-n[1])/2.
print totspin
print en

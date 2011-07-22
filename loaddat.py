from os import listdir
from graphene import graphene
from datrendering import *

T = 1.
g = graphene(width=4,length=4,boundary='z')

ddir = 'data/' + datname(T,g)

fl = listdir(ddir)
fl.sort()
dd = drender(ddir,fl)
i, d, n, en, a = dd.next()

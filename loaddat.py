from os import listdir
from graphene import graphene
from datrendering import *

T = 1.
g = graphene(width=10,length=21,boundary='o',holes=[115])

ddir = 'data/' + datname(T,g)

fl = listdir(ddir)
fl.sort()
dd = drender(ddir,fl)
for tmp in dd:
   if(tmp[0]==0):
      i, d, n, en, a = tmp
   else:
      i = tmp[0]
      d += tmp[1]
      n += tmp[2]
      en += tmp[3]
      a += tmp[4]

c = i + 1.0

d /= c
n /= c
en /= c
a /= c
totspin = sum(n[0]-n[1])/2.
print totspin
print en

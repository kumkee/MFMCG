from graphene import graphene
from drawing import *
from edensity import *
#import graphene
#import drawing
#import pp
a = graphene(width=15,length=30,boundary='z',holes=[[7,12]])
print "size:",a.size(1)
print "holes:",a.holes('2d')
#print "lined hole-pairs:", a.linedholepairs(a.line)
print "dvertex:",a.dvertex('2d')
print "danglingc:",a.danglingc('2d')
print "ndvertex:",a.ndvertex()
print "pbn of hole:",a.pbneighb([0,5])
print "nlines:",a.nlines()
b = a.lslines()
print "len(lslines()):",len(b)
#drawhoneycomb(a,output="h.eps")
#drawgraphene(a,output="g.eps")
'''ppservers=()
ncpus=6
job_server = pp.Server(ncpus,ppservers=ppservers)
job = job_server.submit(drawhoneycomb,(a,'g-','a.eps'),(jmultp,jtwop,savefig),("graphene","drawing","pylab","numpy"))
print job()
job_server.print_stats()'''
a._displace(0,[0.1,0.1])
from hamiltonian import ham
print "h = ham(graphene=a)"
h = ham(graphene=a)
print "h.g.size(1)",h.g.size(1)
print "h.osc",h.osc
print "h.tij(0,1)",h.tij([0,1])
hh = h.g.holes()[0]
print "h.g.hole", hh
hn = h.g.neighb(hh,'1d')[0]
print "link(hn,hh):", h.g.link(hn,hh)
print "tij(hn,hh):", h.tij([hn,hh])
print "h.tij(0,1)",h.tij([0,1])
print "h.osc",h.osc
print "h.displace(0,[0.1,0.1])"
h.displace(0,[0.1,0.1])
print "h.tij(0,1)",h.tij([0,1])
print "h.osc",h.osc
print "osc", h.oscp([0,0])
c = eden(h)
print "c = eden(h)"

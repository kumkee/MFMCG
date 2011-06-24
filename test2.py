import grid
a = grid.honeycomb(4,5)
b = a.lslinks(form='1d')
print b
print b.shape
print a.neighb(12,form='1d')
c = a.lslinks(form='1d', outype='list')
print c


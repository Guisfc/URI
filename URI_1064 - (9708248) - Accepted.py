# -*- coding: utf-8 -*-

media = 0
cont = 0
for x in xrange(0,6,1):
    entrada = input()
    if (entrada > 0):
        media += entrada
        cont+=1; 

print '%d valores positivos' % (cont)
print '%.1f' % (media/cont)

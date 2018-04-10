#!/usr/bin/python

def count(wires):
    nb = 0
    for i in range(0, len(wires)-1):
        for j in range(i+1, len(wires)-1):
            if (wires(i).r < wires(j).r and wires(i).l > wires(j).l) or \
               (wires(i).r > wires(j).r and wires(i).l < wires(j).l):
               nb+=1
    return nb

testsNb = int(input())
for test in range(0, testsNb):
    wiresNb = int(input())
    wires = []
    for i in range(0, wiresNb):
        wires.append({'r': int(input()), 'l': int(input())})
        print "Case #" + str(test) + ":" + str(count(wires))

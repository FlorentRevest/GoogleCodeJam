#!/usr/bin/python3

testsNb = int(input()) # Get input
for test in range(1, testsNb+1):
    string = input()
    nb = []
    z = string.count("Z")
    o = string.count("O")
    w = string.count("W")
    u = string.count("U")
    h = string.count("H")
    f = string.count("F")
    g = string.count("G")
    v = string.count("V")
    s = string.count("S")
    x = string.count("X")
    n = string.count("N")
    i = string.count("I")
    nb.append(z*"0")
    nb.append((o-(z+w+u))*"1")
    nb.append(w*"2")
    nb.append((h-g)*"3")
    nb.append(u*"4")
    nb.append((f-u)*"5")
    nb.append(x*"6")
    nb.append((s-x)*"7")
    nb.append(g*"8")
    nb.append((i-(x+(f-u)+g))*"9")

    print("Case #" + str(test) + ": " + str("".join(nb)))

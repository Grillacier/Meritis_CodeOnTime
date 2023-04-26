def digicode():
    "trouve le digicode selon les spécifications"
    with open("data") as f:
        l = [f.readline(), f.readline(), f.readline(), f.readline(), ""]
        for ligne in f:
            l[4] = ligne
            if len(l[3]) == 7 and int(l[3]) % 14 == 0 and '4' in l[4] and '3' not in l[0]\
                    and '3' not in l[1] and '3' not in l[2]:
                return l[3]
            l[0] = l[1]
            l[1] = l[2]
            l[2] = l[3]
            l[3] = l[4]
    return l[3]
print(digicode())
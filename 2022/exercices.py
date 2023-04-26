#!/usr/bin/env python3
def switch1() :
    max_add = ""
    max = 0
    with open("aa.txt") as f:
        for ligne in f:
            l = ligne.split(" ")
            if max < int(l[0]):
                max = int(l[0])
                max_add = " ".join(l[1:])
    return max_add


def switch2():
    max_add = ""
    max = 0

    with open("aa.txt") as f:
        l = [f.readline(), f.readline(), f.readline(), f.readline(), ""]
        for ligne in f:
            l[4] = ligne
            if len(l[3])==7 and int(l[3]) % 14==0 and '4' in l[4] and '3' not in l[0] and '3' not in l[1] and '3' not in l[2]:
                return l[3]
            l[0] = l[1]
            l[1] = l[2]
            l[2] = l[3]
            l[3] = l[4]
    return  l[3]


def switch3() :
    l = []
    min = 0
    with open("aa.txt") as f:
        min = int(f.readline())
        l.append(min)
        for ligne in f:
            l.append(int(ligne))
            if min > int(ligne):
                min = int(ligne)
    length = len(l)
    print("ok\n")
    for i in range(length) :
        if l[i]+2*min>987654321:
            print("bite " + str(l[i]))
            continue
        for j in range(length):
            if l[i] + l[j] + min > 987654321:
                print("verge")
                continue
            for k in range(length):
                print("penis " + str(i) + " "+ str(j)+ " "+ str(k))
                if(l[i] + l[j] + l[k]==987654321):
                    print(l[i])
                    print(l[j])
                    print(l[k])
                    return (l[i], l[j], l[k])
    return 0

def password():
    "ouvre un fichier et trouve le mot de passe"
    with open("data") as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]
    for a in content:
        for b in content:
            for c in content:
                print(a, b, c)
                if a+b+c == 987654321:
                    print(a, b, c)
                    return a*b*c % 987654321
    return None

print(switch3())

class Transport(Graph) :
    def __init__(self, stops, timetable):
        timetable = json.load(open("aa.txt", "rb"))
        self._edges = dict()
        for e in timetable.keys() :
            a = e.split(" ")
            for i in range(len(a)-1):
                self.add_edge(a[0], a[i+1], timetable[e])

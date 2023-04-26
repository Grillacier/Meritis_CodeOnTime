#!/usr/bin/env python3
import json
from collections import OrderedDict
import random
import math

# Les données ont été dissimulées sur le réseau.
# Notre intrusion risque d'être remarquée.
# Récupère le plus de fichiers avant d'être repéré.
# Il te reste 1h (3600s) avant que nous soyons détectés.
# Tu peux naviguer de serveur en serveur et de là, récupérer les fichiers présents dessus.
# Tous les 10 fichiers transférés, tu te déconnectes pour rester discret et repars du serveur d'origine.
# Te connecter d'un serveur à l'autre te prend quelques secondes, le transfert est immédiat.
# En entrée : 2499 lignes décrivant les fichiers présents sur chaque serveur.
# Sur chaque ligne, un nombre : l'id du serveur, puis séparés par des espaces les ids des fichiers.
# Ensuite 20000 lignes décrivant les liens entre les serveurs.
# Les liens fonctionnent dans les deux sens.
# Sur chaque ligne, l'identité des deux serveurs et le temps en secondes de connexion séparés par des espaces.
# Le résultat attendu : une suite de nombres séparés par des espaces, correspondant à tes actions.
#     si le nombre correspond à un id de serveur, tu te connectes vers ce serveur (il doit exister un lien entre ta position et ce serveur).
#     si le nombre correspond à un id de fichier, tu récupères ce fichier (il doit être présent à ta position) (s'il a déjà été récupéré, l'instruction est ignorée).
#     si c'est 0, tu te déconnectes et te reconnectes sur le serveur d'origine avec l'id 0, cela remet à 0 également le compteur des 10 fichiers avant reconnexion.
# Toute action illicite entraine une déconnexion/reconnexion
# 1 point par fichier unique récupéré ! Un fichier peut exister sur plusieurs serveurs, mais ne peut être récupéré qu'une fois.
# Exemple :
# 1453 10160 116 10112
#   On se connecte sur le serveur 1453 où l'on télécharge le fichier 10160, puis on se connecte deouis le 1453 vers le 116, et l'on y récupère le fichier 10112
def recup(data):
    # On récupère les serveurs
    servers = {}
    for line in data:
        line = line.split()
        servers[int(line[0])] = line[1:]
    # On récupère les liens
    links = {}
    for line in data[2499:]:
        line = line.split()
        links[(int(line[0]), int(line[1]))] = int(line[2])
    # On récupère les fichiers
    files = {}
    for line in data[:2499]:
        line = line.split()
        files[int(line[0])] = line[1:]
    # On récupère les connexions
    connexions = {}
    for line in data[2499+20000:]:
        line = line.split()
        connexions[(int(line[0]), int(line[1]))] = int(line[2])
    # On récupère les actions
    actions = []
    for line in data[2499+20000+20000:]:
        actions.append(int(line))
    #return servers, links, files, connexions, actions
    return actions





class Graph:
    def __init__(self):
        self._edges = dict()

    def __len__(self):
        """Allow to call len() on Graph instances"""
        return len(self._edges)

    def __iter__(self):
        """Allow to iterate over vertex using: for node in graph: ..."""
        return iter(self._edges.keys())

    def __getitem__(self, node):
        """Allow to retrieve edges for a given node using []"""
        return self._edges[node]

    def add_node(self, node):
        if node not in self._edges:
            self._edges[node] = []

    def add_edge(self, src, dst, weight=None):
        self.add_node(src)
        self.add_node(dst)
        self[src].append((dst, weight))

    def actu_node(self, src, dst, weight):
        for i in range(len(self[src])):
            if self[src][i][0] == dst:
                self[src][i] = (self[src][i][0], self[src][i][1]+weight)
                break

    def __str__(self):
        """Pretty-printing of the graph to string"""
        s = ""
        for e in self:
            s += e + " -> " + " " + str(self[e]) + "\n"
        return s

    def bellman_ford(self, start):
        dist = dict()
        pred = dict()

        for n in self:
            dist[n] = math.inf
            pred[n] = None
        dist[start] = 0

        for k in range(0, 2):
            for u in self._edges:
                for (v, w) in self[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
        return dist, pred

    def kruskals_mst(self):
        # Resulting tree
        result = []

        # Iterator
        i = 0
        # Number of edges in MST
        e = 0

        # Sort edges by their weight
        self.m_graph = sorted(self.m_graph, key=lambda item: item[2])

        # Auxiliary arrays
        parent = []
        subtree_sizes = []

        # Initialize `parent` and `subtree_sizes` arrays
        for node in range(self.m_num_of_nodes):
            parent.append(node)
            subtree_sizes.append(0)

        # Important property of MSTs
        # number of egdes in a MST is
        # equal to (m_num_of_nodes - 1)
        while e < (self.m_num_of_nodes - 1):
            # Pick an edge with the minimal weight
            node1, node2, weight = self.m_graph[i]
            i = i + 1

            x = self.find_subtree(parent, node1)
            y = self.find_subtree(parent, node2)

            if x != y:
                e = e + 1
                result.append([node1, node2, weight])
                self.connect_subtrees(parent, subtree_sizes, x, y)


class Transport(Graph) :
    def __init__(self):
        self._edges = dict()
        with open("liens.txt") as f:
            for ligne in f:
                l = ligne.strip("\n").split(" ")
                self.add_edge(int(l[0]), int(l[1]), int(l[2]))
                self.add_edge(int(l[1]), int(l[0]), int(l[2]))

    def path_to_string(self, t, pred):
        s = str(t)
        while pred[t] is not None:
            t = pred[t]
            s = str(t) + " " +s
        return s
    def itinerary(self, s_start, s_dest):
        (dist, paths) = self.bellman_ford(s_start)

        return (dist, paths)
        #return (dist[s_dest],self.path_to_string(s_dest, paths))
def todict():
    d = dict()
    with open("fichiers.txt") as f:
        for ligne in f:
            l = ligne.strip("\n").split(" ")
            d[int(l[0])] = l[1:]
    return d

T = Transport()


def nb_fichier(d, l):
    nb = 0
    for i in l:
        nb += len(d[int(i)])
    return nb

def vop2():
    T = Transport()
    d = todict()
    d[0] = []
    depart = 0
    max = 0
    dist = 0
    l2 = []
    q = ""
    cmp = 0
    for p in d.keys():
        if len(d[max]) < len(d[p]):
            max = p

    init = T.itinerary(depart, max)
    m = init
    courant = 10
    var = 300 
    nb = 10
    l = [2]
    while dist<80000 and var <3600:
        max = 0
        b = False
        print(var)
        for i in d:
            nn = nb_fichier(d, T.path_to_string(m[0][i], m[1]).strip(" ").split(" "))
            if m[0][i] < var and nn>=max and nn>=nb :
                courant = T.path_to_string(m[0][i], m[1])
                max = nn
                b = True
            #print(nb_fichier(d, T.path_to_string(m[0][i], m[1]).strip(" ").split(" ")))
        if not b :
            var += 1
            continue

        # m = T.itinerary(depart, max)
        l = courant.strip(" ").split(" ")
        for i in range(len(l)):
            if cmp >= 10:
                m = T.itinerary(depart, int(l[i-1]))
                dist += m[0][i]
                cmp = 0
                depart = 0
                for p in d.keys():
                    if len(d[max]) < len(d[p]):
                        max = p
                break
            q += 'a'
            l2.append(l[i] + q)
            r = [elem for elem in d[int(l[i])][:10 - cmp] if elem not in l2]
            d[int(l[i])] = [elem for elem in d[int(l[i])][:10 - cmp] if elem not in r]
            l2 += r
            cmp += len(r)
            if i>0:
                T.actu_node(int(l[i-1]), int(l[i]), 0)
        dist += m[0][int(l[-1])]

    l3 = list(OrderedDict.fromkeys(l2))
    for i in range(len(l3)):
        l3[i] = l3[i].strip('a')
    print(" ".join(l3))
    return len(l3)




print(vop2())
'''
if cmp >= 10:
    cmp = 0
    depart = 0
    for p in d.keys():
        if len(d[max]) < len(d[p]):
            max = p
    continue
# m = T.itinerary(depart, max)
l = m[1].strip(" ").split(" ")
if nb_fichier(d, l) < 10:
    max = random.choice(list(d.items()))[0]
    continue
for i in range(len(l)):
    if cmp >= 10:
        m = T.itinerary(depart, int(l[i - 1]))
        dist += m[0]
        cmp = 0
        depart = 0
        for p in d.keys():
            if len(d[max]) < len(d[p]):
                max = p
        break
    q += 'a'
    l2.append(l[i] + q)
    r = [elem for elem in d[int(l[i])][:10 - cmp] if elem not in l2]
    d[int(l[i])] = [elem for elem in d[int(l[i])][:10 - cmp] if elem not in r]
    l2 += r
    cmp += len(r)
    if i > 0:
        T.actu_node(int(l[i - 1]), int(l[i]), 0)
dist += m[0]
for p in d.keys():
    if len(d[max]) < len(d[p]):
        max = p
max = random.choice(list(d.items()))[0]
print(max)
l3 = list(OrderedDict.fromkeys(l2))
for i in range(len(l3)):
    l3[i] = l3[i].strip('a')
print(" ".join(l3))
return len(l3)'''

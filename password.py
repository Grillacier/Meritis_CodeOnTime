# Il te faut un mot de passe pour te connecter sur la machine du voleur.
# Par chance, le mot de passe a été généré par un générateur maison dont nous avons compris le fonctionnement.
# Il utilise une suite de nombres comme source aléatoire, il cherche ensuite dans cette liste, un triplet a, b, c, tel que :
# a+b+c = 987654321
# Le mot de passe est ensuite :
# a*b*c % 987654321
# La suite des nombres aléatoires a été dévoilée, elle constitue ton input.
# En entrée : une liste de nombres, un par ligne.
# Le résultat attendu : le mot de passe recherché.
def fusion(t1, t2):
    if t1 == []:
        return t2
    elif t2 == []:
        return t1
    else:
        if t1[0] < t2[0]:
            return [t1[0]] + fusion(t1[1:], t2)
        else:
            return [t2[0]] + fusion(t1, t2[1:])


def tri_fusion(T):
    if len(T) <= 1:
        return T
    else:
        c = len(T) // 2
    return fusion(tri_fusion(T[0:c]), tri_fusion(T[c:]))


def tri_insertion(tab):
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)):
        k = tab[i]
        j = i - 1
        while j >= 0 and k < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = k


def dicho(t, v):
    a = 0
    b = len(t)
    if b == 0:
        # il faut traîter le cas
        # où la liste est vide
        return False, -1
    while b > a + 1:
        m = (a + b) // 2
        if t[m] > v:
            b = m
        else:
            a = m
    return t[a] == v, a


def password():
    "ouvre un fichier et trouve les trois valeurs dont la somme est 987654321"
    l = []
    min = 0
    with open("data") as f:
        min = int(f.readline())
        l.append(min)
        for ligne in f:
            l.append(int(ligne))
    length = len(l)
    tri_insertion(l)
    print("tri terminé")
    #print(l[24289])
    for i in range(length/2,length):
        if l[i] + 2 * l[-1] < 987654321:
            continue
        for j in range(length):
            if l[i] + l[j] + l[-1] < 987654321:
                continue
            if l[i] + l[j] >= 987654321:
                break
            m = dicho(l, 987654321 - (l[i] + l[j]))
            #print(l[i], l[j], l[m[1]])
            if m[0]:
                print(l[i])
                print(l[j])
                print(l[m[1]])
                return l[i] * l[j] * l[m[1]] % 987654321
    return 0


print(password())

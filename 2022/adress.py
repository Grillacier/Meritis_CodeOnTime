def address() :
    "retourne l'adresse associée à la consommation la plus élevée"
    add_max = ""
    max = 0
    with open("data") as f:
        for ligne in f:
            l = ligne.split(" ")
            if max < int(l[0]):
                max = int(l[0])
                add_max = " ".join(l[1:])
    return add_max
print(address())
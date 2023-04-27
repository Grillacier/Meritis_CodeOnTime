# 1 : 4500
# 2 : 872696
# 3 : 16114107
# 4 : 1050818
# 5 : 2916700

with open('data1.txt') as f:
    n, m = map(int, f.readline().strip().split())
    missions = []

    for i in range(n):
        start, end, r = map(int, f.readline().strip().split())
        missions.append((start, end, r, i))
    missions.sort()

    chronobots = []
    for j in range(m):
        oj, ej, cj = map(int, f.readline().split())
        chronobots.append((oj, ej, cj, j))
    chronobots.sort()

    missions.sort(key=lambda x: x[2], reverse=True)

    chronobots.sort(key=lambda x: x[2])

    assignment = [-1] * n
    last_end = [-1] * m
    revenues = [0] * (m + 1)
    l = len(chronobots)

    for fi, di, ri, i in missions:
        revenu_m = []
        for oj, ej, cj, j in chronobots:
            revenue = -1
            if last_end[j] >= fi:
                continue
            if oj > 0:
                revenu_m.append((ri, j))
            else:
                revenu_m.append((min(ri * cj / 100, 2 * ri) - ej, j))
        revenu_m.sort(key=lambda x: x[0], reverse=True)

        if revenu_m:
            r, j = revenu_m[0]
            assignment[i] = j
            last_end[j] = di
            revenues[j] += r

    print(" ".join(str(j + 1) for j in assignment))
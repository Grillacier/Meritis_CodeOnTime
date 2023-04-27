# 1 : 4500
# 2 : 957005
# 3 : mon pc est mort
# 4 : 52506
# 5 : mon pc est mort

from collections import namedtuple

Mission = namedtuple('Mission', ['start', 'end', 'revenue', 'index'])
Chronobot = namedtuple('Chronobot', ['obsolescence', 'maintenance_cost', 'post_obsolescence_coeff', 'index'])

with open('data5.txt') as f:
    n, m = map(int, f.readline().strip().split())
    missions = []

    for i in range(n):
        start, end, r = map(int, f.readline().strip().split())
        missions.append(Mission(start, end, r, i))

    chronobots = []
    for j in range(m):
        oj, ej, cj = map(int, f.readline().split())
        chronobots.append(Chronobot(oj, ej, cj, j))

    missions.sort(key=lambda x: (x.revenue, x.start), reverse=True)
    chronobots.sort(key=lambda x: x.post_obsolescence_coeff)

    assignment = [-1] * n
    last_end = [-1] * m
    revenues = [0] * (m + 1)

    for i, mission in enumerate(missions):
        revenu_m = []
        for j, chronobot in enumerate(chronobots):
            if last_end[j] >= mission.start:
                continue
            if chronobot.obsolescence >= mission.end:
                revenue = mission.revenue
            else:
                k = sum(1 for m in missions if m.index < mission.index and assignment[m.index] == j)
                revenue = min(mission.revenue * chronobot.post_obsolescence_coeff / 100, 2 * mission.revenue) - chronobot.maintenance_cost * (k + 1)
            revenu_m.append((revenue, j))
        revenu_m.sort(reverse=True)

        if revenu_m:
            r, j = revenu_m[0]
            assignment[mission.index] = j
            last_end[j] = mission.end
            revenues[j] += r

    print(" ".join(str(j + 1) for j in assignment))
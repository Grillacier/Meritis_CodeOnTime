with open('data.txt') as file:
    n = int(file.readline().strip())
    data = []

    for i in range(n):
        d, f, r = map(int, file.readline().strip().split())
        data.append((d, f, r, i+1))

    data.sort(key=lambda x: x[1])

    end = -1
    score = 0
    done = []

    for mission in data:
        di, fi, ri, index = mission
        if di > end:
            end = fi
            done.append(index)
            score += ri

    print(*done)
import heapq

with open('data.txt') as file:
    n = int(file.readline().strip())
    data = []

    for i in range(n):
        start, end = map(int, file.readline().strip().split())
        data.append((start, end))

    data.sort(key=lambda x: x[0])
    bots = []

    for j in data:
        start, end = j
        if bots and bots[0] <= start:
            heapq.heappop(bots)
        heapq.heappush(bots, end)

    print(len(bots))
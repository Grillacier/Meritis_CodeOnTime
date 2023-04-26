data = {}
max = 0
maxIndex = 0
key = 0

with open("data.txt") as file:
    for line in file:
        value = int(line)
        data[key] = value
        if value > max:
            max = value
            maxIndex = key
        key += 1

print(maxIndex, max)
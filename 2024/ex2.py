#creates a list from data given
def get_data(f):
    content = []
    with open(f) as my_file:
        content = my_file.read().split("\n")
    del(content[len(content)-1])
    return content
data = get_data("data2")

#creates file for output
f = open("output.txt", "x")

def evo(f, l):
    times = []
    times.append(int(l[0]))
    count = 0
    for i in range(1, len(l)):
        if int(l[i]) < times[count]:
            times.append(int(l[i]))
            count+=1

    f = open("output.txt", "a")
    f.write(str(times) + "\n")
    f.close()
    return evo(f, l[1:])
evo(f, data)
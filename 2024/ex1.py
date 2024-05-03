#creates a list from data given
def get_data(f):
    content = []
    with open(f) as my_file:
        for l in my_file.readlines():
            content.append(l.strip())
    return content
data = get_data("data1")

def split_data(data):
    l = []
    for line in data:
        l.append(line.split(","))
    return l
# print(split_data(data))
datalist = split_data(data)

#checks if a string is an integer
def is_int(s):
    if s[0].isdecimal():
        return True

#gets each country from list
def get_countries(l):
    countries = {}
    for i in range(len(l)):
        for j in range(3):
            if not is_int(l[i][j]):
                countries[l[i][j]] = 0
    return countries
countries = get_countries(datalist)

#gets minimum time
def get_time(countries, data):
    for i in range(len(data)):
        for j in range(3):
            if not is_int(data[i][j]):
                countries[data[i][j]] += int(data[i][j+1])
    return min(zip(countries.values(), countries.keys()))[1]
print(get_time(countries, datalist))
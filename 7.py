dic = {}
for cl in range(1, 12):
    dic[cl] = [0, 0]

with open ('dataset_3380_5.txt', 'r') as file:
    for line in file:
        line = line.strip().split('\t')
        cl = int(line[0])
        height = int(line[2])
        dic[cl][0] += height
        dic[cl][1] += 1

for cl in range(1, 12):
    try:
        median = float(dic[cl][0] / dic[cl][1])
    except ZeroDivisionError:
        median = '-'
    print(cl, median)
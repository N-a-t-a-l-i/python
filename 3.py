dic = {}
names = []
cnt = 0
math = 0
phis = 0
rus = 0

with open ('dataset_3363_4.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().split(';')
        name = line[0]
        names += [name]
        dic[name] = [int(i) for i in line[1:]]
        math += int(line[1])
        phis += int(line[2])
        rus += int(line[3])
        cnt += 1

with open ('answer3.txt', 'w') as file:
    for name in names:
        scores = sum(dic[name]) / 3
        results = str(math / cnt) + ' ' + str(phis / cnt) + ' ' + str(rus / cnt)
        file.write(str(scores) + '\n')
    file.write(results)
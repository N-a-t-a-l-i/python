dic = {}
words = []
words_max = []

with open ('dataset_3363_3.txt', 'r') as file:
    for line in file:
        print(line)
        for word in line.lower().strip().split():
            words += [word]
            if word not in dic.keys():
                dic[word] = 1
            else:
                dic[word] += 1
                
print(dic)

max_value = 0
for value in dic.values():
    if value > max_value:
        max_value = value

for word in words:
    if dic[word] == max_value:
        words_max.append(word)

words_max.sort()

print (words_max[0], max_value)

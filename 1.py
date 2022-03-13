st = ""  '''Egor pomidor'''

with open ('dataset_3363_2.txt', 'r') as file:
    s = file.readline().strip()+'z'
    print(s)
    number_str = "0"
    alpha = ""
    
    'rrr'
    
    fff
    hello
    
    for symbol in s:
        if symbol.isalpha():
            number = int(number_str)
            for i in range(number):
                st += alpha
            number_str = ""
            alpha = symbol
        else:
            number_str += symbol
                
with open ('Answer_1.txt', 'w') as answer:
    answer.write(st)
    print(st)
    
    'sss'
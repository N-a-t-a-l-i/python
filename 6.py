import requests

with open ('dataset_3378_3.txt', 'r') as file:
    url = 'https://stepic.org/media/attachments/course67/3.6.3/949017.txt'
 
content = ''

while True:
    next_file = requests.get(url)
    content = next_file.text.strip()
    print(content)  
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + content
    if 'we' in content:
        print(content)
        break

with open ('answer6.txt', 'w') as answer:
    for line in next_file.text:
        answer.write(line)
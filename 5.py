import requests

with open ('dataset_3378_2.txt', 'r') as file:
    url = file.readline().strip()

print(url)

page = requests.get(url)

print(page.text)

strings = page.text.splitlines()

print(len(strings))

    

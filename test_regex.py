from bs4 import BeautifulSoup
import requests

# Disini kita akan mengambil semua data "h2" dalam website/URL di bawah ini (tanpa mengambil "Contents")
url = 'https://en.wikipedia.org/wiki/Economy_of_China'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

result = []
x = soup.find_all('h2')
for h2 in x:
    span = h2.find('span')
    print(span)
    if span:
        result.append(span.text)

print(" ")
print(result) 
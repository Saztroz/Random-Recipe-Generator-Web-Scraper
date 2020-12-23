import requests
from bs4 import BeautifulSoup
import random

res = requests.get('https://www.budgetbytes.com/category/recipes/dessert/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.more-link')

li = []
for tag in links:
    li.append(tag.get('href'))

lucky_dessert = random.choice(li)
res2 = requests.get(lucky_dessert)
soup2 = BeautifulSoup(res2.text, 'html.parser')
ingredients = soup.select('.data-recipe')

for tag in soup2.find_all('wprm-recipe-ingredient-group'):
    print(f'{tag.text}')

print(lucky_dessert)




from bs4 import BeautifulSoup #grab html data
import requests #access/download webdata 
website = 'https://news.ycombinator.com/news'
res = requests.get(website)

soup = BeautifulSoup(res.text, 'html.parser')

#print(soup.prettify())
print(soup.title)
print(soup.find_all('a'))
#print(soup.get_text())
print(soup.select('.score')) #using css selectors
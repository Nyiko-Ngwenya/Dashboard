from bs4 import BeautifulSoup
import requests
#import lxml

source = requests.get('https://www.imdb.com/chart/top?ref_=nv_mv_250').text
#print(source)
soup = BeautifulSoup(source,'lxml')
#print(soup)

article = soup.find_all('')

print(article)
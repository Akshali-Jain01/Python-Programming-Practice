from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.sih.gov.in/sih2022PS#")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'col-sm-12'}):
  name= a.find('div', attrs={'class':'container wrapper'})
  price=a.find('div', attrs={'class':'row'})
  rating=a.find('div', attrs={'class':'dataTables_filter'})
  products.append(name.text)
  prices.append(price.text)
  ratings.append(rating.text) 
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')


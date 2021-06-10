

import urllib3
import requests
import pandas as pd
from bs4 import BeautifulSoup
import string

#Making storage for data
company_name = []
company_ticker = []

#create a function to scrape the data
def scrape_stock_symbols(Letter):
  Letter = Letter.upper()
  URL = 'https://www.advfn.com/nyse/newyorkstockexchange.asp?companies='+Letter  #NYSE scrape
  URL2 = 'https://www.advfn.com/nasdaq/nasdaq.asp?companies='+Letter             #NASDAQ scrape
  page = requests.get(URL)
  page2 = requests.get(URL2)
  soup = BeautifulSoup(page.text, 'html.parser')
  soup2 =BeautifulSoup(page2.text, 'html.parser')
  odd_rows = soup.find_all('tr', attrs={'class':'ts0'})
  even_rows = soup.find_all('tr', attrs={'class':'ts1'})
  odd_rows2 = soup2.find_all('tr', attrs={'class':'ts0'})
  even_rows2 = soup2.find_all('tr', attrs={'class':'ts1'})

  for i in odd_rows:
    row = i.find_all('td')
    company_name.append(row[0].text.strip()) #Company Name
    company_ticker.append(row[1].text.strip()) #Company Ticker
    
  for i in odd_rows2:
    row = i.find_all('td')
    company_name.append(row[0].text.strip()) #Company Name
    company_ticker.append(row[1].text.strip()) #Company Ticker

  for i in even_rows:
    row = i.find_all('td')
    company_name.append(row[0].text.strip()) #Company Name
    company_ticker.append(row[1].text.strip()) #Company Ticker

  for i in even_rows2:
    row = i.find_all('td')
    company_name.append(row[0].text.strip()) #Company Name
    company_ticker.append(row[1].text.strip()) #Company Ticker

  return(company_name, company_ticker)

#Loop through every letter in the alphabet to get all of the tickers and company names from advfn
for char in string.ascii_uppercase:
  (temp_name, temp_ticker) = scrape_stock_symbols(char)

data = pd.DataFrame(columns=['company_name', 'company_ticker'])
data['company_name'] = temp_name
data['company_ticker'] = temp_ticker
data = data[data['company_name'] != '']
#show data
pd.set_option('max_rows', 99999)
pd.set_option('max_colwidth', 400)
pd.describe_option('max_colwidth')
data
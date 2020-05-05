from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import chromeDriverPath

from bs4 import BeautifulSoup

import datetime as dt

def getHtml(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu') 

    driver=webdriver.Chrome(options=chrome_options, executable_path=chromeDriverPath)
    driver.get(url)
    html=driver.page_source
    driver.close()
    return html

def getOptionsData(soup):
    callBody=soup.find('tbody',attrs={'id':'tCallsListado'})
    putBody=soup.find('tbody',attrs={'id':'tPutsListado'})
    rows=callBody.find_all('tr')+putBody.find_all('tr')
    dataRows=[]
    for row in rows:
        name=row.find('a').text
        name=name[name.find('\n')+1:name.rfind('\n')]
        cells=row.find_all('td')
        price=float(cells[5].text.replace(',','.'))
        volume=int(cells[-2].text.replace('.',''))
        dataRows.append([name,price,volume])

    return dataRows

def getStockPrice(soup):
    tag=soup.find('span',{'data-field':'UltimoPrecio'})
    return float(tag.text.replace(',','.'))

def writeOptionsCsv(price,optionsData,filePath):
    dataFile=open(filePath,'a+')
    for row in optionsData:
        dataFile.write(f"{row[0]},{row[1]},{row[2]},{price},{dt.date.today()}\n")
    dataFile.close()

def updateDataFile(filePath,url):
    source=getHtml(url)
    soup=BeautifulSoup(source)
    optionsData=getOptionsData(soup)
    price=getStockPrice(soup)
    writeOptionsCsv(price,optionsData,filePath)

url='https://www.invertironline.com/titulo/cotizacion/BCBA/GGAL/GRUPO-FINANCIERO-GALICIA/opciones'
filePath='GGALoptions.txt'

updateDataFile(filePath,url)
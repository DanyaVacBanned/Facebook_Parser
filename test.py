from lib2to3.pgen2.token import OP
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as b
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://anekdot.ru')
html = driver.page_source
soup = b(html, 'lxml')
driver.quit()
topicbox = soup.find_all('div', class_='topicbox')
for text in topicbox:
    words = str(text.find('div', class_='text'))
    link = text.find('a').get('href')
   
    print('Текст: ',words.lower(),'Ссылка: ',link)

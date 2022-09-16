
from bs4 import BeautifulSoup as b
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from data import get_words

def get_urls():
    with open('groups.txt', 'r', encoding='utf-8') as f:
        array = [row.strip() for row in f]
        return array
        # print(array)
def main():
    try:
        options = Options()
        options.add_argument('--headless')       
        urls = get_urls()
        driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
        #Autorizathion
        driver.get('https://facebook.com')
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        username = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')
        time.sleep(2)
        username.clikc()
        username.send_keys('+995558401496')
        time.sleep(2)
        password = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')
        time.sleep(2)
        password.click()
        password.send_keys('123456789Ks')
        time.sleep(2)
        button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
        time.sleep(2)
        button.click()
        time.sleep(5)

        #debug
        # driver.get('https://www.facebook.com/groups/georgiawithkids/?ref=share')
        # time.sleep(2)
        # html = driver.page_source
        # time.sleep(2)
        # soup = b(html, 'lxml')
        # divs= str(soup.find_all('div', {'dir':'auto'}))
        # splitted_divs = divs.split()
        # for l in splitted_divs:
        #     for i in get_words():
        #         if i == l:
        #             print(l)
        
        # scrapping        
        for url in urls:
            driver.get(url=url)
            time.sleep(2)
            html = driver.page_source
            time.sleep(2)
            soup = b(html, 'lxml')
            divs = soup.find_all('div', {'class': 'bdao358l'})
            for content in divs:
                text = str(content.find('div', {'dir':'auto'}))
                link = content.find('a', {'class':'qi72231t'})
                splitted_text = text.lower().split()
                for word in splitted_text:
                    if get_words() == word:
                        return "Есть совпадение по вашему запросу: " + link

    except Exception as ex:
        print(ex)
        
    finally:
        driver.close()
        driver.quit()



if __name__ =="__main__":
    main()
                


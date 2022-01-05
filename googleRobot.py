import time, csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def execute(search_for, pages):
    driver = webdriver.Chrome()
    driver.get('http://www.google.com/')

    return searchInGoogle(search_for, pages, driver)

def searchInGoogle(sinonimo_pesquisa, paginas, driver):
    results = []

    for index in range(paginas):
        if (index+1) == 1:
            campo_pesquisa = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')
            campo_pesquisa.send_keys(sinonimo_pesquisa)
            campo_pesquisa.send_keys(Keys.ENTER)
        else:
            campo_pesquisa = driver.find_element_by_xpath('//a[@aria-label=\'Page '+str(index+1)+'\']')
            campo_pesquisa.click()

        frames_google = driver.find_elements_by_xpath('//div[@class="g" and div[1]/div[1]/div[1]/a]')

        for i in range(len(frames_google)):
            try:
                link = frames_google[i].find_element_by_xpath('./div[1]/div[1]/div[1]/a').get_attribute('href')
                title = frames_google[i].find_element_by_xpath('./div[1]/div[1]/div[1]/a/h3').text
                if(title != ''):
                    results.append({"title": title, "link": link})
            except:
                print("Este bloco deu algum erro na captura!")

    driver.get('http://www.google.com/')

    return results
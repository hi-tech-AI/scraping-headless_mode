from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from time import sleep
import json

def Find_Element(driver : webdriver.Chrome, by, value : str) -> WebElement:
    while True:
        try:
            element = driver.find_element(by, value)
            break
        except:
            pass
        sleep(0.1)
    return element

def Find_Elements(driver: webdriver.Chrome, by, value : str) -> list[WebElement]:
    while True:
        try:
            elements = driver.find_elements(by, value)
            if len(elements) > 0:
                break
        except:
            pass
        sleep(0.1)
    return elements

def Send_Keys(element : WebElement, content : str):
    element.clear()
    for i in content:
        element.send_keys(i)
        sleep(0.1)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options = chrome_options)

url = 'https://www.worldometers.info/geography/alphabetical-list-of-countries/'
driver.get(url)

countries = Find_Element(driver, By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
output = []

for country in countries:
    splits = country.text.split(' ')
    country_name = " ".join(splits[1 : len(splits) - 3])
    output.append({"country" : country_name})
    population = country.find_element(By.TAG_NAME, 'a').text
    land_area = splits[len(splits) - 2]
    density = splits[len(splits) - 1]
    print(country_name)
    print(population)
    print(land_area)
    print(density)

with open('output.json', 'w') as file:
    json.dump(output, file)

driver.quit()   
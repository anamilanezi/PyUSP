from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def get_price(element):
    number = element.text.split("- ")[-1]
    if "," in number:
        number = number.replace(",", "")
    return int(number)


def get_name(element):
    return element.text.split(" - ")[0]


service = Service("D:/Usuarios/Usuario/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
# driver.minimize_window()

cookie = driver.find_element(By.ID, "cookie")
score = driver.find_element(By.ID, "money")

# cursor = driver.find_element(By.CSS_SELECTOR, '#buyCursor b')
# cursor_price = get_price(cursor)
#
# grandma = driver.find_element(By.CSS_SELECTOR, '#buyGrandma b')
# grandma_price = get_price(grandma)

store = driver.find_elements(By.CSS_SELECTOR, "#store div b")

#store_dic = {}

# for item in store[:-1]:
#     name = get_name(item)
#     price = get_price(item)
#     store_dic[name] = price

names = []
prices = []

for item in store[:-1]:
    names.append(get_name(item))
    prices.append(get_price(item))

names.reverse()
prices.reverse()

timeout = time.time() + 5
five_min = time.time() + 60*5
print(timeout)

while True:
    cookie.click()
    if time.time() > timeout:
        for i in range(len(names)):
            if int(score.text) >= prices[i]:
                link = driver.find_element(By.ID, f"buy{names[i]}")
                link.click()
                timeout += 5
                break
        if time.time() > five_min:
            cookie_per_s = driver.find_element(By.ID, "cps").text
            print(cookie_per_s)
            break


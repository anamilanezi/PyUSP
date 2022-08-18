from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("D:/Usuarios/Usuario/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# driver.get("https://en.wikipedia.org/wiki/Main_page")

# articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(articles.text)

# articles = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# articles.click()

# Find a link using text
# content_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# content_portals.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Ana Carolina")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Medeiros Milanezi")

email = driver.find_element(By.NAME, "email")
email.send_keys("anamilanezi@gmail.com")

button = driver.find_element(By.CSS_SELECTOR, "form button")
button.click()
#driver.quit()

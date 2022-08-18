from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("D:/Usuarios/Usuario/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org")
# find_element = driver.find_elements(By.CLASS_NAME, "event-widget time")
# print(find_element)

# Forms usually have a name element, so it's an easy way to use selenium to automate forms
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# Using XPATH
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.get_attribute("href"))

# Find Elements gives a list of objects
# raw_events = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu")
# time = []
# name = []
# for event in raw_events:
#     listed_events = event.text.split("\n")
#
# for i in range(0, 10, 2):
#     time.append(listed_events[i])
#     name.append(listed_events[i + 1])
# print(time)
# print(name)
# events_dic = {}
#
# for i in range(len(time)):
#     events_dic[i] = {"time": time[i],
#                      "name": name[i],
#                      }
# print(events_dic)

# Angela solution
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)
# Close will close the active tab
# driver.close()

# Quit will close the browser
driver.quit()

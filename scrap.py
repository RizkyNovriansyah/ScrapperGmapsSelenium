import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com/maps')

# kota = input('kota : ')
# key = input('key : ')
kota = "Malang"
key = "Toko Sepatu"

final_msg = key+", "+kota
ActionChains(driver).send_keys(final_msg).perform()

class_find = 'searchbox-searchbutton'
driver.find_element_by_class_name(class_find).click()

# 
time.sleep(4)
class_item = 'section-result'
items = driver.find_elements_by_class_name(class_item)
time.sleep(2)
print(len(items))
# print(items)


# ActionChains(driver).key_up(Keys.ENTER).perform()

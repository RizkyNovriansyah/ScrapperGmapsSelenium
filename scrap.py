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
# time.sleep(4)
class_item = 'section-result'
items = []
while len(items) == 0 :
    items = driver.find_elements_by_class_name(class_item)

print(len(items))
count = 0
# print(items)
for item in items:
    count += 1
    print("== Detail Item ==")
    item.click()
    print("Title : ")
    
    # time.sleep(4)
    val = []
    while len(val) == 0 :
        val = driver.find_elements_by_class_name('section-hero-header-title-title')
    title = val[0].find_element_by_tag_name('span')
    print(title.text)

    print("Back To list")
    class_back = 'section-back-to-list-button'
    driver.find_element_by_class_name(class_back).click()
    time.sleep(4)

    class_item = 'section-result'
    items = driver.find_elements_by_class_name(class_item)
    # time.sleep(4)

    for x in range(count):
        items.pop(0)
    
    print(len(items))



# ActionChains(driver).key_up(Keys.ENTER).perform()

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com/maps')

# kota = input('kota : ')
# key = input('key : ')
kota = "Jakarta"
key = "Toko Sepatu"

find_key = key+", "+kota
ActionChains(driver).send_keys(find_key).perform()
class_find = 'searchbox-searchbutton'
driver.find_element_by_class_name(class_find).click()

#
# time.sleep(4)
class_item = 'section-result'
items = []
while len(items) == 0:
    items = driver.find_elements_by_class_name(class_item)

print(len(items))
count = 0
nama_tokos = []
for item in items:
    temp_title = []
    while len(temp_title) == 0:
        temp_title = item.find_elements_by_class_name('section-result-title')
    title = temp_title[0].find_element_by_tag_name('span')
    nama_toko = title.text
    nama_tokos.append(nama_toko)

class_close = 'gsst_a'
driver.find_element_by_class_name(class_close).click()

all_data = []
for nama_toko in nama_tokos:
    final_msg = nama_toko+", "+kota
    if final_msg == find_key:
        continue
    
    print("Find : ")
    print(final_msg)
    ActionChains(driver).send_keys(final_msg).perform()
    class_find = 'searchbox-searchbutton'
    driver.find_element_by_class_name(class_find).click()

    temp_title = []
    error = 0
    while len(temp_title) == 0:
        temp_title = driver.find_elements_by_class_name('section-hero-header-title-title')
        try:
            temp_titles = []
            temp_titles = driver.find_elements_by_class_name('section-result-title')
            if len(temp_titles) > 0 :
                is_not_exist = True
                for t in temp_titles:
                    title = t.find_element_by_tag_name('span')
                    title_temp = title.text 
                    if title_temp == nama_toko:
                        t.click() 
                        is_not_exist = False
                        break   
                if is_not_exist:
                    temp_titles[0].click() 
            
        except:
            error += 1
            if error > 5:
                print(x)
        
    detail = {}

    title = temp_title[0].find_element_by_tag_name('span')
    while title.text == "":
        pass
    detail_nama_toko = title.text
    print("detail_nama_toko : ")
    print(detail_nama_toko)
    detail["nama"] = detail_nama_toko

    btn_detail = driver.find_elements_by_class_name('ugiz4pqJLAG__button')
    # Val 1 alamat, 2 notelp
    counting_val = 0 
    for btn in btn_detail:
        val = btn.get_attribute("aria-label")
        if val is not None:
            num = not "." in val and not "," in val 
        else:
            num = False
        if counting_val == 0:
            detail["alamat"] = val
            print("alamat:")
            print(val)
        elif num:
            detail["notelp"] = val
            print("notelp:")
            print(val)
        counting_val += 1

    all_data.append(detail)
    class_close = 'sbcb_a'
    driver.find_element_by_class_name(class_close).click()


# ActionChains(driver).key_up(Keys.ENTER).perform()

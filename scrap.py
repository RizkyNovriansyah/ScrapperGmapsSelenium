import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import Workbook
import os
# from time import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com/maps')

# kota = input('kota : ')
# key = input('key : ')
time.sleep(2)
kota = "Jakarta"
key = "Toko Sepatu"

find_key = key+", "+kota
ActionChains(driver).send_keys(find_key).perform()
class_find = 'searchbox-searchbutton'
driver.find_element_by_class_name(class_find).click()

nama_tokos = []
for x in range(2):
    time.sleep(4)
    class_item = 'section-result'
    items = []
    while len(items) == 0:
        items = driver.find_elements_by_class_name(class_item)

    # print(len(items))
    for item in items:
        temp_title = []
        while len(temp_title) == 0:
            temp_title = item.find_elements_by_class_name('section-result-title')
        title = temp_title[0].find_element_by_tag_name('span')
        nama_toko = title.text
        nama_tokos.append(nama_toko)

    driver.find_element_by_class_name('n7lv7yjyC35__button-next-icon').click()
    
print("Data Recorded : ")
print(len(nama_tokos))

class_close = 'gsst_a'
driver.find_element_by_class_name(class_close).click()

all_data = []
for nama_toko in nama_tokos:
    final_msg = nama_toko+", "+kota
    if final_msg == find_key:
        continue
    
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
    try:
        title = temp_title[0].find_element_by_tag_name('span')
        while title.text == "":
            pass
        detail_nama_toko = title.text
        print("Nama Toko : ")
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
            elif num:
                detail["notelp"] = val
            
        all_data.append(detail)
        counting_val += 1
    except :
        pass
    
    class_close = 'sbcb_a'
    driver.find_element_by_class_name(class_close).click()

wb = Workbook()
sheet = wb.active
counter_data = 1
sheet.append(("No","Nama Toko","Notelp","Alamat"))
for item in all_data:
    nama = item["nama"]

    alamat = item["alamat"]
    alamat = alamat.split(": ")
    alamat = alamat[1]
    try:
        notelp = item["notelp"]
        notelp = notelp.split(": ")
        notelp = notelp[1]
    except:
        notelp = ""
    
    sheet.append((counter_data,nama,notelp,alamat))
    counter_data += 1
current_time = time.time()
timez = str(current_time).split('.')
task_id =  timez[0]
path = "%s.xlsx" % (task_id)
print(path)
wb.save("data/"+path)
# ActionChains(driver).key_up(Keys.ENTER).perform()
driver.close()
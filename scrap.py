from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com/maps')

kota = input('kota : ')
key = input('key : ')

final_msg = key+", "+kota
ActionChains(driver).send_keys(final_msg).perform()

driver.find_element_by_class_name('searchbox-searchbutton').click()
# ActionChains(driver).key_up(Keys.ENTER).perform()

from selenium import webdriver

url_base = "https://cosmos.bluesoft.com.br/"

driver = webdriver.Chrome()
driver.get(url_base)

input_barcode = '7898944856141' # input('Digite o código de barras:')

input = driver.find_element_by_id("search-input")
input.send_keys(input_barcode)

button = driver.find_element_by_id("magnifier")
button.click()

product_description = driver.find_element_by_id("product_description")
image_product = driver.find_element_by_class_name('product-thumbnail').find_element_by_tag_name('img').get_attribute("src")
pais_registro = driver.find_element_by_xpath('//*[@id="dados-gerais"]/div[1]/dl/dd[1]')

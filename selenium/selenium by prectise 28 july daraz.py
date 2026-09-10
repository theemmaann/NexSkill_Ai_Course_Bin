from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = "https://www.alibaba.com/trade/search?spm=a2700.product_home_newuser.header.&has4Tab=true&tab=all"

cService = webdriver.ChromeService(executable_path='C:\\Users\\DELL\\Documents\\GitHub\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=cService)

driver.get(url)

alibaba = []
ali_dom= driver.find_elements(By.XPATH, "//div[contains(@class,'fy26-product-card-wrapper list-card fy26-product-card searchx-offer-item')]")

print("Elements found:", len(ali_dom))
print("Page title:", driver.title)
driver.save_screenshot("debug.png")

for p in range (len(ali_dom)-1):
    baba={}
    img= ali_dom[p+1].find_element(By.TAG_NAME,"img")
    innera= ali_dom[p+1].find_element(By.TAG_NAME,"a")
    price = ali_dom[p+1].find_element(By.TAG_NAME,"div")
    baba["img"] = img.get_attribute('src')
    baba["URL"] = innera.get_attribute('herf')
    baba["Price"] = price.text.strip()
    alibaba.append(baba)

filename='Alibaba_Method2.csv'
with open(filename, 'w', newline='') as f:
    w= csv.DictWriter(f,['img','URL','Price'])
    w.writeheader()
    for baba in alibaba:
        w.writerow(baba)

driver.close()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url="https://zerolifestyle.co/pages/smart-watches"
cService = webdriver.ChromeService(executable_path='C:\\Users\\DELL\\Documents\\GitHub\\chromedriver-win64\\chromedriver.exe') # '/Users/bpfalz/Downloads/chromedriver' for my macbook
driver = webdriver.Chrome(service=cService)
driver.get(url)
watcheslist=[]
watchesdiv=driver.find_elements(By.XPATH, "//product-item[contains(@class,'product-item')]")
for p in range(len(watchesdiv) -1):
    watches={}
    img=watchesdiv[p+1].find_element(By.TAG_NAME,"img")
    innera=watchesdiv[p+1].find_element(By.TAG_NAME,"a")
    price=watchesdiv[p+1].find_element(By.TAG_NAME,'span')
    watches["img"]=img.get_attribute('src')
    watches["url"]=innera.get_attribute('href')
    watches["price"]=price.text.strip()
    watcheslist.append(watches)

filename='Zero_lifestyle_Method2.csv' 
with open (filename,'w', newline='') as f:
    w=csv.DictWriter(f,['img','url','price']) 
    w.writeheader()
    for watches in watcheslist:
        w.writerow(watches)

driver.close()        

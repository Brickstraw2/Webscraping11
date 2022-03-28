from selenium import webdriver
import time 
import json
import sqlite3

conn = sqlite3.connect('price.db')
db = conn.cursor()

driver = webdriver.Chrome('/home/student/Desktop/chromedriver')
driver.get('http://wollplatz.de')


prodcucts =  ['DMC Natura XL']#, 'Drops Safran', 'Drops Baby Merino Mix', 'Stylecraft Special DK']
product_data = {}

time.sleep(5)
cookie = driver.find_element_by_id('AcceptReload')
cookie.click()
time.sleep(3)


for product in prodcucts:
    product_data[product] = []
    search = driver.find_element_by_class_name("input-txt")
    search.send_keys(product)
    time.sleep(3)
    # asd = driver.find_elements_by_class_name('varianten')[0]
    asd = driver.find_element_by_xpath('//*[@id="sooqrView44898be26662b0df"]/div[4]/div/div[2]/div[1]/div/div[1]/h3/a')
    asd.click()
    time.sleep(5)
    price = driver.find_element_by_class_name("product-price-amount").text
    product_data[product].append({
        'price': price
    })
    time.sleep(2)
    # print(price) 
    needle = driver.find_element_by_xpath('//*[@id="pdetailTableSpecs"]/table/tbody/tr[5]/td[2]').text
    product_data[product].append({
        'needle': needle
    })
    # print(needle) 
    time.sleep(2)
    composition = driver.find_element_by_xpath('//*[@id="pdetailTableSpecs"]/table/tbody/tr[4]/td[2]').text
    product_data[product].append({
        'composition': composition
    })
    # print('the composition is ',composition) 
    time.sleep(1)

    with open('/home/student/Desktop/wolle/data.json', 'w+') as outfile:
        json.dump(product_data, outfile)
    
    db.execute("INSERT INTO ccc VALUES (?,?,?)", (price, needle, composition))
    conn.commit()


db.execute("SELECT * FROM ccc")
print(db.fetchall())

conn.close()
print("ok")

#//*[@id="sooqrView44898be26662b0df"]/div[4]/div/div[2]/div[1]/div/div[1]/h3/a
#//*[@id="pdetailTableSpecs"]/table/tbody/tr[5]/td[2]S
#//*[@id="pdetailTableSpecs"]/table/tbody/tr[11]/td[2]
#//*[@id="pdetailTableSpecs"]/table/tbody/tr[11]


#//*[@id="pdetailTableSpecs"]/table/tbody/tr[3]/td[2]
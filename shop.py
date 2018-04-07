from selenium import webdriver
from selenium.webdriver.common.by import By
import xlwt
# import time

options = webdriver.ChromeOptions()
# options.add_argument("headless")
browser = webdriver.Chrome(options=options)
browser.set_page_load_timeout(120)
browser.set_script_timeout(120)

wbk = xlwt.Workbook()
sheet = wbk.add_sheet("sheet 1")
file_name = "D:/大众点评人均价格.xls"
count = 0

shop_id_list = ["shop_id"] # shop_id 是自己提前选择好的。例如：http://www.dianping.com/shop/8887013 这里的 shop_id 是8887013

try:
    for shop_id in shop_id_list:
        print("第" + str(count+1) + "个")
        browser.get("http://www.dianping.com/shop/" + shop_id)
        name_element = browser.find_element(By.CSS_SELECTOR, "#basic-info > h1")
        price_element = browser.find_element(By.CSS_SELECTOR, "#avgPriceTitle")
        try:
            name_element_text = name_element.text.split(" ")[0]
            sheet.write(count, 0, name_element_text)
            print(name_element_text)
            price_element_text = price_element.text.replace("人均:", "")
            sheet.write(count, 1, price_element_text)
            print(price_element_text)
        except Exception:
            continue
        count = count + 1
        wbk.save(file_name)
        # time.sleep(120)

finally:
    browser.close()

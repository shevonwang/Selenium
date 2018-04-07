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

shop_id_list = ["93422081", "97448967", "98523373", "92384680", "77526405", "6031065", "5410564", "8880938", "27342650", "91952106",
                "21151020", "24666802", "68192434", "39683017", "20924197", "67228840", "97081910", "23144620", "96708536", "23304582",
                "92851655", "95048182", "4718318", "5615293", "97042654", "18324847", "76996780", "91060479", "90989481", "76086919",
                "40706441", "65649717", "83588877", "83500589", "57695388", "73577703", "66378265", "76732126", "65545378", "69535262",
                "35809971", "3895429", "92665211", "27495720", "23755186", "2650306", "2186023", "3713956", "13853847", "18676052",
                "92050177", "96567894", "76080744", "69085639", "67923458", "93502858", "8882756", "27189343", "17219829", "23423342",
                "6556315", "57840750", "66703059", "65327808", "9039812", "90329953", "67501793", "22004713", "44360527", "5363700",
                "22519190", "27437238", "80535206", "72461626", "66132892", "95970973", "19727935", "17931548", "5224808", "27137016",
                "69423970", "8673368", "92043678", "59038893", "9779794", "66210714", "95867787", "93314491", "66985041", "66931416",
                "8926193", "23002017", "8951470", "14731381", "19097771", "90968367", "2444296", "91076048", "21332801", "67918734",
                "17220958", "8887013", "73613533", "56829467", "24070822"]

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
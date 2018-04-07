from selenium import webdriver
import xlwt

browser = webdriver.Chrome()
browser.set_page_load_timeout(120)
browser.set_script_timeout(120)
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')
filename = "D:/携程酒店价格4.7.xls"

hotel_id_list = ["6833415", "5795151", "375517", "2870251", "434984", "445812", "4835705", "2006896", "1800795",
                 "2296822", "2288617", "6319866", "2006575",
                 "6577326", "1002219", "1763585", "468509", "3105304", "2019226", "2018072", "1979640", "2336254",
                 "1815793", "2299307", "708044",
                 "701301", "668290", "2120668", "2299600", "1409293", "5845479", "2269516", "1302120", "534115",
                 "2270356",
                 "2298680", "1478062", "3784185", "1322127", "2001856", "8514712", "778348", "2221272", "4445000",
                 "1764854",
                 "1787735", "1004130", "666919", "852475", "4829049", "2200591", "691076", "1281550", "11054829",
                 "2289324",
                 "6122827", "2707296", "1579339", "994891", "718276", "5234922", "2295076", "6083030", "533511",
                 "483133",
                 "9887453", "2277027", "1205352", "856502", "6661244", "2298407", "3440284", "7074310", "2187688",
                 "481831",
                 "1585672", "1587750", "2579599", "4694558", "5607014", "703374", "2300287", "4826937", "824682",
                 "3732370",
                 "436645", "8600310", "8495115", "1958554", "1563450", "2785422", "6461629", "8421402", "5673240",
                 "8179473",
                 "663057", "992511", "535739", "2111496", "1742543"]
try:
    count = 0
    for hotel_id in hotel_id_list:
        # 酒店名字
        print("第 " + str(count + 1) + "个")
        browser.get("http://hotels.ctrip.com/hotel/" + hotel_id + ".html?isFull=F")
        hotel_name = browser.find_element_by_class_name("cn_n")
        print(hotel_name.text)
        sheet.write(count, 0, hotel_name.text)

        # 房间类型
        hotelRoomBox = browser.find_element_by_id("hotelRoomBox")
        room_type_elements = hotelRoomBox.find_elements_by_xpath('.//td[@data-hotelid="' + hotel_id + '"]')
        room_type_last = count
        for i in range(0, len(room_type_elements)):
            rowspan = int(room_type_elements[i].get_attribute("rowspan"))
            for j in range(0, rowspan):
                room_type_text = room_type_elements[i].find_element_by_css_selector(
                    "a.room_unfold.J_show_room_detail").text
                print(room_type_text)
                sheet.write(room_type_last, 1, room_type_text.replace("查看详情", ""))
                room_type_last = room_type_last + 1

        # 价格
        elements_1 = browser.find_elements_by_class_name("base_price")
        for element_1 in elements_1:
            print(element_1.text)
            sheet.write(count, 2, element_1.text)
            count = count + 1
        # 每抓取一个酒店存一次文件
        wbk.save(filename)

finally:
    wbk.save(filename)
    browser.close()

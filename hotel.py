from selenium import webdriver
import xlwt

browser = webdriver.Chrome()
browser.set_page_load_timeout(120)
browser.set_script_timeout(120)
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')
filename = "D:/携程酒店价格4.7.xls"

hotel_id_list = ["hotel_id"] # hotel_id 是自己选择提前选择好的。例如：http://hotels.ctrip.com/hotel/1205352.html?isFull=F 这里的 hotel_id 是1205352
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

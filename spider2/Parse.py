from Settings import *
from Request import Request

# 
def ParseLetterPage(response, doc_name, hos_name, dept_name):
    return ParseExperiencePage(response, doc_name, hos_name, dept_name)

# 
def ParseExperiencePage(response, doc_name, hos_name, dept_name):
    '''
    returns:
        list: content
        Bool: if retry
        Bool: if end
    '''
    items = []
    table_list = response.css("table.doctorjy")
    if len(table_list) == 0:
        return items, True, False
    for table in table_list:
        item = {}
        item['name'] = doc_name
        item['hos_name'] = hos_name
        item['dept_name'] = dept_name
        item['time'] = table.css("tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(3)::text").extract_first("")
        if item['time'] == "":
            return items, False, True
        item['illness'] = table.css("tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > a:nth-child(2)::text").extract_first("")
        if item['illness'] == "":
            item['illness'] = table.css("tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1)::text").extract_first("")
        item['now_state'] = table.css("tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > div:nth-child(4)::text").extract_first("")
        item['fee'] = table.css("tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > div:nth-child(5)::text").extract_first("")
        item['liaoxiao'] = table.css("tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > span:nth-child(1)::text").extract_first("")
        item['attitude'] = table.css("tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2) > span:nth-child(1)::text").extract_first("")
        item['comment'] = table.css("td.spacejy::text").extract()
        items.append(item)
    return items, False, False

def test():
    # url = "https://www.haodf.com/jingyan/kanbingjingyan-xubaohua/5.htm"
    url = "https://www.haodf.com/jingyan/ganxiexin-zhangyongming-6.htm"
    respose = Request(url)
    item = ParseExperiencePage(respose, "家医生", "医院", "科室")
    print(item)
    pass

if __name__ == "__main__":
    test()
from Settings import *
from Request import Request

# 
def ParseLetterPage(response, doc_name, items):
    tmp = response.css()

# 
def ParseExperiencePage(response, doc_name, items):
    '''
    returns:
        list: content
        Bool: if retry
        Bool: if end
    '''
    table_list = response.css("table.doctorjy")
    if len(table_list) == 0:
        return items, True, False
    for table in table_list:
        item = {}
        item['name'] = doc_name
        item['time'] = table.css("tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(3)::text").extract_first("")
        if item['time'] == "":
            return items, False, True
        item['illness'] = table.css("tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > a:nth-child(2)::text").extract_first("")
        item['now_state'] = table.css("tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > div:nth-child(4)::text").extract_first("")
        item['fee'] = table.css("tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > div:nth-child(5)::text").extract_first("")
        item['liaoxiao'] = table.css("tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > span:nth-child(1)::text").extract_first("")
        item['attitude'] = table.css("tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2) > span:nth-child(1)::text").extract_first("")
        item['comment'] = table.css("td.spacejy::text").extract()
        items.append(item)
    return items, False, False
    

    pass

def test():
    # item = {'ill_his_list':[]}
    # url1 = "https://www.haodf.com/doctor/1013224538-all-servicestar.htm"
    # response = request(url1)
    # parse_doc2(response, item)
    # url2 = "https://www.haodf.com/doctor/DE4r0Fy0C9LuSQuZEy6ClyviZLC3b3s8R/jingyan/1.htm"
    # response = request(url2)
    # parse_doc3(response, item)
    url = "https://www.haodf.com/jingyan/kanbingjingyan-xubaohua/5.htm"
    respose = Request(url)
    item, g = ParseExperiencePage(respose, "", [])
    print(item)
    # print(item['goodat'], type(item['goodat']))
    # print(item['title_list'], type(item['title_list']))
    # print(item['intro'], type(item['intro']))
    pass

if __name__ == "__main__":
    test()
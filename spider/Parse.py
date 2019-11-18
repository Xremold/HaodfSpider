from Settings import *
from Request import Request
# 医院主要信息解析
def ParseHospital(response):
    item = {}
    item['name'] = response.css(".hospital-name::text").extract_first("")
    item['tag_list'] = response.css(".hospital-label-item::text").extract()
    # place 的提取可能还有问题，
    item['place'] = response.css("div.h-d-content p:nth-child(2) span.h-d-c-item-text::text").extract_first("")
    item['dept_list'] = response.css(".f-l-i-s-i-w-name::text").extract()

    if response.css(".hospital-influence-box") == []:
        item['score_list'] = response.css(".hp-i-orange::text").extract()
    else:
        item['score_list'] = response.css(".h-i-orange::text").extract()

    item['dept_score_dict'] = response.css(".hospital-o-li-t::text").extract()
    item['dept_score_dict'].extend(response.css(".hospital-o-li-num::text").extract())
    return item

# 医生主要信息解析
def ParseDoctor(response, hos_name, dept_name):
    item = {}
    
    item['name'] = response.css("div.nav h1 a::text").extract_first("")
    item['title_list'] = response.css(".doctor_about > div:nth-child(2) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr > td:contains('职　　称：')~td::text").extract_first("")
    item['dept_name'] = dept_name
    item['hos_name'] = hos_name
    item['goodat'] = response.css("#full_DoctorSpecialize::text").extract_first("")
    item['intro'] = response.css("#full::text").extract()
    item['ifhaodf_list'] = response.css("li.honour-title > span::text").extract()

    item['score_list'] = []
    item['score_list'].append(response.css('p.r-p-l-score::text').extract_first(""))
    item['score_list'].extend(response.css('div.score-part > p > span::text').extract())

    item['online_service_list'] = response.css(".doct_data_xxzx > tbody:nth-child(1) > tr > td:nth-child(2)::text").extract()
    item['online_service_list'].extend(response.css(".doct_data_xxzx > tbody:nth-child(1) > tr > td:nth-child(3) > :nth-child(1)::text").extract())
    # print(item['online_service_list'], len(item['online_service_list']), sep="\n")
    item['clinic_list'] = []
        
    clinic_tds = response.css(".doctortimefrom > tbody:nth-child(1) > tr > td")
    weekday = ["null","周一","周二","周三","周四","周五","周六","周日"]
    time = ["null", "上午", "下午", "夜晚"]
    td_cnt = 8
    while td_cnt < len(clinic_tds):
        td = clinic_tds[td_cnt]
        if td.css("img") != []:
            item['clinic_list'].append([weekday[td_cnt%8] + time[td_cnt//8], td.css("img::attr(title)").extract_first("")])
        td_cnt += 1
    item['sum_dict'] = response.css("div.nav2 > a::text").extract()
    item['sum_dict'].extend(response.css("div.nav2 > a~span::text").extract())

    item['ill_his_list'] = []
    return item

# 解析医生执业经历
def ParseDoctor2(response, item):
    tmp = response.css("a.overflow_ellipsis::text").extract()
    item['ill_his_list'].append(tmp)
    # print("parse_doc2 called", item['ill_his_list'], sep="\n")
    return item

# 解析患者投票
def ParseDoctor3(response, item):
    tmp = response.css("#tabmainin > a::text").extract()
    item['ill_his_list'].append(tmp)
    tmp = response.css("#tabmainin_gray > a::text").extract()
    item['ill_his_list'].append(tmp)
    # print("parse_doc3 called", item['ill_his_list'], sep="\n")
    return item

def ParseLetterPage(response, doc_name, items):
    tmp = response.css()


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
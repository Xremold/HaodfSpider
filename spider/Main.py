from Request import Request
from Parse import ParseDoctor, ParseDoctor2, ParseDoctor3, ParseHospital
from Itemprocess import ProcessDoctor, ProcessHospital
from Settings import *
import utils.process as process
from HandleErr import LogDocErr, LogHosErr

init_hos_cnt = 0
init_hos_written = 0
init_dept_cnt = 0
init_doc_cnt = 0

def hos_level(url, hos_name):
    global init_dept_cnt
    global init_doc_cnt
    global init_hos_cnt
    global init_hos_written

    response = Request(url)
    if init_hos_written == 0: # 医院信息没有写入
        hos_item = ParseHospital(response)
        ProcessHospital(hos_item)
        process.write_a_hospital()
        DebugPrint("========hospital:", hos_name, "written")
    init_hos_written = 0

    depts = response.css(".f-l-i-s-i-w-name")
    for dept in depts:
        if init_dept_cnt > 0: # 跳过已经写入的科室
            init_dept_cnt -= 1
            continue
        dept_url = dept.css("::attr(href)").extract_first("")
        dept_name = dept.css("::text").extract_first("")
        dept_level("https:"+dept_url, hos_name, dept_name)
    process.finish_a_hospital()
    DebugPrint("========hospital:", hos_name, "finished")
    pass

def dept_level(url, hos_name, dept_name): # 这个函数的含义是爬取一页医生列表
    global init_dept_cnt
    global init_doc_cnt
    global init_hos_cnt
    global init_hos_written

    response = Request(url)
    doctors = response.css("a.name::attr(href)").extract()

    for doc_url in doctors:
        if init_doc_cnt > 0:
            init_doc_cnt -= 1
            continue
        doc_url = "https:"+doc_url
        doc_level(doc_url, hos_name, dept_name)
        
    next_list = response.css("a.p_num")
    if len(next_list) == 0:
        process.finish_a_dept()
        DebugPrint("======deptatment:", dept_name, "finished")
        return
    if next_list[-1].css("::text").extract_first("") == "下一页":
        url = next_list[-1].css("::attr(href)").extract_first("")
        url = "https:"+url
        dept_level(url, hos_name, dept_name)
    else:
        process.finish_a_dept()
        DebugPrint("======deptatment:", dept_name, "finished")

def doc_level(url, hos_name, dept_name):
    global init_dept_cnt
    global init_doc_cnt
    global init_hos_cnt
    global init_hos_written

    response = Request(url)
    doc_item = ParseDoctor(response, hos_name, dept_name)
    url1 = response.css("div.doctor_panel:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3)::attr(href)").extract_first()
    url2 = response.css("div.doctor_panel:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3)::attr(href)").extract_first()
    # DebugPrint(url1, url2, end="\n\n\n")
    if url1 != None and url2 == None:
        response = Request("https"+url1)
        doc_item = ParseDoctor2(response, doc_item)
    elif url1 == None and url2 != None:
        doc_item['ill_his_list'].append([])
        response = Request("https:"+url2)
        doc_item = ParseDoctor3(response, doc_item)
    elif url1 != None and url2 != None:
        response = Request("https:"+url1)
        doc_item = ParseDoctor2(response, doc_item)
        response = Request("https:"+url2)
        doc_item = ParseDoctor3(response, doc_item)
    if doc_item['name'] == "":
        LogDocErr(url, hos_level, dept_name)
    else:
        ProcessDoctor(doc_item)
    process.finish_a_doctor()
    DebugPrint("====doctor:", doc_item['name'], "finished")
    pass


def pop_a_hospital(cnt=0):
    with open(SrcFilePath, 'r', encoding='utf-8') as f:
        ret = ""
        for i in range(0, cnt):
            f.readline()
        ret = f.readline()
        if ret == None or ret == "\n" or ret == "":
            return None,None
        return ret.split(',')

if __name__ == "__main__":

    init_hos_cnt, init_hos_written, init_dept_cnt, init_doc_cnt = process.read_json()
    DebugPrint("spider started with init_hos_cnt:", init_hos_cnt, "init_dept_cnt:", init_dept_cnt, "init_doc_cnt", init_doc_cnt)
    st_hos_cnt = init_hos_cnt
    while True:
        hos_name, hos_url = pop_a_hospital(st_hos_cnt)
        if hos_name == None and hos_url == None:
            break
        # hos_url = 'https://www.haodf.com/hospital/DE4raCNSz6OmG3OUNZWCWNv0.htm'
        hos_level(hos_url, hos_name)
        st_hos_cnt += 1

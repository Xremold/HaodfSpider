from Parse import ParseDoctor, ParseDoctor2, ParseDoctor3
from Request import Request
from Settings import *
from Itemprocess import ProcessDoctor
import utils.process as process

def PopAHospital(cnt):
    with open(DocErrLogPath, "r", encoding="utf-8") as f:
        for i in range(0, cnt): 
            f.readline()
        line = f.readline()
        if line == None or line == "" or line == "\n":
            return None, None, None
        return line.split(",")


if __name__ == "__main__":
    cnt = 0
    while True:
        url, hos_name, dept_name = PopAHospital(cnt)
        cnt += 1
        if url == None:
            break
        dept_name = dept_name[:-1]
        # DebugPrint(url, hos_name, dept_name)
        
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
        ProcessDoctor(doc_item)
        if doc_item['name'] == "":
            print("############: ",cnt)
        process.finish_a_doctor()
        # DebugPrint("====doctor:", doc_item['name'], "finished")
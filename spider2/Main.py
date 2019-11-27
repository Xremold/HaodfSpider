from Settings import SrcFilePath, DebugPrint, RestoreExperiencePageErrLog, RestoreLetterPageErrLog
import utils.Process as process
from Request import Request as request
from Parse import ParseExperiencePage, ParseLetterPage
from ItemProcess import ProcessExperiencePage, ProcessLetterPage
import HandleErr as err
import time

doctor_cnt = 0
letter_page_cnt = 0
experience_page_cnt = 0

def LetterPageLevel(url, doc_name, hos_name, dept_name):
    global letter_page_cnt

    response = request(url)
    if letter_page_cnt > 0:                                         # 跳过已经写入的page
        letter_page_cnt -= 1
    else:
        items, retry, end = ParseLetterPage(response, doc_name, hos_name, dept_name)
        if retry:                                                   # 页面解析错误
            err.LogLetterPageErr(url, hos_name, dept_name, doc_name)
            pass
        else:
            ProcessLetterPage(items)
            process.FinishADoctorLetPage()
            # DebugPrint("====letter page finished", "write items:", len(items), "条")
            if end:
                return
        

    next_list = response.css("a.p_num")
    if len(next_list) == 0:                                         # 只有一页
        return
    if next_list[-1].css("::text").extract_first("") == "下一页":    # 有下一页按钮
        url = "https:" + next_list[-1].css("::attr(href)").extract_first("")
        LetterPageLevel(url, doc_name, hos_name, dept_name)
    else:                                                           # 没有下一页按钮
        return
    pass

def ExperiencePageLevel(url, doc_name, hos_name, dept_name):
    global experience_page_cnt

    response = request(url)
    if experience_page_cnt > 0:                                     # 跳过已经写入的page
        experience_page_cnt -= 1
    else:
        items, retry, end = ParseExperiencePage(response, doc_name, hos_name, dept_name)
        if retry:                                                   # 页面解析错误
            err.LogExperiencePageErr(url, hos_name, dept_name, doc_name)
            pass
        else:
            ProcessExperiencePage(items)
            process.FinishADoctorExpPage()
            # DebugPrint("====experience page finished, write items:", len(items), "条")
            if end:
                return
        

    next_list = response.css("a.p_num")
    if len(next_list) == 0:                                         # 只有一页
        return
    if next_list[-1].css("::text").extract_first("") == "下一页":    # 有下一页按钮
        url = "https:"+next_list[-1].css("::attr(href)").extract_first("")
        ExperiencePageLevel(url, doc_name, hos_name, dept_name)
    else:                                                           # 没有下一页按钮
        return
    pass

def DoctorLevel(url, hos_name, dept_name):
    response = request(url)
    doc_name = response.css("div.nav h1 a::text").extract_first("")
    if doc_name == "":
        err.LogDoctorErr(url, hos_name, dept_name)
        pass

    experience_url = response.css("#toptr_type_all > div.lt > div:nth-child(3) > a::attr(href)").extract_first("")
    if experience_url != "":
        ExperiencePageLevel("https:"+experience_url, doc_name, hos_name, dept_name)
    letter_url = response.css("#toptr_type_all > div.lt > div:nth-child(5) > a::attr(href)").extract_first("")
    # DebugPrint(experience_url, letter_url)
    if letter_url != "":
        LetterPageLevel("https:"+letter_url, doc_name, hos_name, dept_name)
    
    process.FinishADoctor()
    DebugPrint("========doctor finished", doc_name, "index:", doctor_cnt)
    pass


def PopADoctor(cnt=0):
    with open(SrcFilePath, "r", encoding="utf-8") as f:
        for i in range(0, cnt):
            f.readline()
        ret = f.readline()
        if ret == None or ret == "" or ret == "\n":
            return None, None, None
        url, hos_name, dept_name = ret.split(",")
        dept_name = dept_name[:-1]
        return url, hos_name, dept_name


def Main():
    global doctor_cnt
    global experience_page_cnt
    global letter_page_cnt
    doctor_cnt, experience_page_cnt, letter_page_cnt = process.ReadJson()
    DebugPrint("spider started with doctor_cnt:", doctor_cnt, "experience_page_cnt:", experience_page_cnt, "letter_page_cnt:", letter_page_cnt)
    while True:
        url, hos_name, dept_name = PopADoctor(doctor_cnt)
        doctor_cnt += 1

        if url == None and hos_name == None and dept_name == None:
            break

        DoctorLevel(url, hos_name, dept_name)

def FinishRest(): 
    # # time.sleep(60)
    # for i in range(0, 2):           # 对医生未解析成功的就在解析两次
    #     process.ResetJson()
    #     err.PutDocErrToSrc()
    #     Main()
    
    # for i in range(0, 2):
    #     err.RestoreExperiencePageErr()
    #     with open(RestoreExperiencePageErrLog, "r", encoding="utf-8") as f:
    #         while True:
    #             tmp = f.readline()
    #             if tmp == None or tmp == "" or tmp == "\n":
    #                 break

    #             url, hos_name, dept_name, doc_name = tmp.split(",")
    #             doc_name = doc_name[:-1]

    #             ExperiencePageLevel(url, doc_name, hos_name, dept_name)
    
    for i in range(0, 1):
        # err.RestoreLetterPageErr()
        with open(RestoreLetterPageErrLog, "r", encoding="utf-8") as f:
            while True:
                tmp = f.readline()
                if tmp == None or tmp == "" or tmp == "\n":
                    break

                url, hos_name, dept_name, doc_name = tmp.split(",")
                doc_name = doc_name[:-1]

                LetterPageLevel(url, doc_name, hos_name, dept_name)
    
    for i in range(0, 1):
        # err.RestoreExperiencePageErr()
        with open(RestoreExperiencePageErrLog, "r", encoding="utf-8") as f:
            while True:
                tmp = f.readline()
                if tmp == None or tmp == "" or tmp == "\n":
                    break

                url, hos_name, dept_name, doc_name = tmp.split(",")
                doc_name = doc_name[:-1]

                ExperiencePageLevel(url, doc_name, hos_name, dept_name)
    pass

if __name__ == "__main__":
    # Main()
    FinishRest()
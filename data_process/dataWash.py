from settings import *
import csv
import json
import re
'''
doctor:
    0:name, 1:title_list, 2:dept, 3:hospital, 4:goodat, 5:intro, 6；ifhaodf_list, 
    7:score_list, 8:online_service_list, 9；clinic_list, 10:sum_dict, 11:ill_his_list
clinic_list:
    (time, type, price, place)
'''

def DocProcessALine(row):

    tmp = row[1]
    if tmp == " ":
        tmp = []
    else:
        tmp = tmp.strip().split(" ")
    row[1] = json.dumps(tmp, ensure_ascii=False)

    tmp = json.loads(row[7])
    if len(tmp) == 0:
        tmp = ["", "", "", "", ""]
    else:
        for i in range(1, len(tmp)):
            if tmp[i][-2:] == "暂无":
                tmp[i] = ""
            else:
                if i == 1 or i == 3:
                    tmp[i] = tmp[i][6:]
                elif i == 2:
                    tmp[i] = tmp[i][8:]
                elif i == 4:
                    tmp[i] = tmp[i][9:]
    row[7] = json.dumps(tmp, ensure_ascii=False)


    tmp = json.loads(row[8])
    new_tmp = []
    half_len = len(tmp) // 2
    for i in range(0, half_len):
        if tmp[i] == "电话咨询：" and tmp[i + half_len][-8:] == "没有开通电话咨询":
            continue
        new_tmp.append(tmp[i][:-1])
    row[8] = json.dumps(new_tmp, ensure_ascii=False)

    tmp = json.loads(row[9])
    new_tmp = []
    new_line = []
    for line in tmp:
        new_line = []
        new_line.append(line[0])
        new_line.extend(re.sub(r"  +", " ", line[1].strip()).split(" "))
        for i in range(2, len(new_line)):
            if new_line[i][:2] == "挂号":
                new_line[i] = new_line[i][4:-1]
            elif new_line[i][:2] == "地点":
                new_line[i] = new_line[i][3:]

        new_tmp.append(new_line)
    row[9] = json.dumps(new_tmp, ensure_ascii=False)

    with open(DOCTORDSTPATH, "a+", encoding="utf-8") as f:
        fw = csv.writer(f, dialect="unix")
        fw.writerow(row)
    pass

def DocReadCsv():
    cnt = 0
    with open(DOCTORSRCPATH, "r", encoding="utf-8") as f:
        fr = csv.reader(f, dialect="unix")
        for row in fr:
            DocProcessALine(row)
    pass

if __name__ == "__main__":
    # print(0)
    DocReadCsv()
    pass
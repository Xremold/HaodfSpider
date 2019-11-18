from Settings import *
import json
import csv
import re
# from spider.Config import DebugPrint

def ProcessHospital(item):
    # DebugPrint(item)
    row = []
    row.append(item['name'])
    row.append(json.dumps(item['tag_list'], ensure_ascii=False))
    row.append(item['place'])
    row.append(json.dumps(item['dept_list'], ensure_ascii=False))
    row.append(json.dumps(item['score_list'], ensure_ascii=False))
    dept_score_dict = {}
    half_len = len(item['dept_score_dict']) // 2
    for i in range(0, half_len):
        dept_score_dict[item['dept_score_dict'][i]] = item['dept_score_dict'][i + half_len]
    row.append(json.dumps(dept_score_dict, ensure_ascii=False))
    with open(DstHosFilePath, 'a+', encoding='utf-8') as f:
        fw = csv.writer(f, dialect="unix")
        fw.writerow(row)
    pass

def ProcessDoctor(item):
    # DebugPrint(item)
    row = []
    row.append(item['name'])
    row.append(item['title_list'])
    row.extend([item['dept_name'], item['hos_name']])
    goodat = re.sub(r"[\n\t ]", "", item['goodat'])
    row.append(goodat)
    intro = "".join(item['intro'])
    intro = re.sub(r"[\n\t]", "", intro)
    intro = re.sub(r"\s+", " ", intro)
    row.append(intro)
    row.append(json.dumps(item['ifhaodf_list'], ensure_ascii=False))
    score_list = item['score_list']
    score_list[0] = score_list[0].replace(" ", "")
    row.append(json.dumps(score_list, ensure_ascii=False))
    row.append(json.dumps(item['online_service_list'], ensure_ascii=False))
    row.append(json.dumps(item['clinic_list'], ensure_ascii=False))
    sum_dict = {}
    half_len = len(item['sum_dict']) // 2
    for i in range(0, half_len):
        sum_dict[item['sum_dict'][i]] = item['sum_dict'][i + half_len][1:-1]
    row.append(json.dumps(sum_dict, ensure_ascii=False))

    row.append(json.dumps(item['ill_his_list'], ensure_ascii=False))
    with open(DstDocFilePath, "a+", encoding="utf-8") as f:
        fw = csv.writer(f, dialect="unix")
        fw.writerow(row)
    pass
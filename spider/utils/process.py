import json
from Config import *

def read_json():
    with open(ProcessFilePath, "r", encoding="utf-8") as f:
        obj = json.load(f)
        return obj['hospital_cnt'], obj['hospital_written'], obj['dept_cnt'], obj['doctor_cnt']

def finish_a_doctor():
    obj = {}
    with open(ProcessFilePath, "r", encoding='utf-8') as f:
        obj = json.load(f)
    obj['doctor_cnt'] += 1
    with open(ProcessFilePath, 'w', encoding='utf-8') as f:
        json.dump(obj, f)
    # DebugPrint("====doctor finished")
    
def finish_a_dept():
    obj = {}
    with open(ProcessFilePath, "r", encoding='utf-8') as f:
        obj = json.load(f)
    obj['dept_cnt'] += 1
    obj['doctor_cnt'] = 0
    with open(ProcessFilePath, 'w', encoding='utf-8') as f:
        json.dump(obj, f)
    # DebugPrint("======depart finished")

def finish_a_hospital():
    obj = {}
    with open(ProcessFilePath, "r", encoding='utf-8') as f:
        obj = json.load(f)
    obj['hospital_cnt'] += 1
    obj['dept_cnt'] = 0
    obj['doctor_cnt'] = 0
    obj['hospital_written'] = 0
    with open(ProcessFilePath, 'w', encoding='utf-8') as f:
        json.dump(obj, f)
    # DebugPrint("========hospital finished")

def write_a_hospital():
    obj = {}
    with open(ProcessFilePath, "r", encoding='utf-8') as f:
        obj = json.load(f)
    obj['hospital_written'] = 1
    with open(ProcessFilePath, 'w', encoding='utf-8') as f:
        json.dump(obj, f)
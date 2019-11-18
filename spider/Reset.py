from Settings import *
import json

if __name__ == "__main__":
    with open(DstDocFilePath, "w", encoding="utf-8") as f:
        f.truncate()
    with open(DstHosFilePath, "w", encoding="utf-8") as f:
        f.truncate()
    obj = {}
    with open(ProcessFilePath, "r", encoding="utf-8") as f:
        obj = json.load(f)
    obj['hospital_cnt'] = 0
    obj['hospital_written'] = 0
    obj['dept_cnt'] = 0
    obj['doctor_cnt'] = 0
    with open(ProcessFilePath, "w", encoding="utf-8") as f:
        json.dump(obj, f)
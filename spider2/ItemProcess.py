from Settings import DstExperiencePath, DstLetterPath, DebugPrint
import json
import csv
import re

'''
0:name, 1:hos_name, 2:dept_name, 3:time, 4:illness, 
5:now_state, 6:fee, 7:liaoxiao, 8:attitude, 9:comment
'''

def ProcessLetterPage(items):
    items = [item.values() for item in items]
    for item in items:
        item[3] = item[3][3:]
        item[4] = item[4].strip()
        item[6] = item[6].strip()
        item[9] = re.sub(r"\s+", "", "".join(item[9]))
    with open(DstLetterPath, "a", encoding="utf-8") as f:
        fw = csv.writer(f, dialect="unix")
        fw.writerows(items)
    pass

def ProcessExperiencePage(items):
    items = [item.values() for item in items]
    for item in items:
        item[3] = item[3][3:]
        item[4] = item[4].strip()
        item[6] = item[6].strip()
        item[9] = re.sub(r"\s+", "", "".join(item[9]))
    with open(DstExperiencePath, "a", encoding="utf-8") as f:
        fw = csv.writer(f, dialect="unix")
        fw.writerows(items)
    pass


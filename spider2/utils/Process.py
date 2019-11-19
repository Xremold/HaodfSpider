from Settings import ProcessFilePath, DebugPrint
import json

def ReadJson():
	with open(ProcessFilePath, "r", encoding="utf-8") as f:
		obj = json.load(f)
	return obj['doc_count'], obj['doc_experience_page'], obj['doc_letter_page']

def FinishADoctor():
	obj = {}
	with open(ProcessFilePath, "r", encoding="utf-8") as f:
		obj = json.load(f)
	obj['doc_count'] += 1
	obj['doc_experience_page'] = 0
	obj['doc_letter_page'] = 0
	with open(ProcessFilePath, "w", encoding="utf-8") as f:
		json.dump(obj, f, ensure_ascii=False)

def FinishADoctorExpPage():
	obj = {}
	with open(ProcessFilePath, "r", encoding="utf-8") as f:
		obj = json.load(f)
	obj['doc_experience_page'] += 1
	with open(ProcessFilePath, "w", encoding="utf-8") as f:
		json.dump(obj, f, ensure_ascii=False)

def FinishADoctorLetPage():
	obj = {}
	with open(ProcessFilePath, "r", encoding="utf-8") as f:
		obj = json.load(f)
	obj['doc_letter_page'] += 1
	with open(ProcessFilePath, "w", encoding="utf-8") as f:
		json.dump(obj, f, ensure_ascii=False)

def ResetJson():
	obj = {}
	obj['doc_count'] = 0
	obj['doc_experience_page'] = 0
	obj['doc_letter_page'] = 0
	with open(ProcessFilePath, "w", encoding="utf-8") as f:
		json.dump(obj, f, ensure_ascii=False)
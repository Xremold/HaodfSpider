from Settings import DoctorErrLog, LetterPageErrLog, ExperiencePageErrLog, SrcFilePath, RestoreExperiencePageErrLog, RestoreLetterPageErrLog

def LogDoctorErr(url, hos_name, dept_name):
    with open(DoctorErrLog, "a+", encoding="utf-8") as f:
        f.write(url+","+hos_name+","+dept_name+"\n")

def LogLetterPageErr(url, hos_name, dept_name, doc_name):
    with open(LetterPageErrLog, "a+", encoding="utf-8") as f:
        f.write(url+","+hos_name+","+dept_name+","+doc_name+"\n")

def LogExperiencePageErr(url, hos_name, dept_name, doc_name):
    with open(ExperiencePageErrLog, "a+", encoding="utf-8") as f:
        f.write(url+","+hos_name+","+dept_name+","+doc_name+"\n")


def PutDocErrToSrc():
    with open(SrcFilePath, "w", encoding="utf-8") as f:
        f.truncate()
    tmp = []
    with open(DoctorErrLog, "+", encoding="utf-8") as inf:
        tmp = inf.readlines()
        inf.truncate()
    with open(SrcFilePath, "w", encoding="utf-8") as outf:
        outf.writelines(tmp)

def RestoreLetterPageErr():
    tmp = []
    with open(LetterPageErrLog, "+", encoding="utf-8") as f:
        tmp = f.readlines()
        f.truncate()
    with open(RestoreLetterPageErrLog, "w", encoding="utf-8") as f:
        f.writelines(tmp)

def RestoreExperiencePageErr():
    tmp = []
    with open(ExperiencePageErrLog, "+", encoding="utf-8") as f:
        tmp = f.readlines()
        f.truncate()
    with open(RestoreExperiencePageErrLog, "w", encoding="utf-8") as f:
        f.writelines(tmp)

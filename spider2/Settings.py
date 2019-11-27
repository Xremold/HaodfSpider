# for Request.py
RandomUserAgent = True
ProxyEnabled = False
RequestDelay = 2

# for whole project
Debug = True
def DebugPrint(*objects, sep=' ', end='\n'):
    if Debug:
        print(*objects, sep=sep, end=end)

# for process.py
ProcessFilePath = "./utils/process.json"

# for Main.py and HandleErr
SrcFilePath = "./src/doctors_url.csv"

# for ItemProcess.py
DstLetterPath = "./dst/letter.csv"
DstExperiencePath = "./dst/experience.csv"

# for HandleErr.py
DoctorErrLog = "./logs/doctor_err.log"
LetterPageErrLog = "./logs/letter_page_err.log"
ExperiencePageErrLog = "./logs/experience_page_err.log"

# for HandleErr.py and Main.py
RestoreLetterPageErrLog = "./logs/letter_page_err2.log"
RestoreExperiencePageErrLog = "./logs/experience_page_err2.log"
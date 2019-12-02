DOCTORSRCPATH = "../spider/dst/doctor.csv"
DOCTORDSTPATH = "./final_data/doctor.csv"
HOSPITALSRCPATH = "../spider/dst/hospital.csv"

LETTERSRCPATH = "../spider2/dst/letter.csv"
# LETTERSRCPATH = "./test/test.csv"
EXPERIENCESRCPATH = "../spider2/dst/experience.csv"

LETTERDSTPATH = "./final_data/letter.csv"
# LETTERDSTPATH = "./test/test_dst.csv"
EXPERIENCEDSTPATH = "./final_data/experience.csv"

DEBUG = True

def DebugPrint(*objects, sep=' ', end='\n'):
    if DEBUG:
        print(*objects, sep=sep, end=end)
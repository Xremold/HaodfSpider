DOCTORSRCPATH = "../spider/dst/doctor.csv"
DOCTORDSTPATH = "./final_data/doctor.csv"
HOSPITALSRCPATH = "../spider/dst/hospital.csv"

DEBUG = True

def DebugPrint(*objects, sep=' ', end='\n'):
    if DEBUG:
        print(*objects, sep=sep, end=end)
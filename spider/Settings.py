RandomUserAgent = True
ProxyEnabled = False
RequestDelay = 2


Debug = True
ProcessFilePath = "./utils/process.json"
SrcFilePath = "./src/hospital_remains.csv"
DstHosFilePath = "./dst/hospital.csv"
DstDocFilePath = "./dst/doctor.csv"
DocErrLogPath = "./dst/docerrlog.txt"
HosErrLogPath = "./dst/hoserrlog.txt"

def DebugPrint(*objects, sep=' ', end='\n'):
    if Debug:
        print(*objects, sep=sep, end=end)

# DebugPrint("hhhh", ["jhh", "dd"], end="\n\n")
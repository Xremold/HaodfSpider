from Settings import DocErrLogPath, HosErrLogPath

def LogDocErr(url, hos_name, dept_name):
    with open(DocErrLogPath, "a+", encoding="utf-8") as f:
        f.write(url + "," +  hos_name + "," + dept_name + "\n")

def LogHosErr(url, hos_name):
    with open(HosErrLogPath, "a+", encoding="utf-8") as f:
        f.write(url + "," + hos_name + "\n")
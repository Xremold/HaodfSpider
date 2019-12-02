from settings import LETTERDSTPATH, LETTERSRCPATH, EXPERIENCEDSTPATH, EXPERIENCESRCPATH

def CheckDuplicate(line, file_path):
    flag = False
    with open(file_path, "r", encoding="utf-8") as f:
        while True:
            tmp = f.readline()
            if tmp == None or tmp == "" or tmp == "\n":
                break
            if tmp == line and not flag:
                # print("first find")
                flag = True
            elif tmp == line and flag:
                # print("second find")
                return True
    return False

if __name__ == "__main__":
    with open(LETTERSRCPATH, "r", encoding="utf-8") as inf, open(LETTERDSTPATH, "w", encoding="utf-8") as outf:
        while True:
            tmp = inf.readline()
            if tmp == None or tmp == "" or tmp == "\n":
                break
            if not CheckDuplicate(tmp, LETTERSRCPATH):
                outf.write(tmp)
    with open(EXPERIENCESRCPATH, "r", encoding="utf-8") as inf, open(EXPERIENCEDSTPATH, "w", encoding="utf-8") as outf:
        while True:
            tmp = inf.readline()
            if tmp == None or tmp == "" or tmp == "\n":
                break
            if not CheckDuplicate(tmp, EXPERIENCESRCPATH):
                outf.write(tmp)
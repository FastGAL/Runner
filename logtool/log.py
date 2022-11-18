import time
import os

time_file = time.time()
os.system("mkdir logs")#创建文件夹保平安
logfile = open("logs/log_" + str(time_file) + ".txt", "w+")


def logINFO(text):
    logfile.write("[INFO][" + str(time.time()) + "] " + str(text))
    print("[INFO][" + str(time.time()) + "] " + str(text))

def logWARN(text):
    logfile.write("[WARN][" + str(time.time()) + "] " + str(text))
    print("[WARN][" + str(time.time()) + "] " + str(text))

def logERR(text):
    logfile.write("[ERR][" + str(time.time()) + "] " + str(text))
    print("[ERR][" + str(time.time()) + "] " + str(text))
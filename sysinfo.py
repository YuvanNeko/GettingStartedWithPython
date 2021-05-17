import os
import time
def sysinfo():
    print(os.uname())
while True:
    sysinfo()
    time.sleep(2)
    
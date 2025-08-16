import sys
import numpy as np
import matplotlib.pyplot as plt
import csv
import fire

# def main(args: str, hoge: bool) -> None:
#     if hoge:
#         print(args)

# sample nnn.csv
# 2024-01-06,hh:mm:ss,PING,192.168.1.156,(192.168.1.156),56(84),bytes,of,data.
# 2024-01-06,22:53:48,41.1
# 2024-01-06,22:54:49,34.6
# 2024-01-06,22:54:49,34.8
# 2024-01-06,22:55:49,32.6
# 2024-01-06,22:55:59,33.4

# output
# CAM-DATE,TIME,Avr,MAX0.00,0
# hoge,22:53,41.10,41.1
# hoge,22:54,34.70,34.8
# hoge,22:55,33.00,33.4

float_format="{:.2f}"

class ping_info:
    def __init__(self):
        self.cnt=0
        self.avr = 0.0
        self.sum=0.0
        self.max = 0.0
    
    def printInf(self,strCam :str,strMinutes :str) :
        self.avr=self.sum/self.cnt
        outStr=strCam +","+ strMinutes + "," + float_format.format(self.avr)+ "," + str(self.max)
        print (outStr)

def main(args: str) -> None:
    print(args)

    # csvPath=args[1]
    csvPath="C:\work\TTP\Acecare\Ping_Log\py\csv\hoge.csv"
    strCam="hoge"
    
    with open(csvPath, newline='') as f:
        reader = csv.reader(f)
        rowData = list(reader)

    size=1
    cnt_row=1
    float_format="{:.2f}"
    pi = ping_info()
    # list piList = [ping_info]

    for row in rowData:
        #skip header
        if size == 1:
            size=size+1
            outStr="CAM-DATE,TIME,Avr,MAX" + float_format.format(pi.avr)+ "," + str(pi.max)
            print (outStr)
            continue
        else:
            size+=1

        # strDate=row[0]
        strMinutes=str(row[1])[0:5]
        ping=float(row[2])

        pi.sum = pi.sum + ping
        pi.cnt = pi.cnt + 1

        if(pi.max<ping):
            pi.max = ping

        #eof
        if (cnt_row == len(rowData)-1):
            pi.avr=pi.sum/pi.cnt
            outStr=strCam +","+ strMinutes + "," + float_format.format(pi.avr)+ "," + str(pi.max)
            print (outStr)
                    
        else:
            cnt_row = cnt_row+1
            rowNext = rowData[cnt_row]
            strMinutesNext=str(rowNext[1])[0:5]

        #next minutes
        if strMinutesNext == strMinutes:
            continue

        else:
            pi.printInf(strCam, strMinutes)
            # add list and new
            pi = ping_info()

    # print (cal_Avr_Ping_Minutes(strCam,))

# def cal_Avr_Ping_Minutes(cam:str, pi.avr, nextMinutes) -> str:
#     str_Line =  cam + "," + pi.avr
#     return str_Line

# def cal_Avr_Ping(cam:str, pi.avr) -> str:
#     str_Line =  cam + "," + pi.avr
#     return str_Line

if __name__ == "__main__":
    fire.Fire(main(sys.argv))   # これにするだけ

# # main
# if __name__=='__main__':
#     main(args)

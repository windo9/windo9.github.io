import numpy as np
import cv2
import csv

# Define the dimensions of the image
iHeight = 60
iWidth = 1440

# Create a black image with the specified dimensions
img = np.zeros((iHeight, iWidth, 3), np.uint8)

# Fill the entire image with a blue rowor
img[:, :] = (255, 255, 255)
img[0, :] = (0, 0, 0)
img[iHeight-1, :] = (0, 0, 0)

def main() -> None:
    csvPath='C:\\work\\TTP\\Acecare\\Ping_Log\\py\\mp4List20240202.csv'  
    strCAM='CAMxxxx'
    # strCAMnext=''

    with open(csvPath, newline='') as f:
        reader = csv.reader(f)
        # sorted(reader, key=lambda x: int(x[1]))
        rowData = list(reader)

    # file rayout
    # cam000005,20240118,000313,1
    # ~
    # cam000005,20240123,235402,0
    #sort by cam, date, time (asc)
    rowData.sort(key= lambda col: (col[0],col[1],col[2]))
    
    size=0
    idxStrDate:int=1
    idxIsEmpty:int=3

    for row in rowData:
        size=size+1
        
        strCAM=row[0]
        strDate=row[idxStrDate]
        hms=row[2]
        isEmpty:str=row[idxIsEmpty]

        xPlot:int=int(hms[0:2]) * 60 + int(hms[2:4])

        if isEmpty == '1':
            img[1:iHeight-1, xPlot] = (255, 0, 0)#plot ok blue

        else:
            img[1:iHeight-1, xPlot] = (0, 0, 255)#plot zero red

        #eof
        if (size == len(rowData)):
            # saveImg(img, strCAM, strDate) # skip last date
            pass
        
        else:
            strDateNext=rowData[size][idxStrDate]

        #next date
        if strDateNext == strDate:
            continue

        else:
            saveImg(img, strCAM, strDate)


def saveImg(img, strCAM, strDate)-> None:
    # csvPath='C:\work\TTP\Acecare\Ping_Log\py\mp4List20240202.csv'  
    imgPath= 'csv2bmp\\'+strCAM +'_'+ strDate + '.bmp'

    # #add plot H split
    for i in range (24):
        xPlot=i*60
        if i>0 :
            img[0:4, xPlot] = (0, 0, 0)
            img[0:2, xPlot-1] = (0, 0, 0)

    cv2.imwrite(imgPath, img)  

    img[:, :] = (255, 255, 255)
    img[0, :] = (0, 0, 0)
    img[iHeight-1, :] = (0, 0, 0)

# main
if __name__=='__main__':
    main()



#test data     
# CAM002_20240125_000000.mp4,1
# CAM002_20240125_002011.mp4,1
# CAM002_20240125_022611.mp4,0
# CAM002_20240125_235911.mp4,0


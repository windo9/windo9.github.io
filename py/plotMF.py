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
    csvPath='C:\work\TTP\Acecare\Ping_Log\py\mp4List.csv'  
    strCAM='CAMxxxx'
    # strCAMnext=''

    with open(csvPath, newline='') as f:
        reader = csv.reader(f)
        rowData = list(reader)
        
    size=0
    for row in rowData:
        # row -> "./cam000005/20240104/00/cam000005_20240104_000229.mp4"
        size=size+1
        spl=row[0].split('_') 
        strCAM=spl[0]
        strDate=spl[1]
        hms=spl[2].replace('mp4','')
        mins = int(hms[0:2]) * 60 + int(hms[2:4])
        xPlot=mins

        isEmpty=row[1]
        if isEmpty == '1':
            img[1:iHeight-1, xPlot] = (255, 0, 0)#plot ok blue

        else:
            img[1:iHeight-1, xPlot] = (0, 0, 255)#plot zero red

        #eof
        if (size == len(rowData)):
            saveImg(img, strCAM, strDate)
        
        else:
            splNext = rowData[size][0].split('_') 
            strDateNext= splNext[1]

        #next date
        if strDateNext == strDate:
            continue

        else:
            saveImg(img, strCAM, strDate)        
            # Fill the entire image with a blue rowor
            # img[:, :] = (255, 255, 255)
            # img[0, :] = (0, 0, 0)
            # img[iHeight-1, :] = (0, 0, 0)
        
            # #next cam
            # if strCAMnext == strCAM:
            #     continue
            # else:
            #     imgPath= 'img/'+strCAM + strDate + '.bmp'  
            #     cv2.imwrite(imgPath, img)         
            #     # Fill the entire image with a blue rowor
            #     img[:, :] = (255, 255, 255)
            #     img[0, :] = (0, 0, 0)
            #     img[iHeight-1, :] = (0, 0, 0)


def saveImg(img, strCAM, strDate)-> None:
    imgPath= 'img/'+strCAM +'-'+ strDate + '.bmp'

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
# CAM001_20240125_001011.mp4,1
# CAM001_20240125_001511.mp4,0
# CAM001_20240125_011511.mp4,1
# CAM001_20240125_235911.mp4,1
# CAM002_20240125_000000.mp4,1
# CAM002_20240125_002011.mp4,1
# CAM002_20240125_022611.mp4,0
# CAM002_20240125_235911.mp4,0


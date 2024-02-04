
#ライブラリの読み込み
import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt
# import pandas as pd
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
    args = sys.argv
    print(args)
  
    csvPath='mp4List.csv'  # csv0Path='mp4List0.csv'
    strCAM='CAMxxxx'
    strCAMnext=''

    # panda=pd.read_csv(csvPath,header=0)
    with open(csvPath, newline='') as f:
        reader = csv.reader(f)
        rowData = list(reader)
        
    size=0
    for row in rowData:
        size=size+1
        spl=row[0].split('_') 
        strCAM=spl[0]
        strDate=spl[1]
        hms=spl[2].replace('mp4','')
        mins = int(hms[0:2]) * 60 + int(hms[2:4])
        xPlot=mins

        isEmpty=row[1]
        if isEmpty == '1':
            img[0:iHeight-1, xPlot] = (255, 0, 0)#plot ok blue
            if xPlot < iWidth-1:
                img[:, xPlot+1] = (255, 0, 0)#plot ok blue
            else:
                img[:, xPlot-1] = (255, 0, 0)#plot ok blue

        else:
            img[0:iHeight, xPlot] = (0, 0, 255)#plot zero red
            if xPlot < iWidth-1:
                img[:, xPlot+1] = (0, 0, 255)#plot zero red
            else:
                img[:, xPlot-1] = (0, 0, 255)#plot zero red

        if (size == len(rowData)):
            imgPath= 'img/'+strCAM + strDate + '.bmp'  
            cv2.imwrite(imgPath, img)
        
        else:
            splNext = rowData[size][0].split('_') 
            strCAMnext = splNext[0]

        if strCAMnext == strCAM:
            continue
        else:
            imgPath= 'img/'+strCAM + strDate + '.bmp'  
            cv2.imwrite(imgPath, img)         
            # Fill the entire image with a blue rowor
            img[:, :] = (255, 255, 255)
            img[0, :] = (0, 0, 0)
            img[iHeight-1, :] = (0, 0, 0)

    # panda=pd.read_csv(csv0Path,header=0)

    # for row in panda.rowumns:
    #     spl=row.split('_') 
    #     strCAM=spl[0]
    #     hms=spl[2].replace('mp4','')
    #     mins = int(hms[0:2]) * 60 + int(hms[2:4])
    #     xPlot=mins
    #     img[0:iHeight, xPlot] = (0, 0, 255)#plot zero red
    
    # Display the image
    # cv2.imshow("image", img)
    # strDate = '20240125'

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

import numpy as np
import cv2

# confirm paths are for directories or files
from os import path
# find all directories
from os import listdir



# files
# find all object folders
# print("these are all the filenames in Elena.dir: {}".format(listdir('images/')))


#########
## Get list of Dirs and images
#########

# scores for each object
objScores = []

## get object directories
raw_objDirs = listdir('images/')
objDirs = []

for i in raw_objDirs:
    if path.isdir('images/'+i): 
        # print("it's true: {}".format('images/'+i))
        objDirs.append(i)
        objScores.append(0) # populate objscores with tmp values
    # else:
        # print("it's not true: {}".format('images/'+i))

## find all images in each objects dir
imgList = []

for x in objDirs:
    objImgs = listdir('images/'  + x)
    # print("This is the objDir: {}".format("images/" + x))

    row = []
    for y in objImgs:
        if path.isfile('images/'+ x + '/' + y): 
            # print("it's true: {}".format('images/'+ x + '/' + y))
            row.append('images/'+ x + '/' + y)
        # else:
            # print("it's not true: {}".format('images/'+ x + '/' + y))
    imgList.append(row)

cnt =0
for i in imgList:
    print("List {}".format(imgList[cnt]))
    cnt +=1



###########
### Display/Navigate images
###########
dirCnt = 0 # current dir position
imgCnt = 0 # current image position
dirSize = len(objDirs) # number of objects 
imgSize = [] # list with number of images in each dir

cnt = 0
for i in imgList:
    imgSize.append(len(imgList[cnt]))
    cnt+=1
print("this is the imgSize: {}".format(imgSize))


cv2.namedWindow("main", cv2.WINDOW_AUTOSIZE)
while(True):
    k = cv2.waitKey(0)
    print(k)

    if k == 63232:
        print("cycling up, imgCnt: {}, ImgSize: {} ".format(imgCnt, imgSize[dirCnt]))
        if imgCnt+1 < imgSize[dirCnt]:
            imgCnt +=1
        else:
            imgCnt = 0
    # elif k == 63235:
    #     print("left")
    # elif k == 63234:
    #     print("right")
    elif k == 13:
        print("the answer is..")
        k = cv2.waitKey(0)
        if k == 121: # if 'y' is pressed increment point for object
            objScores[dirCnt]+=1
            print("your score stands at: {}".format(objScores))
        if dirCnt+1 < dirSize:
            dirCnt+=1
        else: 
            dirCnt = 0

    elif k == 27 or k == 113: #if q or esc is pressed then exit
        print("exiting")
        break

    # read in the file and display
    img = cv2.imread(imgList[dirCnt][imgCnt],1)

    cv2.namedWindow("main", cv2.WINDOW_AUTOSIZE)
    cv2.resizeWindow("main", 1000, 1000)

    # roughly put window in the middle of the screen
    cv2.moveWindow("main", 400, 200)

    # input the resizing values  
    img2 = cv2.resize(img, (int(img.shape[1]/10),int(img.shape[0]/10)))
    print("This is the first: {} and second: {} values ".format(img2.shape[0], img2.shape[1]))
    cv2.imshow("main",img2)



    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
        break

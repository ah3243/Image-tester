
import numpy as np
import cv2

# confirm paths are for directories or files
from os import path
# find all directories
from os import listdir

#########
## Get list of Dirs and images
#########

## get object directories
raw_objDirs = listdir('images/')
objDirs = []

for i in raw_objDirs:
    if path.isdir('images/'+i): 
        objDirs.append(i)

## find all images in each objects dir
imgList = []

for x in objDirs:
    objImgs = listdir('images/'  + x)

    row = []
    for y in objImgs:
        if path.isfile('images/'+ x + '/' + y): 
            row.append('images/'+ x + '/' + y)
    imgList.append(row)

cnt =0
for i in imgList:
    print("List {}".format(imgList[cnt]))
    cnt +=1

#########
## Get any saved scores
#########
saveFilePath = 'saved.txt'
# cached scores
scores = {}


if path.isfile(saveFilePath)== False or path.getsize(saveFilePath)==0:
    print("no save file found generating new one")
    f = open(saveFilePath, 'w')
    tmpVals = ""
    for i in objDirs:
        tmpVals += str(i + "\n" + "0" + "\n")
    f.write(tmpVals)
    f.close()

f = open(saveFilePath, 'r')
tmp = f.read()
objScos = tmp.split('\n')

cnt =0
tmpList = []

for i in objScos:

    #filter out the key
    if cnt%2==False:
        tmpList = []
        tmpList.append(objScos[cnt])

    # filter out the value
    else: 
        tmpList.append(objScos[cnt])
        scores[tmpList[0]] = tmpList[1]

    cnt +=1
print("The previously saved scores: {}".format(scores))
f.close()


###########
### Vars for navigation/display
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
    ###########
    ## read in the file and display
    ###########

    img = cv2.imread(imgList[dirCnt][imgCnt],1)

    cv2.namedWindow("main", cv2.WINDOW_AUTOSIZE)
    cv2.resizeWindow("main", 1000, 1000)

    # roughly put window in the middle of the screen
    cv2.moveWindow("main", 400, 200)

    # input the resizing values  
    img2 = cv2.resize(img, (int(img.shape[1]/10),int(img.shape[0]/10)))
    cv2.imshow("main",img2)


    ##########
    ## get keyboard input
    ##########
    k = cv2.waitKey(0)

    # if the uparrow is pressed then cycle through images for specific object
    if k == 63232:
        if imgCnt+1 < imgSize[dirCnt]:
            imgCnt +=1
        else:
            imgCnt = 0

    elif k == 13:
        ## show the answer
        print("the answer is..: {}".format(objDirs[dirCnt]))
        nameReveal = np.zeros((500,500,3), np.uint8)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(nameReveal,objDirs[dirCnt],(2,250), font, 4,(255,255,255),2,cv2.LINE_AA)
        cv2.imshow("main", nameReveal) 
        k = cv2.waitKey(0)

        # if 'y' is pressed(answered correctly) increment point for object
        if k == 121: 
            tmp = int(scores[objDirs[dirCnt]])+1
            print("This is tmp: {}".format(tmp))
            scores[objDirs[dirCnt]]= tmp

            print("your score stands at: {}".format(scores))
        if dirCnt+1 < dirSize:
            dirCnt+=1
        else: 
            dirCnt = 0

    elif k == 27 or k == 113: #if q or esc is pressed then exit
        print("Saving results..")
        
        f = open(saveFilePath, 'w')
        tmpStr = ""
        for i in scores:
            print("This is i: {}".format(i))
            tmpStr +=str(str(i) + '\n' + str(scores[i]) + '\n')
        print("This is the resutls: \n{}".format(tmpStr))
        f.write(tmpStr)
        f.close()

        print("exiting")
        cv2.destroyAllWindows()
        break

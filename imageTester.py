
import numpy as np
import cv2

# find all directories
from os import listdir

# create display window


# find all object folders
print("these are all the filenames in Elena.dir: {}".format(listdir('images/Elena')))

# find all images of specific objects


while(True):
    cv2.namedWindow("main", cv2.WINDOW_AUTOSIZE)
    k = cv2.waitKey(0)
    print(k)

    if k == 63232:
        print("the up key")
    elif k == 63233:
        print("the down key")
    elif k == 13:
        print("the answer is..")
    elif k == 27:
        break

    # # read in the file and display
    # img = cv2.imread('images/Bob/bob3.jpg',1)

    # cv2.namedWindow("main", cv2.WINDOW_AUTOSIZE)
    # cv2.resizeWindow("main", 1000, 1000)

    # # roughly put window in the middle of the screen
    # cv2.moveWindow("main", 400, 200)

    # # input the resizing values  
    # img2 = cv2.resize(img, (int(img.shape[1]/10),int(img.shape[0]/10)))
    # print("This is the first: {} and second: {} values ".format(img2.shape[0], img2.shape[1]))
    # cv2.imshow("main",img2)



    # k = cv2.waitKey(0)
    # if k == 27:         # wait for ESC key to exit
    #     cv2.destroyAllWindows()
    #     break

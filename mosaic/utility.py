import cv2
import numpy as np


def writeImage():
    FILENAME = 'images/image1.jpeg'
    image = cv2.imread(FILENAME)
    cv2.imwrite('write.jpeg', image)


def overlayImages():
    FILENAME1 = '../images/image3.jpeg'
    FILENAME2 = '../images/image4.jpeg'

    image1 = cv2.imread(FILENAME1)
    image2 = cv2.imread(FILENAME2)

    result = cv2.addWeighted(image1, 0.4, image2, 1, 0)

    cv2.imshow('overlay', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
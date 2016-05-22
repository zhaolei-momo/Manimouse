# code to read an image, show it and write it in the directory with different name

import numpy as np
import cv2

img=cv2.imread('sample1.jpeg',0)	#reading image in grayscale

cv2.imshow('result',img)
k=cv2.waitKey(0)

if k==27:
	cv2.closeAllWindows()

elif k==ord('s'):
	cv2.imwrite('result_samle1.jpeg',img)
	cv2.closeAllWindows()
	

# code to read an image, show it and write it in the directory with different name

import numpy as np
import cv2

img=cv2.imread('sample1.jpeg',0)	#reading image in grayscale, 0 indicates grayscale version

cv2.imshow('result',img)
k=cv2.waitKey(0)					# k is used to get the input key from the user

if k==27:							# k=27 represents user pressing the ESC key. The program simply terminates in this case.
	cv2.closeAllWindows()

elif k==ord('s'):					# k=ord('s') represents user presiing the 's' key. In this case the grayscale version is saved before program exits.
	cv2.imwrite('result_samle1.jpeg',img)
	cv2.closeAllWindows()
	

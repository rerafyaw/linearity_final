import numpy as np
import cv2
import csv

def qr2binary():
	img = cv2.imread('QR.jpg',0) 
	ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

	i = 0
	while img[i,i] == 255:
		i+=1
		initpx = img[i,i]
	j = i
	while img[j,j] == 0:
		j+=1

	box_size = j-i

	height, width = img.shape

	img = img[i:height - i, i:width - i]
	M_height = len(img)/box_size
	M_width = len(img[0])/box_size
	M = np.zeros(shape = (M_width, M_height))
	center = box_size/2
	for i in range(M_height):
		for j in range(M_width):
			if img[center+ i*box_size, center + j*box_size] == 0:
				M[i,j] = 1
	print M

	with open("output.csv", "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(M)

	cv2.imshow('binary', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	qr2binary()

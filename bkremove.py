import numpy as np
import cv2
import glob
import os
import time
import sys
from threading import Thread

debug = 0
colorspace = '1'

def	elabora(file):
	src = cv2.imread(file)

	# cartoonizzo un po' 
	if colorspace == '1':
		img = cv2.medianBlur(src, 5)
	else:
		if colorspace == '2':
			img = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
			img = cv2.medianBlur(img, 5)
		else:
			img = cv2.cvtColor(src, cv2.COLOR_BGR2HLS)
			img = cv2.medianBlur(img, 5)
	
	# aggiungo i bordi
	#cny = cv2.cvtColor(cv2.Canny(img, 10, 200), cv2.COLOR_GRAY2BGR)
	#img = img + cny
	
	h, w = img.shape[:2]
	if debug:
		print w, h
		print colorspace
		orig = img.copy()
	
	# creo marker
	marker = np.zeros((h, w), dtype=int)

	size = 10
	offset = 5
	
	for i in range (h / 2 - size, h / 2 + size):
		for j in range (w / 2 - size, w / 2 + size):
			marker[i][j] = 2

	for i in range(size):
		for j in range(size):
			marker[offset + i][offset + j] = 1
			marker[h - size - offset + i][offset + j] = 1
			marker[h - size - offset + i][w - size - offset + j] = 1
			marker[offset + i][w - size - offset + j] = 1
			
			marker[h / 2 - size / 2 + i][offset + j] = 1
			marker[h / 2 - size / 2 + i][w - size - offset + j] = 1
			

	# segmentazione con watershed
	cv2.watershed(img, marker)

	src[marker == 1] = [0, 0, 0]
	
	if debug:
		#mostro risultati
		cv2.imshow('image', src)
		cv2.imshow('image1', orig)
		#cv2.imshow('canny', cny)
		if (cv2.waitKey(0) & 0xff) == 27:
			quit()
		cv2.destroyAllWindows()
	else:
		# salvo immagini
		name, ext = os.path.splitext(file)
		name1 = name + '_out' + '.png'
		cv2.imwrite(name1, src)

# leggo directory

if len(sys.argv) < 2:
	print "usage: bkremove imagedir [colorspace]"
	print "example: bkremove c:\test\images"
	print "colorspaces are 1: rgb, 2:HSV, 3:HLS"
	quit()

if len(sys.argv) == 3:
	colorspace = sys.argv[2]
	
dir = sys.argv[1] + '/*.jpg'
files = glob.glob(dir)
start = time.time()

for file in files:
	if debug:
		print file
		elabora(file)
	else:
		t = Thread(target=elabora, args=(file,))
		t.start()
	
end = time.time()
print  "total time: %f" % (end - start)

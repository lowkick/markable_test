import numpy as np
import cv2
import glob
import os
import time
import sys
from threading import Thread

debug = 0

def	elabora(file):
	src = cv2.imread(file)
	
	# cartoonizzo un po' 
	img = cv2.medianBlur(src, 5)
	
	h, w = img.shape[:2]
	if debug:
		print w, h
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
		if (cv2.waitKey(0) & 0xff) == 27:
			quit()
		cv2.destroyAllWindows()
	else:
		# salvo immagini
		name, ext = os.path.splitext(file)
		name1 = name + '_out' + '.png'
		cv2.imwrite(name1, src)

# leggo directory

if len(sys.argv) != 2:
	print "usage: bkremove imagedir"
	print "example: bkremove c:\test\images"
	quit()

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

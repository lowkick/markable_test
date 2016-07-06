import numpy as np
import cv2
import glob
import os
import time
from threading import Thread

def	elabora(file):
	src = cv2.imread(file)
	
	# cartoonizzo un po' 
	img = cv2.medianBlur(src, 5)
	
	#orig = img.copy()
	w, h = img.shape[:2]

	# creo marker
	marker = np.zeros((w, h), dtype=int)

	size = 10
	offset = 5
	
	for i in range (w / 2 - size, w / 2 + size):
		for j in range (h / 2 - size, h / 2 + size):
			marker[i][j] = 2

	for i in range(size):
		for j in range(size):
			marker[offset + i][offset + j] = 1
			marker[w - size - offset + i][offset + j] = 1
			marker[w - size - offset + i][h - size - offset + j] = 1
			marker[offset + i][h - size - offset + j] = 1

	# segmentazione con watershed
	cv2.watershed(img, marker)

	src[marker == 1] = [0, 0, 0]
		
	# mostro risultati
	#cv2.imshow('image', src)
	#cv2.imshow('image1', orig)
	#if (cv2.waitKey(0) & 0xff) == 27:
	#	quit()
	#cv2.destroyAllWindows()
	
	# salvo immagini
	name, ext = os.path.splitext(file)
	name1 = name + '_out' + '.png'
	cv2.imwrite(name1, img)



files = glob.glob('images/*.jpg')
start = time.time()

for file in files:
	#elabora(file)
	t = Thread(target=elabora, args=(file,))
	t.start()
	
end = time.time()
print  "total time: %f" % (end - start)
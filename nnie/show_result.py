import cv2
import sys,os
img_name = sys.argv[1]
while(True):
	img = cv2.imread(img_name)
	resized = cv2.resize(img, (416,416))
	contxt = open('det_result.txt')
	line = contxt.readline()
	while(line != ''):
	    bbox = line.split('\n')[0]
	    print(bbox)
	    coords = bbox.split(' ')
	    cv2.rectangle(resized, (int(coords[0]),int(coords[1])), (int(coords[2]), int(coords[3])), (255,0,0), 1)
	    line = contxt.readline()
	cv2.imshow('test', resized)
	cv2.waitKey(100)
	contxt.close()

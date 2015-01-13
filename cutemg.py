import subprocess as sp
import numpy
import matplotlib.pyplot as plt
import cv2

FFMPEG_BIN = "ffmpeg"
command = [ FFMPEG_BIN,
            '-i', 'demo.mp4',
            '-f', 'image2pipe',
            '-pix_fmt', 'rgb24',
            '-vcodec', 'rawvideo', '-']
pipe = sp.Popen(command, stdout = sp.PIPE, stderr=sp.PIPE, bufsize=10**8)
print pipe

# raw_image = pipe.stdout.read(1280*720*3)
# # transform the byte read into a numpy array
# image =  numpy.fromstring(raw_image, dtype='uint8')
# image = image.reshape((720,1280,3))
# print image
# # throw away the data in the pipe's buffer.
# pipe.stdout.flush()
while(1):

	img=pipe.stdout.read(1280*720*3)
	#print len(img)
	if (len(img)==1280*720*3):
		imgshow=numpy.fromstring(img,dtype='uint8')		
		imgshow=imgshow.reshape(720,1280,3)
		cv2.imshow('window',imgshow)
		cv2.waitKey(1)
	else:
		print 'end of file, exit'
		break

print 'done...'
print stdout




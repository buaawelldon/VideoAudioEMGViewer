def main():
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

	command_aud = [ FFMPEG_BIN,
	        '-i', 'demo.mp4',
	        '-f', 's16le',
	        '-acodec', 'pcm_s16le',
	        '-ar', '44100', # ouput will have 44100 Hz
	        '-ac', '2', # stereo (set to '1' for mono)
	        '-']
	pipe_aud = sp.Popen(command_aud, stdout=sp.PIPE,stderr=sp.PIPE, bufsize=10**8)

	while(1):
		img=pipe.stdout.read(1280*720*3)
		#print len(img)
		if (len(img)==1280*720*3):
			imgshow=numpy.fromstring(img,dtype='uint8')		
			imgshow=imgshow.reshape(720,1280,3)
			#cv2.imshow('window',imgshow)
			#cv2.waitKey(1)
		else:
			print 'end of file, exit'
			break
	raw_audio = pipe_aud.stdout.read(88200*4)

	# Reorganize raw_audio as a Numpy array with two-columns (1 per channel)
	
	audio_array = numpy.fromstring(raw_audio, dtype="int16")
	audio_array = audio_array.reshape((len(audio_array)/2,2))
	print audio_array.shape


	print 'done...'
if __name__ == '__main__':
	main()




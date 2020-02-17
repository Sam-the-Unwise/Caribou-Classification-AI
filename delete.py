#!/usr/bin/env python
import os
import shutil
# this is just an example of the address
image_file = '/Users/qiaoshuyue/Desktop/text' #Please write the right address of where the images are saved 
if os.path.exists(image_file):

	shutil.rmtree(image_file)
	os.mkdir(image_file)   
else:
    print 'no such file:%s'%image_file 
#! /usr/bin/python
import os
import time
from stat import ST_MODE, S_ISDIR
import shutil

dir = "/home/epicpi/Downloads/"#working directory
delTime = 600000 #how old file must be before being deleted

print "Deleting old files from " + dir

for filename in os.listdir(dir):
	info = os.stat(dir+filename)
	if time.time() - info.st_atime > delTime:
		if S_ISDIR(info[ST_MODE]):
			shutil.rmtree(dir+filename, ignore_errors=False, onerror=None)
		else:
			os.remove(dir+filename)
		print "deleted " + filename


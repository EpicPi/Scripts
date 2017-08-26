#! /usr/bin/python
print('Screen Capture Initiated') # captures pages of an online resource and converts to a pdf

from pymouse import PyMouse
import pyscreenshot as ImageGrab
from fpdf import FPDF
from PIL import Image
import os
import time

dir = "/home/epicpi/" #working directory for this capture
x = 0
pages = 243
wait = 4

#captures first image and sizes the pdf pages accordingly
im=ImageGrab.grab(bbox=(1620,24,2646,1280)) # X1,Y1,X2,Y2
im.save(dir+"im.png")
cover = Image.open(dir+"im.png")
width, height = cover.size

pdf = FPDF(unit = "pt", format = [width, height])
m = PyMouse()

 
while x < pages:
	x += 1
	m.click(2151,0)#location of next page button

	time.sleep(wait)
	
	#grab screenshot of the page and store to png
	im=ImageGrab.grab(bbox=(1620,24,2646,1280)) # X1,Y1,X2,Y2
	im.save(dir+"im"+str(x)+".png")

	#add to pdf
	pdf.add_page()
	pdf.image(dir + "im"+str(x)+".png", 0, 0)
	
	#remove the saved png
	os.remove(dir+"im"+str(x)+".png")
	time.sleep(.1)

	print(x)
	pass

pdf.output(dir + 'book' + ".pdf", "F")#compile the pdf


# Import required libraries
from PIL import Image
import numpy as np
#import board
#import neopixel
import matplotlib.pyplot as plt

#pixels = neopixel.Neopixel(board.D18, 121, brightness = 0.2, auto_write=False, pixel_order=RGBW)

def reshape(image, x, y):
	small_img=image.resize((11, 12),Image.BILINEAR)
	#resize
	o_size=(1000,1000) #output size
	#display image
	res=small_img.resize(o_size,Image.NEAREST)
	plt.imshow(res)
	plt.show()
	return small_img

#def extractRGB(image):
#	image = small_img.convert('RGB')
#	width = image.size[0] #define W and H
#	height = image.size[1]
#	for y in range(0, height): #each pixel has coordinates
#        	row = ""
#        	for x in range(0, width):
#			RGB = image.getpixel((x,y))
#                	R,G,B = RGB  #now you can use the RGB value
#                	print(R, G, B)

def imageToLED(image, r, g, b):

	for i in range(0, len(r)-1):
		r[i] = int(float(r[i]))
		b[i] = int(float(b[i]))
		g[i] = int(float(g[i]))
	
	for l in range(5):
        	for m in range(6):
            		temp1 = r[24*l+12+m]
            		r[24*l+12+m] = r[24*l+23-m]
            		r[24*l+23-m] = temp1
	for l in range(5):
        	for m in range(6):
            		temp1 = g[24*l+12+m]
            		g[24*l+12+m] = g[24*l+23-m]
            		g[24*l+23-m] = temp1
	for l in range(5):
            for m in range(6):
                    temp1 = b[24*l+12+m]
                    b[24*l+12+m] = b[24*l+23-m]
                    b[24*l+23-m] = temp1
	return (r, g, b)

#Parameters
numNeopixels_x = 12 #Declare number of Neopixels in grid
numNeopixels_y = 11

#while(1):
image = Image.open('batman.png')
plt.imshow(image)
plt.show()
resizedImage = reshape(image, numNeopixels_x, numNeopixels_y)
#pixels = extractRGB(resizedImage)

image = resizedImage.convert('RGB')
width = image.size[0] #define W and H
height = image.size[1]

r = []
b = []
g = []

for y in range(0, height): #each pixel has coordinates
	row = ""
	for x in range(0, width):
		RGB = image.getpixel((x,y))
		R,G,B = RGB
		r.append(R)
		b.append(B)
		g.append(G)

pixels = imageToLED(resizedImage, r, g, b) #Convert the image to an LED value array and assign them to the string of Neopixels
print(pixels)
pixels.show() #Light up the LEDs

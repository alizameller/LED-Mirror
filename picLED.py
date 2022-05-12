# Displays an image to 11x12 matrix of LEDs
# Import required libraries
from PIL import Image
import numpy as np
import board
import neopixel
import matplotlib.pyplot as plt

pixels = neopixel.Neopixel(board.D18, 132, brightness = 0.2, auto_write=False, pixel_order = neopixel.GRBW)

def reshape(image, x, y):
  small_img = image.resize((12, 11), Image.BILINEAR)
  #resize
  o_size = (1000, 1000) #output size
  #display image
  res = small_img.resize(o_size, Image.NEAREST)
  return small_img
  
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
image  = Image.open('inputfiles/rgbcircle.jpeg') #specify Image file name (include path if not located in current directory)
resizedImage = reshape(image, numNeopixels_x, numNeopixels_y)
  
image = resizedImage.convert('RGB')
print(image)
width = image.size[0]
height = image.size[1]
  
r = []
g = []
b = []
  
for y in range(0, height):
  row = ""
  for x in range(0, width):
    RGB = image.getpixel((x,y))
    R,G,B = RGB
    r.append(R)
    b.append(B)
    g.append(G)
  
(r, g, b) = imageToLed(resizedImage, r, g, b)
print(type(r))
for i in range(132):
  pixels[i] = (r[i], g[i], b[i])
print(pixels)
pixels.show() 

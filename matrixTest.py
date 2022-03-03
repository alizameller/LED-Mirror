import time
import board
import neopixel

pixels = neopixel.Neopixel(board.D18, 121, brightness = 0.2, auto_write=False, pixel_order=RGBW)

with open("R.txt", "r") as Rfile:
with open("G.txt", "r") as Gfile:
with open("B.txt", "r") as Bfile:

i = 0
j = 0
k = 0

#intilize all arrays R,G,B with size 132 to zero 
red=[]
red = [0 for i in range(132)] 
green=[]
green = [0 for i in range(132)] 
blue=[]
blue = [0 for i in range(132)] 
# will varibles R,G,B be considered an int or float 
for line in Rfile:
        R = {}.format(line.strip())
        #convert to int for simplicity R,G,B
        red[i] = int(R)
        i = i + 1
for line in Gfile:
        G = {}.format(line.strip())
        green[j] = int(G)
        j = j + 1
for line in Bfile:
        B = {}.format(line.strip())
        blue[k] =  int(B)
        k = k + 1
# test code to print out what a value of the neopixels would be
for a in range(132):
        print("neoPixel[",a,"] = (",red[a],",",green[a], ",",blue[a],")")

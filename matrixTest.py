import time
import board
import neopixel

pixels = neopixel.Neopixel(board.D18, 121, brightness = 0.2, auto_write=False, pixel_order=RGBW)

with open("R.txt", "r") as Rfile, open("G.txt", "r") as Gfile, open("B.txt", "r") as Bfile:
	i = 0
	j = 0
	k = 0
	temp1 = [0]

	R = open("R.txt").read().split('\n')
	for i in range(0, len(R)-1):
		R[i] = int(float(R[i]))

	for l in range(5):
		for m in range(6):
			temp1 = R[24*l+12+m]
			R[24*l+12+m] = R[24*l+23-m]
			R[24*l+23-m] = temp1


	G = open("G.txt").read().split('\n')
	for j in range(0, len(G)-1):
		G[i] = int(float(G[i]))

	for l in range(5):
		for m in range(6):
			temp1 = G[24*l+12+m]
			G[24*l+12+m] = G[24*l+23-m]
			G[24*l+23-m] = temp1

	B = open("B.txt").read().split('\n')
	for k in range(0, len(B)-1):
		B[i] = int(float(B[i]))

	for l in range(5):
		for m in range(6):
			temp1 = B[24*l+12+m]
			B[24*l+12+m] = B[24*l+23-m]
			B[24*l+23-m] = temp1

	for l in range(132):
		print(R[l], G[l], B[l])
		r = R[l]
		g = G[l]
		b = B[l]
		pixels[l] = (r, g, b)
	pixels.show() 

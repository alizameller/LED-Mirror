import cv2
import matplotlib.pyplot as plt
import numpy
import PIL

def grab_frame(cap):
    ret,frame = cap.read()
    return cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

def resize_image(array):
    #check if array is correct
    print(array)

    #percent by which the image is resized
    #scale_percent = 7

    #calculate the 50 percent of original dimensions
    #width = int(array.shape[1] * scale_percent / 100)
    #height = int(array.shape[0] * scale_percent / 100)

    # dsize
    dsize = (64, 84)

    return cv2.resize(array, dsize)

#Initiate the camera
cap1 = cv2.VideoCapture(0)

a = numpy.random.rand(64, 84)

plt.ion()

#create image plot
im1 = plt.imshow(a, interpolation='nearest')

while True:
    #get image array
    array = numpy.asarray(grab_frame(cap1))
    resize = resize_image(array)

    im1.set_data(resize)
    plt.pause(0.2)

plt.ioff() #due to infinite loop, this gets never called.
plt.show()
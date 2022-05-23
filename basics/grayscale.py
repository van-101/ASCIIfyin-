from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np


input_image= imread("gangs-of-wasseypur.jpg")
r,g,b=input_image[:,:,0],input_image[:,:,1],input_image[:,:,2]

gamma=0.45

rc,gc,bc=0.2126,0.7152,0.0722

grayscale_image= rc*(r**gamma) + gc*(g**gamma) + bc*(b**gamma)

fig=plt.figure(1)
img1,img2=fig.add_subplot(121), fig.add_subplot(122)

img1.imshow(input_image)
img2.imshow(grayscale_image, cmap=plt.cm.get_cmap('gray'))

fig.show()
plt.show()

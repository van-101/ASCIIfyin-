import cv2
import os
from natsort import natsorted, realsorted as ns


image_folder='data'
files=os.listdir(image_folder)
new=natsorted(files)
video_name='asciify.avi'

images=[img for img in new if img.endswith(".jpg")]
frame=cv2.imread(os.path.join(image_folder,images[0]))
height,width,layers=frame.shape

video=cv2.VideoWriter(video_name, 0,30,(width,height))

for image in images: 
    video.write(cv2.imread(os.path.join(image_folder,image)))

cv2.destroyAllWindows()
video.release()

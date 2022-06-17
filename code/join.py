import cv2
import os
from natsort import natsorted, realsorted as ns

#getting extracted frames
image_folder='data'

#sorting the directory containing frames
files=os.listdir(image_folder)
new=natsorted(files)
video_name='asciify2.avi'

#compiling it into a video
images=[img for img in new if img.endswith(".jpg")]
frame=cv2.imread(os.path.join(image_folder,images[0]))
height,width,layers=frame.shape

video=cv2.VideoWriter(video_name, 0,30,(width,height))

for image in images: 
    video.write(cv2.imread(os.path.join(image_folder,image)))

cv2.destroyAllWindows()
video.release()

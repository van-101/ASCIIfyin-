# ASCIIfyin-
## converting images and photos to ASCII images and ASCII videos, 
The project consists of converting media to ascii art using python. the art consisting of photos and videos. 


## To convert colored photos to colored ASCII photos,
  ![Screenshot from 2022-06-17 03-15-21](https://user-images.githubusercontent.com/82715876/174171352-ec21465e-c077-42f2-b687-521f17b76195.png)


resizing the image
creating a new image using the PIL 
mapping chosen characters 
removing excess borders and saving the final image. 
 
 ### To run this, 
 upload the path of image you want to convert into ascii and recieve a output2.jpg file in your system

## To convert video to ASCII videos,
**the additional task**




https://user-images.githubusercontent.com/82715876/174432201-cb3bf207-bd05-41b7-a44f-3911ab0810ec.mp4


each frame of the video is captured seperately using opencv. 
each image is first converted to an ascii image using the code from to ascii photos. 
then each asciified image is saved in a seperate directory. 
the computer doesn't store the images in a natural order, so the `natsort` module comes in handy to sort the ascii frames and compile the images        in an order so that the video makes sense. 
the video is stored in an `.avi` form. But is converted here to .mp4 for the readme file.
     
 ### to run this, 
 work with a linux/mac system, 
upload the path of video in extract.py and run the extract.py file followed by the join.py file to recieve a video stored as "asciify2.avi". 

## Learnings from this project, 

This project made me comfortable with python and it's libraries like `OpenCV`, `PIL`, `natsort`, `os` and `numpy`. learnt the concepts of image processing, extracting frames, compiling frames and more. 
     
### Resources used: 
[acm source code week2](https://cdn.discordapp.com/attachments/978237259339939920/982623505289990144/ascii.py)<br>
[extracting images from a video](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjVsPqf_LL4AhVXIbcAHefLB5MQFnoECAIQAQ&url=https%3A%2F%2Fwww.geeksforgeeks.org%2Fextract-images-from-video-in-python%2F&usg=AOvVaw03nKIh1GhiABeCmT0QwaQo)<br>
[compiling extracted images into a video](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiro6XT_LL4AhVcldgFHULsCs0QFnoECAcQAQ&url=https%3A%2F%2Fpypi.org%2Fproject%2Fnatsort%2F&usg=AOvVaw3cz2abjPl-KY1YTlx8iCpt)<br>

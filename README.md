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

_(unable to upload the preview of the video in readme, you can find it in the files though)_

each frame of the video is captured seperately using opencv. 
each image is first converted to an ascii image using the code from to ascii photos. 
then each asciified image is saved in a seperate directory. 
the computer doesn't store the images in a natural order, so the `natsort` module comes in handy to sort the ascii frames and compile the images        in an order so that the video makes sense. 
the video is stored in an `.avi` form. 
     
 ### to run this, 
 upload the path of video in extract.py and then upload the path of the new directory called "data" to join.py. run the code to recieve a asciify.avi stored in your systen. 

## Learnings from this project, 

This project made me comfortable with python and it's libraries like `OpenCV`, `PIL`, `natsort`, `os` and `numpy`. learnt the concepts of image processing, extracting frames, compiling frames and more. 
     
### Resources used: 
[https://cdn.discordapp.com/attachments/978237259339939920/982623505289990144/ascii.py]

[https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjVsPqf_LL4AhVXIbcAHefLB5MQFnoECAIQAQ&url=https%3A%2F%2Fwww.geeksforgeeks.org%2Fextract-images-from-video-in-python%2F&usg=AOvVaw03nKIh1GhiABeCmT0QwaQo]

[https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiro6XT_LL4AhVcldgFHULsCs0QFnoECAcQAQ&url=https%3A%2F%2Fpypi.org%2Fproject%2Fnatsort%2F&usg=AOvVaw3cz2abjPl-KY1YTlx8iCpt]

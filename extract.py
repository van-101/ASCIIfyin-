# Importing all necessary libraries
import cv2
import os
from PIL import Image, ImageOps, ImageDraw, ImageFont
import numpy as np

Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}


def get_data(mode):
    font = ImageFont.truetype("fonts/DejaVuSansMono-Bold.ttf", size=20)
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale


# Making Background Black or White
bg = "white"
# bg = "black"
if bg == "white":
    bg_code = (255, 255, 255)
elif bg == "black":
    bg_code = (0,0,0)

# Getting the character List, Font and Scaling characters for square Pixels
char_list, font, scale = get_data("complex")
num_chars = len(char_list)
num_cols = 300


# Read the video from specified path
vid = cv2.VideoCapture("/home/rasputina/py_comding/opencv/gossip.mp4")

try:

    # creating a folder named data
    if not os.path.exists('new'):
        os.makedirs('new')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while (True):

    # reading from frame
    success, frame = vid.read()

    if success:
        # continue creating images until video remains
        name = './new/frame' + str(currentframe) + '.jpg'
        #   name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)
        image=frame
#  Extracting height and width from Image
        height, width, x = image.shape

# Defining height and width of each cell==pixel
        cell_w = width / num_cols
        cell_h = scale * cell_w
        num_rows = int(height / cell_h)
# print(num_rows, cell_w, cell_h)

# Calculating Height and Width of the output Image
        char_width, char_height = font.getsize("A")
        out_width = char_width * num_cols
        out_height = scale * char_height * num_rows

# Making a new Image using PIL
        out_image = Image.new("RGB", (out_width, out_height), bg_code)
        draw = ImageDraw.Draw(out_image)


#mapping characters RGB
        for i in range(num_rows): 
            for j in range(num_cols): 
                partial_image=image[int(i*cell_h):min(int((i+1)*cell_h),height),int(j*cell_w):min(int((j+1)*cell_w), width),:]
                partial_avg_color=np.sum(np.sum(partial_image, axis=0), axis=0)/(cell_h*cell_w)
                partial_avg_color=tuple(partial_avg_color.astype(np.int32).tolist())
                c=char_list[min(int(np.mean(partial_image)*num_chars/255),num_chars-1)]
                draw.text((j*char_width, i*char_height), c, fill=partial_avg_color, font=font)


# Inverting Image and removing excess borders
        if bg == "white":
            cropped_image = ImageOps.invert(out_image).getbbox()
        elif bg == "black":
            cropped_image = out_image.getbbox()

# Saving the new Image
        out_image = out_image.crop(cropped_image)
        # img=Image.fromarray(out_image)
        
        # writing the extracted images
        out_image.save(f"{name}")

        # increasing counter so that it will
        currentframe += 1
        # show how many frames are created
    
    else: 
        break


vid.release()
cv2.destroyAllWindows()

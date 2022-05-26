import qrcode
# generating a qrcode, and saving it as a jpg file
img=qrcode.make("https://www.tacobell.co.in/")
img.save("my heart<3".jpg)


#reading qrcodes

import cv2
d=cv2.QRCodeDetector()

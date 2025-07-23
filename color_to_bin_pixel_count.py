#step one convert your image to binary color for it to be easily be analized. the black part will be perlite, white part wil be considered cementite

import cv2

# Load the image
image = cv2.imread("ogsample.jpg")  #replace the ogsample.jpg with your image path

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
ret, binary_image = cv2.threshold(gray_image, 116, 270, cv2.THRESH_BINARY) 

# Save the binary image
cv2.imwrite("binary_image.jpg", binary_image) 

#https://www.tutorialspoint.com/opencv-python-how-to-convert-a-colored-image-to-a-binary-image


#now analyze this image with pillow. 
from PIL import Image
import numpy as np

def bw_anal(image_path):
    image = Image.open(image_path).convert('L')
    image_aray = np.array(image)
    total_pixels = image_aray.size

    # threshold for black or white range
    black_threshhold = 30
    white_threshhold = 225

    black_pixels = np.sum(image_aray < black_threshhold)
    white_pixels = np.sum(image_aray >white_threshhold)

    black_percentage = (black_pixels/total_pixels)*100
    white_percentage = (white_pixels/total_pixels)*100

   #print(f'black pixels: {black_pixels}')
   #print(f'white pixels: {white_pixels}')
    print(f'black: {black_percentage}%\nwhite: {white_percentage}%')

path = 'binary_image.jpg' #this is the image we created. #replace this path with your photo. 
bw_anal(path)


import cv2
  
# Reading the image

path = r'.\imagens\dogs.jpg' 
image = cv2.imread(path) 
  
# Extracting height and width from 
# image shape
height, width = image.shape[:2]
  
# get the center coordinates of the
# image to create the 2D rotation
# matrix
center = (width/2, height/2)
  
# using cv2.getRotationMatrix2D() 
# to get the rotation matrix
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=1)
  
# rotate the image using cv2.warpAffine 
# 90 degree anticlockwise
rotated_image = cv2.warpAffine(
    src=image, M=rotate_matrix, dsize=(width, height))
  
cv2.imshow("rotated image:", rotated_image)
cv2.imwrite('rotated_image.jpg', rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
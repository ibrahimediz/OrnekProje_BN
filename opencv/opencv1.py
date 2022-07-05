import cv2
import numpy as np

img = cv2.imread("opencv/pictures/ornekler1.jpeg")
print(img[25:50,25:50])
img[25:50,25:50] = [255,255,255]
cv2.imshow("imaj",img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
"""
 [[69 81 83]  # RGB opencv bunu BGR olarak okuyor
  [69 81 83]
  [70 82 84]
  ...
  [66 78 80]
  [68 80 82]
  [71 83 85]]]
"""
# [69 81 83] gri =>  [212]
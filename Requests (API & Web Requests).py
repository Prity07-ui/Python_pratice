#Requests (API & Web Requests)

import requests

response = requests.get("https://api.github.com")

print(response.status_code)

#OpenCV (Computer Vision)
import cv2

img = cv2.imread("image.jpg")

cv2.imshow("Image", img)
cv2.waitKey(0)
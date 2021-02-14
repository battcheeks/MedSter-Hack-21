import requests
url3 = "http://localhost:8000/old_data/"
url = []
response = requests.get(url3)
response = response.json()
response = response[-1]
url = response['image']

import cv2
from skimage import io
img = io.imread(url)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imshow('URL Image', img)
cv2.waitKey()
cv2.destroyAllWindows()


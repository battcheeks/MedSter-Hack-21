import requests
import json
import cv2
import urllib
import numpy as np
url1 = "http://localhost:8000/appointments/"  
response = requests.get(url1)
print(response.json())

data = {"patient_name": "uvXYZ",
"gender": "F",
"address": "lk,",
"number": 1,
"appointment_date": "2021-02-10",
"time": "10:00 - 11:00",
"doctor_name": "Mahesh",
"hospital_name": "m,",
"description": "nm,."}

resp = requests.post(url1, json=data)
print(resp.status_code)


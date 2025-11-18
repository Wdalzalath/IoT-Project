import requests
# import urllib, json
import RPi.GPIO as GPIO
import time

# setup rpi pin
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

# you can add extra
# GPIO.setup(24,GPIO.OUT)
# GPIO.setup(25,GPIO.OUT)

while True:
    # change url
    # url = "https://www.example.com/data/"
    url  = requests.get("http://localhost:9990/data")
    data = url.json()
    
    # you can use this
    # response = urllib.urlopen(url)
    # data = json.loads(response.read())
    
    # print(len(data))
    # print(data)
    for i in range(0, 3): # length of rpi pin(3 or 5 or ..)
        if data[i]['Room Status'] == '1' and data[i]['Room No'] in 'Room_1':
            GPIO.output(18,GPIO.HIGH) # light on
            time.sleep(0.5)
        elif data[i]['Room Status'] == '0' and data[i]['Room No'] in 'Room_1':
            GPIO.output(18,GPIO.LOW) # light off
            time.sleep(0.5)
        elif data[i]['Room Status'] == '1' and data[i]['Room No'] in 'Room_2':
            GPIO.output(23,GPIO.HIGH) # light on
            time.sleep(0.5)
        elif data[i]['Room Status'] == '0' and data[i]['Room No'] in 'Room_2':
            GPIO.output(23,GPIO.LOW) # light off
            time.sleep(0.5)
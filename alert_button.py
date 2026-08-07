import requests
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

data = {
    "chat_id" :"6632493494",
    "text" : "Someone pressed the alert button!"
}
button_pressed = False
while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        sendRequest = requests.post("https://api.telegram.org/bot8706346697:AAFUgaCNxWhtKYyEpx6SECfMihya8t2dEPA/sendMessage", json= data)
        button_pressed = True
    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False
    time.sleep(0.1)


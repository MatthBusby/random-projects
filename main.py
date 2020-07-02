import time
import RPi.GPIO as GPIO


RelayPin = 10 
TouchPin = 11

def setup ():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(RelayPin, GPIO.OUT)
    
def loop():
	while True:
		if GPIO.input(TouchPin) == GPIO.HIGH:
			print 'touched!'
			GPIO.output(RelayPin, GPIO.HIGH)
		else:	
			GPIO.output(RelayPin, GPIO.LOW) # close cir

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  
		destroy()

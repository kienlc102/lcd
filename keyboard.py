import RPi.GPIO as GPIO
import time
import sys

left = 7
right = 13
enter = 22
led1 = 0
led2 = 5
led3 = 6
led4 = 26
def buttonEventHandler (pin):
    print("handling button event",pin)
    toggleLED(led3)
    # turn the green LED on
    #GPIO.output(25,True)

    #time.sleep(1)

    # turn the green LED off
    #GPIO.output(25,False)

def my_callback(channel):
    print('This is a edge event callback function!')

def setLEDon(LED):
    GPIO.output(LED,True)

def setLEDoff(LED):
    GPIO.output(LED,False)

def toggleLED(LED):
    if (GPIO.input(LED) == True):
        GPIO.output(LED,False)
    else:
        GPIO.output(LED,True)
# main function
def main():

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(True)
    # Setup BUTTON as INPUT
    GPIO.setup(enter,GPIO.IN)
    GPIO.setup(left,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(right,GPIO.IN)

    # Setup LED as OUTPUT
    GPIO.setup(led1,GPIO.OUT)
    GPIO.setup(led2,GPIO.OUT)
    GPIO.setup(led3,GPIO.OUT)
    GPIO.setup(led4,GPIO.OUT)
    #GPIO.remove_event_detect(left)
    GPIO.add_event_detect(enter,GPIO.FALLING)
    try:
        GPIO.add_event_detect(left,GPIO.FALLING)
    except RuntimeError as e:
        print(e)
        sys.exit()
    GPIO.add_event_detect(right,GPIO.FALLING)
    GPIO.add_event_callback(enter,buttonEventHandler)
    GPIO.add_event_callback(left,buttonEventHandler)
    GPIO.add_event_callback(right,buttonEventHandler)
    

    # make the red LED flash
    try:
        while True:
            #GPIO.output(24,True)
            #time.sleep(1)
            #GPIO.output(24,False)
            time.sleep(1)
    except KeyboardInterrupt:
        print ("Program interrupted by CTRL-C")
    except:
        print ("Other error or exception occurred!")
    finally:
        print ("Clean up")
        GPIO.cleanup()



    GPIO.cleanup()



if __name__=="__main__":
    main()


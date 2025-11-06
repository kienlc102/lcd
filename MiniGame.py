import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_1inch8
from PIL import Image,ImageDraw,ImageFont
import RPi.GPIO as GPIO
import player as player
import ball as ball


# Raspberry Pi pin configuration:
RST = 27
DC = 23
BL = 18
bus = 1 
device = 0 
logging.basicConfig(level=logging.DEBUG)

class MiniGame():

    def __init__(self):
            self.disp = None
            self.switch = 17
            self.left = 13
            self.right = 7
            self.enter = 22
            self.player = player.player(60, 80)
            self.ball = ball.ball(0, 0)
    
    def active(self):
        if self.disp is None:
            try:
                print("active LCD_1inch8.LCD_1inch8")

                self.disp = LCD_1inch8.LCD_1inch8()
                self.disp.Init()
                self.disp.clear()
            except Exception as e:
                print("Displayer active error: ", e)
    
    def setupGPIO(self):
        print("Starting testButton...")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.right, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.enter, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print("hoan tat setup")

    def show_frame(self, frame):
        try:
            # Show image
            if self.disp is not None:
                self.disp.ShowImage(frame)
            
        except IOError as e:
            logging.info(e)    
        except KeyboardInterrupt:
            self.disp.module_exit()
            logging.info("quit:")
            exit()

    def draw_text(self, text, position, color=(255,255,255)):
        if self.disp is None:
            self.active()
        image = Image.new("RGB", (160, 128), (0,0,0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        draw.text(position, text, font=font, fill=color)
        self.show_frame(image)

    def clear(self):
        self.disp.clear() 

    def stop(self):
        try:
            self.disp.module_exit()
            print("STOP - DISPLAY")
        except:
            pass
        logging.info("quit:")
        print()
        #need2check
        #exit()
    
    def sleep(self):
        print("Displayer sleep")

        try:
            self.disp.clear()
            if self.disp is not None:
                self.disp.module_exit()
            
            logging.info("quit:")
            self.disp = None

            #test
            #self.disp = None
            #exit()
        except Exception as e:
            print("Displayer sleep error: ", e)

    def game_loop(self):
        self.active()
        self.setupGPIO()
        try:
            while True:
                self.clear()
                self.draw_text(self.player.block, (self.player.x, self.player.y))
                self.draw_text("*", (self.ball.x, self.ball.y))
        except KeyboardInterrupt:
            print("Exiting game loop...")
        finally:
            self.sleep()
            self.stop()
    




                                                                                                  
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_1inch8
from PIL import Image,ImageDraw,ImageFont
import RPi.GPIO as GPIO


# Raspberry Pi pin configuration:
RST = 27
DC = 23
BL = 18
bus = 1 
device = 0 
logging.basicConfig(level=logging.DEBUG)


class Displayer():

    def __init__(self):
        try:
            self.disp = None
            self.switch = 17
            self.left = 7
            self.right = 13
            self.enter = 22
        except IOError as e:
            logging.info(e) 
    
    def is_switch_active(self):
        print('is_switch_active:',GPIO.input(17))
        if GPIO.input(17):
            return False
        else:
            return True

    def set_disp(self):
        print('set_disp:',GPIO.input(17))
        if GPIO.input(17):
            print("set_disp SLEEP")
            return False
        else:
            print("set_disp ACTIVE")
            self.disp = LCD_1inch8.LCD_1inch8()
            Lcd_ScanDir = LCD_1inch8.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
            # Initialize library.
            self.disp.Init()
            # Clear display.
            self.disp.clear()
            return True
            

    def clear(self):
        self.disp.clear() 

    def show(self, image):
        try:
            # Show image
            self.disp.ShowImage(image)
                        
        except IOError as e:
            logging.info(e)    
        except KeyboardInterrupt:
            self.disp.module_exit()
            logging.info("quit:")
            exit()

    def active(self):
        if self.disp is None:
            try:
                print("active LCD_1inch8.LCD_1inch8")

                self.disp = LCD_1inch8.LCD_1inch8()
                self.disp.Init()
                self.disp.clear()
            except Exception as e:
                print("Displayer active error: ", e)

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
    
    def draw_text(self, text, position, color=(255,255,255)):
        if self.disp is None:
            self.active()
        image = Image.new("RGB", (160, 128), (0,0,0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        draw.text(position, text, font=font, fill=color)
        self.show_frame(image)
    
    def testButton(self):
        print("Starting testButton...")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.right, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.enter, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print("hoan tat setup")
        
        try:
            while True:
                if GPIO.input(self.left) == GPIO.HIGH:
                    self.clear()
                    self.draw_text("Left Pressed", (10, 50))
                    print("Left Pressed")
                if GPIO.input(self.right) == GPIO.HIGH:
                    self.clear()
                    self.draw_text("Right Pressed", (10, 50))
                    print("Right Pressed")
                if GPIO.input(self.enter) == GPIO.HIGH:
                    self.clear()
                    self.draw_text("Enter Pressed", (10, 50))
                    print("Enter Pressed")
                time.sleep(0.2)
        except KeyboardInterrupt:
            print("Exiting testButton")
        finally:
            GPIO.cleanup()


    





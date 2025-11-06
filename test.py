from display import Displayer
from PIL import Image
import time
image_path = "/home/pi/kien/lcd/alo1.jpg"

image = Image.open(image_path)
test = Displayer()
test.active()

test.draw_text("dep trai")
while 1:
    time.sleep(1)



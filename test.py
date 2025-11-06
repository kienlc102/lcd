from display import Displayer
from PIL import Image


# Khởi tạo LCD
lcd = Displayer()
lcd.active()



# Chạy test nút nhấn
try:
    lcd.testButton()
except KeyboardInterrupt:
    print("Exiting...")
finally:
    lcd.sleep()
    lcd.stop()

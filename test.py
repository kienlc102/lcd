from display import Displayer
from PIL import Image

image_path = "/home/pi/kien/lcd/alo1.jpg"

# Khởi tạo LCD
lcd = Displayer()
lcd.active()

# Hiển thị ảnh lúc khởi động
lcd.show(image_path)

# Chạy test nút nhấn
try:
    lcd.testButton()
except KeyboardInterrupt:
    print("Exiting...")
finally:
    lcd.sleep()
    lcd.stop()

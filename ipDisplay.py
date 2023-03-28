import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess

#pin configuration:
RST = None     
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding

x = 0

font = ImageFont.load_default()

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    cmd = "echo 'Gathering Data...'"
    CPU = subprocess.check_output(cmd, shell = True )
    cmd = 'sleep 5'
    MemUsage = subprocess.check_output(cmd, shell = True )
    
    # Write two lines of text.

    draw.text((x, top+50),       "IP: " + str(IP, 'utf-8'),  font=font, fill=255)
    draw.text((x, top),     str(CPU, 'utf-8'), font=font, fill=255)
    draw.text((x, top+15),    str(MemUsage, 'utf-8'),  font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(.1)

# banana py_ws2812 #
This module contains python routines to program the WS2812 RGB LED chips on the banana pi,
using the hardware SPI MOSI (so no other hardware is needed)

As the WS2812 communication needs strict timing, the DIN line cannot be driven from
a normal GPIO line with python (an interrupt on the banana pi would screw things up).
Thats' why this module uses the hardware SPI MOSI line, this does confirm to the
timing requirements.

More info on the WS2812: https://www.amazon.com/Ring-WS2812-Light-Integrated-Drivers/dp/B07Z43Z3R8
# Wiring of WS2812-banana pi #
Connections from the banana pi to the WS2812:
![image](https://user-images.githubusercontent.com/69899376/232456440-25eb9861-7c35-45fe-9dab-b651c043b499.png)


```
WS2812     Bananapi M2
GND   --   GND. At least one of pin 6, 9, 14, 20, 25
DIN   --   MOSI, Pin 19, MOSI
VCC   --   5V. At least one of pin 2 or 4
```

Of course the WS2812 can (should) be chained, the DOUT of the first
connected to the DIN of the next, and so on.

Then, get the python spidev module:
```
git clone https://github.com/vanvohuyhoang/py-spidev.git
cd py-spidev
make
make install
```

# Testing this ws2812.py module #
This module can be tested using:
    python ws2812.py


Sample program that uses the module:
```
import spidev
import ws2812
import time

spi = spidev.SpiDev()
spi.open(0, 0)

# define the colors
colors = [
    [255, 0, 0],    # red
    [0, 255, 0],    # green
    [0, 0, 255],    # blue
    [255, 255, 0],  # yellow
    [255, 0, 255],  # purple
    [0, 255, 255],  # cyan
    [255, 255, 255],  # white
    [255, 165, 0],  # orange
    [255, 192, 203],  # pink
    [0, 128, 128],  # teal
    [230, 230, 250],  # lavender
    [139, 0, 139],  # magenta
]

def send_color(spi, color):
    ws2812.write2812(spi, [color] * 12)

def turn_off_leds(spi):
    colors = [[0, 0, 0]] * 12
    ws2812.write2812(spi, colors)

# loop through the colors and send each one with a delay of 1 second
for color in colors:
    send_color(spi, color)
    time.sleep(1)

# turn off the LEDs at the end
turn_off_leds(spi)

```
    
# Notes #
Note: this module tries to use numpy, if available.
Without numpy it still works, but is *really* slow (more than a second
to update 300 LED's on a banana pi Pi Zero).
So, if possible, do:
```
sudo apt install python-numpy
```
![image](https://user-images.githubusercontent.com/69899376/232456243-5e4685ed-ddaa-41a5-9532-d008caf3eff5.png)

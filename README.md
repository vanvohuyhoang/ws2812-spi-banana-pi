# bananapy_ws2812 #
This module contains python routines to program the WS2812 RGB LED chips on the banana pi,
using the hardware SPI MOSI (so no other hardware is needed)

As the WS2812 communication needs strict timing, the DIN line cannot be driven from
a normal GPIO line with python (an interrupt on the banana pi would screw things up).
Thats' why this module uses the hardware SPI MOSI line, this does confirm to the
timing requirements.

More info on the WS2812: https://www.amazon.com/Ring-WS2812-Light-Integrated-Drivers/dp/B07Z43Z3R8
# Wiring of WS2812-banana pi #
Connections from the banana pi to the WS2812:
 +-----+-----+---------+------+---+---Pi ?---+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |  12 |   8 |   SDA.1 | ALT5 | 0 |  3 || 4  |   |      | 5v      |     |     |
 |  11 |   9 |   SCL.1 | ALT5 | 0 |  5 || 6  |   |      | 0v      |     |     |
 |   6 |   7 | GPIO. 7 | ALT3 | 0 |  7 || 8  | 0 | ALT4 | TxD     | 15  | 13  |
 |     |     |      0v |      |   |  9 || 10 | 0 | ALT4 | RxD     | 16  | 14  |
 |   1 |   0 | GPIO. 0 | ALT5 | 0 | 11 || 12 | 0 | ALT4 | GPIO. 1 | 1   | 16  |
 |   0 |   2 | GPIO. 2 | ALT5 | 0 | 13 || 14 |   |      | 0v      |     |     |
 |   3 |   3 | GPIO. 3 | ALT5 | 0 | 15 || 16 | 0 | ALT4 | GPIO. 4 | 4   | 15  |
 |     |     |    3.3v |      |   | 17 || 18 | 0 | ALT3 | GPIO. 5 | 5   | 68  |
 |  64 |  12 |    MOSI | ALT4 | 0 | 19 || 20 |   |      | 0v      |     |     |
 |  65 |  13 |    MISO | ALT4 | 0 | 21 || 22 | 0 | ALT5 | GPIO. 6 | 6   | 2   |
 |  66 |  14 |    SCLK | ALT4 | 0 | 23 || 24 | 0 | ALT4 | CE0     | 10  | 67  |
 |     |     |      0v |      |   | 25 || 26 | 0 | ALT3 | CE1     | 11  | 71  |
 |  19 |  30 |   SDA.0 | ALT4 | 0 | 27 || 28 | 0 | ALT4 | SCL.0   | 31  | 18  |
 |   7 |  21 | GPIO.21 | ALT3 | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   8 |  22 | GPIO.22 | ALT3 | 0 | 31 || 32 | 0 | ALT5 | GPIO.26 | 26  | 354 |
 |   9 |  23 | GPIO.23 | ALT3 | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  10 |  24 | GPIO.24 | ALT3 | 0 | 35 || 36 | 0 | ALT3 | GPIO.27 | 27  | 356 |
 |  17 |  25 | GPIO.25 | ALT3 | 0 | 37 || 38 | 0 | ALT3 | GPIO.28 | 28  | 21  |
 |     |     |      0v |      |   | 39 || 40 | 0 | ALT3 | GPIO.29 | 29  | 20  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+---Pi ?---+---+------+---------+-----+-----+

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

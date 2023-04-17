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

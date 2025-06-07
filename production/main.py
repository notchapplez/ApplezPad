import board
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
import neopixel

button_pins = (board.GP26, board.GP27, board.GP28, board.GP29, board.GP6, board.GP7)
led_pin = board.GP4
num_leds = 6

keyboard = KMKKeyboard()
keyboard.col_pins = button_pins
keyboard.row_pins = ()
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.keymap = [
    [
        KC.LCTL(KC.C),
        KC.LCTL(KC.V),
        KC.PGUP,
        KC.LGUI(KC.C),
        KC.LGUI(KC.V),
        KC.PGDN
    ]
]

pixels = neopixel.NeoPixel(led_pin, num_leds, brightness=0.3, auto_write=False)

def wheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (0, int(pos * 3), int(255 - pos * 3))
    elif pos < 170:
        pos -= 85
        return (int(pos * 3), int(255 - pos * 3), 0)
    else:
        pos -= 170
        return (int(255 - pos * 3), 0, int(pos * 3))

def led_loop():
    t = time.monotonic()
    base = int((t * 50) % 255)
    for i in range(num_leds):
        color = wheel((base + i * 42) % 255)
        pixels[i] = color
    pixels.show()

if __name__ == '__main__':
    keyboard.start()
    while True:
        keyboard.process()
        led_loop()
        time.sleep(0.02)

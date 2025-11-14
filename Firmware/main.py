import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

mouse_keys = MouseKeys()
keyboard.modules.append(mouse_keys)


PINS = [board.D5, board.D6, board.D7, board.D8, board.D9, board.D10, board.D0, board.D1, board.D2]
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D, KC.E, KC.F]
]

if __name__ == '__main__':
    keyboard.go()








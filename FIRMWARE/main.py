import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.modules.holdtap import HoldTap
from kmk.modules.oled import Oled, OledDisplayMode

keyboard = KMKKeyboard()

# ---------- MODULES ----------
keyboard.modules.append(Macros())
keyboard.modules.append(HoldTap())

# ---------- OLED (STATIC TEXT) ----------
oled = Oled(
    oled_width=128,
    oled_height=32,          
    device_address=0x3C,
    i2c=board.I2C(),         
    default_display_mode=OledDisplayMode.STATIC,
    static_text="Sashreek's Macropad!",
)
keyboard.modules.append(oled)

# ---------- PIN MAPPING ----------

PINS = [
    board.GP27,   # SW1
    board.GP28,   # SW2
    board.GP29,   # SW3
    board.GP1,    # SW4
    board.GP2,    # SW5
    board.GP26,   # SW6
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# ---------- KEYMAP ----------
keyboard.keymap = [
    [
        KC.SPACE,                                # SW1
        KC.A,                                    # SW2
        KC.W,                                    # SW3
        KC.S,                                    # SW4
        KC.HT(KC.E, KC.ESC, prefer_hold=False),  # SW5 tap = E, hold = ESC
        KC.D,                                    # SW6
    ]
]

# ---------- START ----------
if __name__ == '__main__':
    keyboard.go()

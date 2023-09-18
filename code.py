print("Starting Keyboard")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.layers import Layers
from kmk.modules.capsword import CapsWord

keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.ROW2COL
keyboard.row_pins = (board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)
keyboard.col_pins = (board.GP22, board.GP21, board.GP20, board.GP19, board.GP18, board.GP17)
keyboard.extensions.append(MediaKeys()) # Needed for volume control


ZOOM_IN = KC.LCTL(KC.PLUS)
ZOOM_OUT = KC.LCTL(KC.MINUS)

# setup the rotary ecoder volume knob
encoder_handler = EncoderHandler()
encoder_handler.pins = [
    [board.GP6, board.GP7, None, False],
]
encoder_handler.map = [
    [[KC.VOLU, KC.VOLD]], # An array for the layer, and an array for each encoder in that layer
    [[ZOOM_IN, ZOOM_OUT]],
    [[KC.BRIGHTNESS_UP, KC.BRIGHTNESS_DOWN]],
    # the button press is in the key matrix
]
keyboard.modules.append(encoder_handler)
keyboard.modules.append(Layers())
keyboard.modules.append(CapsWord())

# Setup the split communication
split = Split(split_type=SplitType.UART, split_side=SplitSide.LEFT, data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip = True)
keyboard.modules.append(split)

# Layer Keys
LAYER_1_KEY = KC.MO(1)
LAYER_2_KEY = KC.MO(2)

# Special Keys
XXXXX = KC.NO
_____ = KC.TRNS
SEL_LEFT = KC.LALT(KC.LSHIFT(KC.LEFT))
SEL_RIGHT = KC.LALT(KC.LSHIFT(KC.RIGHT))
# SEL_UP = KC.LALT(KC.LSHIFT(KC.UP))
# SEL_DOWN = KC.LALT(KC.LSHIFT(KC.DOWN))

LINE_UP = KC.LALT(KC.UP)
LINE_DOWN = KC.LALT(KC.DOWN)

# Thumb Keys Diagram
#            ____                                      ____
#           | 21 |                                    | 18 |
#           |____|          -----     ----            |____| 
#                  ______  / 18 /     \ 21 \   _____
#                /      / /____/       \____\  \  20 \
#  -------      /   19 / /----/         -----   \     \   ______
# |   20  |     \_____/ / 17 /           \ 22 \  \____/  |  19  |
# |_______|            /____/             \____\         |______| 

default_keys = [
    # Left Side                                                          # Right Side
    # GP22     # GP21      # GP20  #GP19     #GP18     #GP17             # GP22        # GP21      # GP20      #GP19     #GP18      #GP17
    KC.ESCAPE,  KC.N1,      KC.N2,  KC.N3,    KC.N4,   KC.N5,            KC.N6,        KC.N7,       KC.N8,     KC.N9,    KC.N0,     KC.MINUS,   #GP09
    KC.GRAVE,   KC.Q,       KC.W,   KC.E,     KC.R,    KC.T,             KC.Y,         KC.U,        KC.I,      KC.O,     KC.P,      KC.EQL,     #GP10
    KC.LSHIFT,  KC.A,       KC.S,   KC.D,     KC.F,    KC.G,             KC.H,         KC.J,        KC.K,      KC.L,     KC.SCOLON, KC.QUOTE,   #GP11
    KC.LCTL,    KC.Z,       KC.X,   KC.C,     KC.V,    KC.B,             KC.N,         KC.M,        KC.COMMA,  KC.DOT,   KC.SLASH,  KC.BSLASH,  #GP12
    XXXXX,      KC.MPLY,    KC.TAB, KC.SPACE, KC.LALT, LAYER_1_KEY,      LAYER_2_KEY,  KC.DELETE,   KC.BSPACE, KC.ENTER, KC.LGUI,   XXXXX,      #GP13
]
extra_keys = [
    _____, _____, _____, _____, _____, _____,       _____, _____, _____, KC.LBRACKET, KC.RBRACKET, _____, 
    _____, _____, _____, _____, _____, _____,       _____, _____, _____, _____, _____, _____, 
    _____, _____, _____, _____, _____, _____,       _____, _____, KC.UP, _____, _____, _____, 
    _____, _____, _____, _____, _____, _____,       _____, KC.LEFT, KC.DOWN, KC.RIGHT, _____, 
    _____, _____, _____, _____, _____, _____,       _____, _____, _____, _____, _____, _____, 
]

vs_code_keys = [
    _____, _____, _____, _____, _____, _____,       _____, _____, _____, _____, _____, _____, 
    _____, _____, _____, _____, _____, _____,       _____, _____, _____, _____, _____, _____, 
    KC.CW, _____, _____, _____, _____, _____,       _____, _____, LINE_UP, _____, _____, _____, 
    _____, _____, _____, _____, _____, _____,       _____, SEL_LEFT, LINE_DOWN, SEL_RIGHT, _____, 
    _____, _____, _____, _____, _____, _____,       _____, _____, _____, _____, _____, _____, 
]

keyboard.keymap = [
    default_keys,
    extra_keys,
    vs_code_keys,
]

if __name__ == '__main__':
    keyboard.go()
    

# -------------
# AI Generated
# -------------

# USB HID "boot keyboard" usage codes
# Modifiers are a bitmask: 
#   0x02 = Left Shift, 0x40 = Right Alt (AltGr)

MOD_LSHIFT = 0x02
MOD_ALTGR  = 0x40

KEYMAP_DE = {
    # Letters (y/z swapped on DE)
    'a': (0x04, 0x00), 'b': (0x05, 0x00), 'c': (0x06, 0x00),
    'd': (0x07, 0x00), 'e': (0x08, 0x00), 'f': (0x09, 0x00),
    'g': (0x0A, 0x00), 'h': (0x0B, 0x00), 'i': (0x0C, 0x00),
    'j': (0x0D, 0x00), 'k': (0x0E, 0x00), 'l': (0x0F, 0x00),
    'm': (0x10, 0x00), 'n': (0x11, 0x00), 'o': (0x12, 0x00),
    'p': (0x13, 0x00), 'q': (0x14, 0x00), 'r': (0x15, 0x00),
    's': (0x16, 0x00), 't': (0x17, 0x00), 'u': (0x18, 0x00),
    'v': (0x19, 0x00), 'w': (0x1A, 0x00), 'x': (0x1B, 0x00),
    'z': (0x1C, 0x00),
    'y': (0x1D, 0x00),

    'A': (0x04, MOD_LSHIFT), 'B': (0x05, MOD_LSHIFT), 'C': (0x06, MOD_LSHIFT),
    'D': (0x07, MOD_LSHIFT), 'E': (0x08, MOD_LSHIFT), 'F': (0x09, MOD_LSHIFT),
    'G': (0x0A, MOD_LSHIFT), 'H': (0x0B, MOD_LSHIFT), 'I': (0x0C, MOD_LSHIFT),
    'J': (0x0D, MOD_LSHIFT), 'K': (0x0E, MOD_LSHIFT), 'L': (0x0F, MOD_LSHIFT),
    'M': (0x10, MOD_LSHIFT), 'N': (0x11, MOD_LSHIFT), 'O': (0x12, MOD_LSHIFT),
    'P': (0x13, MOD_LSHIFT), 'Q': (0x14, MOD_LSHIFT), 'R': (0x15, MOD_LSHIFT),
    'S': (0x16, MOD_LSHIFT), 'T': (0x17, MOD_LSHIFT), 'U': (0x18, MOD_LSHIFT),
    'V': (0x19, MOD_LSHIFT), 'W': (0x1A, MOD_LSHIFT), 'X': (0x1B, MOD_LSHIFT),
    'Z': (0x1C, MOD_LSHIFT),
    'Y': (0x1D, MOD_LSHIFT),

    '1': (0x1E, 0x00), '2': (0x1F, 0x00), '3': (0x20, 0x00),
    '4': (0x21, 0x00), '5': (0x22, 0x00), '6': (0x23, 0x00),
    '7': (0x24, 0x00), '8': (0x25, 0x00), '9': (0x26, 0x00),
    '0': (0x27, 0x00),

    ' ':  (0x2C, 0x00),  # Space
    '\n': (0x28, 0x00),  # Enter
    '\t': (0x2B, 0x00),  # Tab

    # German-specific letters
    'ä': (0x34, 0x00), 'Ä': (0x34, MOD_LSHIFT),
    'ö': (0x33, 0x00), 'Ö': (0x33, MOD_LSHIFT),
    'ü': (0x2F, 0x00), 'Ü': (0x2F, MOD_LSHIFT),
    'ß': (0x2D, 0x00),

    # Punctuation on DE (note: differs from US)
    # Key 0x2D (US '-') is 'ß' / '?' on DE
    '?': (0x2D, MOD_LSHIFT),

    # Key 0x38 (US '/') is '-' / '_' on DE
    '-': (0x38, 0x00),
    '_': (0x38, MOD_LSHIFT),

    # Key 0x30 (US '=') is '´' / '`' on US, BUT on DE: this is to the right of 'Ü' -> '+' / '*'
    '+': (0x30, 0x00),
    '*': (0x30, MOD_LSHIFT),

    # Key 0x31 (US '\') is '#'/ '\'' on DE
    '#': (0x31, 0x00),
    '\'': (0x31, MOD_LSHIFT),

    # Key 0x33 (US ';') is 'ö' handled above
    # Key 0x34 (US ''') is 'ä' handled above

    # Key 0x36 / 0x37: comma/period and their shifted forms
    ',': (0x36, 0x00),
    ';': (0x36, MOD_LSHIFT),
    '.': (0x37, 0x00),
    ':': (0x37, MOD_LSHIFT),

    # Key 0x38 handled as -/_ above

    # Brackets on DE are via AltGr on the number row
    '{': (0x24, MOD_ALTGR),  # AltGr+7
    '[': (0x25, MOD_ALTGR),  # AltGr+8
    ']': (0x26, MOD_ALTGR),  # AltGr+9
    '}': (0x27, MOD_ALTGR),  # AltGr+0

    # At, Euro, backslash, pipe, tilde on DE via AltGr
    '@': (0x14, MOD_ALTGR),  # AltGr+Q
    '€': (0x08, MOD_ALTGR),  # AltGr+E
    '\\': (0x2D, MOD_ALTGR), # AltGr+ß
    '|': (0x64, MOD_ALTGR),  # AltGr+< (102nd key)
    '~': (0x30, MOD_ALTGR),  # AltGr+'+' -> '~'

    # Caret and degree (dead key on DE) on 0x35 (US '`' key)
    '^': (0x35, 0x00),             # dead ^ (DE)
    '°': (0x35, MOD_LSHIFT),       # Shift+^
    # Acute/grave dead key (DE) is 0x2E (US '=' key)
    '´': (0x2E, 0x00),             # dead acute
    '`': (0x2E, MOD_LSHIFT),       # dead grave

    # Parentheses and common shifted symbols (DE on number row)
    '!': (0x1E, MOD_LSHIFT),
    '"': (0x1F, MOD_LSHIFT),
    '§': (0x20, MOD_LSHIFT),
    '$': (0x21, MOD_LSHIFT),
    '%': (0x22, MOD_LSHIFT),
    '&': (0x23, MOD_LSHIFT),
    '/': (0x24, MOD_LSHIFT),  # note: '/' is Shift+7 on DE
    '(': (0x25, MOD_LSHIFT),
    ')': (0x26, MOD_LSHIFT),
    '=': (0x27, MOD_LSHIFT),

    # 102nd key (to the left of Z on DE keyboard)
    '<': (0x64, 0x00),
    '>': (0x64, MOD_LSHIFT),
}


KEYMAP_US = {
    # Letters
    'a': (0x04, 0), 'b': (0x05, 0), 'c': (0x06, 0), 'd': (0x07, 0),
    'e': (0x08, 0), 'f': (0x09, 0), 'g': (0x0A, 0), 'h': (0x0B, 0),
    'i': (0x0C, 0), 'j': (0x0D, 0), 'k': (0x0E, 0), 'l': (0x0F, 0),
    'm': (0x10, 0), 'n': (0x11, 0), 'o': (0x12, 0), 'p': (0x13, 0),
    'q': (0x14, 0), 'r': (0x15, 0), 's': (0x16, 0), 't': (0x17, 0),
    'u': (0x18, 0), 'v': (0x19, 0), 'w': (0x1A, 0), 'x': (0x1B, 0),
    'y': (0x1C, 0), 'z': (0x1D, 0),

    'A': (0x04, MOD_LSHIFT), 'B': (0x05, MOD_LSHIFT), 'C': (0x06, MOD_LSHIFT),
    'D': (0x07, MOD_LSHIFT), 'E': (0x08, MOD_LSHIFT), 'F': (0x09, MOD_LSHIFT),
    'G': (0x0A, MOD_LSHIFT), 'H': (0x0B, MOD_LSHIFT), 'I': (0x0C, MOD_LSHIFT),
    'J': (0x0D, MOD_LSHIFT), 'K': (0x0E, MOD_LSHIFT), 'L': (0x0F, MOD_LSHIFT),
    'M': (0x10, MOD_LSHIFT), 'N': (0x11, MOD_LSHIFT), 'O': (0x12, MOD_LSHIFT),
    'P': (0x13, MOD_LSHIFT), 'Q': (0x14, MOD_LSHIFT), 'R': (0x15, MOD_LSHIFT),
    'S': (0x16, MOD_LSHIFT), 'T': (0x17, MOD_LSHIFT), 'U': (0x18, MOD_LSHIFT),
    'V': (0x19, MOD_LSHIFT), 'W': (0x1A, MOD_LSHIFT), 'X': (0x1B, MOD_LSHIFT),
    'Y': (0x1C, MOD_LSHIFT), 'Z': (0x1D, MOD_LSHIFT),

    # Digits (top row)
    '1': (0x1E, 0), '2': (0x1F, 0), '3': (0x20, 0), '4': (0x21, 0),
    '5': (0x22, 0), '6': (0x23, 0), '7': (0x24, 0), '8': (0x25, 0),
    '9': (0x26, 0), '0': (0x27, 0),

    # Shifted top row symbols
    '!': (0x1E, MOD_LSHIFT),
    '@': (0x1F, MOD_LSHIFT),
    '#': (0x20, MOD_LSHIFT),
    '$': (0x21, MOD_LSHIFT),
    '%': (0x22, MOD_LSHIFT),
    '^': (0x23, MOD_LSHIFT),
    '&': (0x24, MOD_LSHIFT),
    '*': (0x25, MOD_LSHIFT),
    '(': (0x26, MOD_LSHIFT),
    ')': (0x27, MOD_LSHIFT),

    # Whitespace & control
    ' ': (0x2C, 0),
    '\n': (0x28, 0),   # Enter
    '\t': (0x2B, 0),   # Tab

    # Punctuation
    '-': (0x2D, 0), '_': (0x2D, MOD_LSHIFT),
    '=': (0x2E, 0), '+': (0x2E, MOD_LSHIFT),

    '[': (0x2F, 0), '{': (0x2F, MOD_LSHIFT),
    ']': (0x30, 0), '}': (0x30, MOD_LSHIFT),

    '\\': (0x31, 0), '|': (0x31, MOD_LSHIFT),

    ';': (0x33, 0), ':': (0x33, MOD_LSHIFT),
    "'": (0x34, 0), '"': (0x34, MOD_LSHIFT),

    '`': (0x35, 0), '~': (0x35, MOD_LSHIFT),

    ',': (0x36, 0), '<': (0x36, MOD_LSHIFT),
    '.': (0x37, 0), '>': (0x37, MOD_LSHIFT),
    '/': (0x38, 0), '?': (0x38, MOD_LSHIFT),
}

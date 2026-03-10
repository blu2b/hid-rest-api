from hid_keymap import KEYMAP_DE, KEYMAP_US
import time
import random

HID = "/dev/hidg0" # adjust if your HID gadget is at a different path

def send_report(modifier, keycode):
    with open(HID, "wb") as f:
        f.write(bytes([modifier, 0x00, keycode, 0, 0, 0, 0, 0])) # press
        f.write(b"\x00\x00\x00\x00\x00\x00\x00\x00")  # release

def type_text(text, layout):
    if (layout == "US") or (layout == "EN"):
         keymap = KEYMAP_US
    else:
        keymap = KEYMAP_DE

    for char in text:
        if char not in keymap:
            print(f"Skipping unsupported char: {char}")
            continue
        keycode, needs_shift = keymap[char]
        modifier = 0x02 if needs_shift else 0x00  # 0x02 = Left Shift
        send_report(modifier, keycode)
        # add small random dely
        processing_time = random.uniform(0.01, 0.05)
        time.sleep(processing_time)
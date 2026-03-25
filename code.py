import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
import time
import board
import digitalio

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

def make_button(pin):
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
    return button

buttons = [
    (make_button(board.GP0),  60),  # C4
    (make_button(board.GP1),  61),  # C#4
    (make_button(board.GP2),  62),  # D4
    (make_button(board.GP3),  63),  # D#4
    (make_button(board.GP4),  64),  # E4
    (make_button(board.GP5),  65),  # F4
    (make_button(board.GP6),  66),  # F#4
    (make_button(board.GP7),  67),  # G4
    (make_button(board.GP8),  68),  # G#4
    (make_button(board.GP9),  69),  # A4
    (make_button(board.GP10), 70),  # A#4
    (make_button(board.GP11), 71),  # B4
    (make_button(board.GP12), 72),  # C5
]

held = [False] * len(buttons)

while True:
    for i, (button,note) in enumerate(buttons):
        pressed = not button.value
        if pressed and not held[i]:
            midi.send(NoteOn(note, 127))
            held[i] = True
        elif not pressed and held[i]:
            midi.send(NoteOff(note, 0))
            held[i] = False

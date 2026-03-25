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
    (make_button(board.GP15), 60), #C
    (make_button(board.GP14), 62), #D
    (make_button(board.GP13), 64), #E
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

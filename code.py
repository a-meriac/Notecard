import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
import time
import board
import digitalio

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while True:
    if not button.value:
        midi.send(NoteOn(60, 120))
        while not button.value:
            pass
        midi.send(NoteOff(60, 120))

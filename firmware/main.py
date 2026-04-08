import board
import digitalio
import time
import pwmio
import analogio
import neopixel

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2, auto_write=True)

adc = analogio.AnalogIn(board.A0)

buzzer = pwmio.PWMOut(board.D10, duty_cycle=0, frequency=440)

def tone(freq, dur):
    buzzer.frequency = freq
    buzzer.duty_cycle = 32768
    time.sleep(dur)
    buzzer.duty_cycle = 0

def read():
    return adc.value / 65535

palette = [
    (255, 0, 64),
    (0, 128, 255),
    (0, 255, 128),
    (255, 255, 0),
    (180, 0, 255),
]

melody = [220, 330, 440, 660, 880]

i = 0
t = 0.05

while True:
    val = read()
    led.value = val > 0.5
    pixel[0] = palette[i % len(palette)]
    tone(melody[i % len(melody)], t + val * 0.1)
    i += 1
    time.sleep(0.1 + val * 0.2)

# Thumby game to test the circle library quality and performance

import thumby
from time import ticks_ms, ticks_us, ticks_diff, sleep_ms

GAME_DIR = '/Games/CirclePreview'
from sys import path
path.append(GAME_DIR)
import circles


thumby.display.setFPS(30)
thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)

last_ms = ticks_ms()
filled = False
mode = 0
modes = ['dsp', 'prf']


# Row Display

globalX = 0
previewCircles = []

def updateRow():
    global globalX

    if thumby.buttonL.pressed():
        globalX += 6

    if thumby.buttonR.pressed():
        globalX -= 6

    for previewCircle in previewCircles:
        previewCircle.draw()

class PreviewCircle:
    def __init__(self, x, diameter):
        self.x = x
        self.diameter = diameter

    def draw(self):
        x = self.x + globalX

        if x + (self.diameter / 2) >= 0 and x - (self.diameter / 2) < thumby.display.width:
            if filled:
                circles.drawFilledCircle(x, int(thumby.display.height / 2), self.diameter)
            else:
                circles.drawCircle(x, int(thumby.display.height / 2), self.diameter)

            numberX = x - 1
            numberX = numberX - 2 if self.diameter > 9 else numberX
            numberY = thumby.display.height - 5 if self.diameter < 29 else int(thumby.display.height / 2) - 2
            numberColour = 1 if filled is False or self.diameter < 29 else 0

            thumby.display.drawText(str(self.diameter), int(numberX), numberY, numberColour)

if hasattr(circles, 'circleSizes'):
    sizes = list(circles.circleSizes.keys())
    sizes.sort()
else:
    sizes = range(4, 65)

acumX = -2
for diameter in range(1, sizes[-1] + 1):
    evenExtra = 1 if (diameter % 2 == 0 or diameter == 1 or diameter == 3) else 0
    acumX = acumX + diameter + evenExtra
    x = acumX
    previewCircles.append(PreviewCircle(x, diameter))


# Profiler

tests = [
    4,
    8,
    12,
    19,
    24,
    28,
    31,
    35,
    39,
    42,
    47,
    50,
    54,
    61,
    64,
]
tests = sizes
results = []
globalY = 0

def updateProfiler():
    global tests, results, globalY

    if results:
        if thumby.buttonL.pressed():
            globalY += 3

        if thumby.buttonR.pressed():
            globalY -= 3

        for i, time in enumerate(results):
            y = globalY + 6 + (6 * i)

            if (y >= 0 and y < thumby.display.height):
                diameter = str(tests[i])
                if len(diameter) == 1:
                    diameter = '0' + diameter

                thumby.display.drawText(diameter + ': ' + str(time) + ' ms', 0, y, 1)
    else:
        times = 30

        for diameter in tests:
            total = 0

            for i in range(0, times):
                thumby.display.fill(0)
                start = ticks_us()
                if filled:
                    circles.drawFilledCircle(int(thumby.display.width / 2), int(thumby.display.height / 2), diameter)
                else:
                    circles.drawCircle(int(thumby.display.width / 2), int(thumby.display.height / 2), diameter)
                total += ticks_diff(ticks_us(), start)

            thumby.display.drawText('Running...', 0, 0, 1)
            thumby.display.update()

            results.append((total / times) / 1000)


while(1):
    now = ticks_ms()
    dt = ticks_diff(now, last_ms)
    last_ms = now

    if thumby.buttonU.justPressed():
        mode -= 1
        results = []

        if mode < 0:
            mode = len(modes) - 1

    if thumby.buttonD.justPressed():
        mode += 1
        results = []

        if mode > len(modes) - 1:
            mode = 0

    if thumby.buttonA.justPressed():
        filled = False if filled else True

    thumby.display.fill(0)

    if mode == 0:
        updateRow()
    elif mode == 1:
        updateProfiler()

    thumby.display.drawText(str(round(1000 / dt)), 0, 0, 1)
    thumby.display.drawText(modes[mode], 61, 0, 1)

    thumby.display.update()

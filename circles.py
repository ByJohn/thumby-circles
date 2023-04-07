# https://github.com/ByJohn/thumby-circles

import thumby
import math

# Supported circles diameters (including 1-3)
circleSizes = {
    4: [1],
    5: [1],
    6: [1],
    7: [2],
    8: [2],
    9: [2],
    10: [3, 1],
    11: [3, 2],
    12: [4, 2],
    13: [4, 2],
    14: [4, 3],
    15: [5, 3],
    16: [5, 3],
    17: [6, 4, 2],
    18: [6, 4, 3],
    19: [6, 4, 3],
    20: [7, 5, 3],
    21: [7, 5, 4],
    22: [8, 5, 4],
    23: [8, 6, 4],
    24: [9, 6, 5, 4],
    25: [9, 7, 5, 4],
    26: [9, 7, 5, 4],
    27: [10, 7, 6, 4],
    28: [10, 8, 6, 5],
    29: [11, 8, 6, 5],
    30: [11, 8, 7, 5],
    31: [12, 9, 7, 6, 5],
    32: [12, 9, 7, 6, 4],
}

def drawCircle(x, y, diameter, colour = 1):
    if diameter == 1:
        thumby.display.setPixel(x, y, colour)
        return
    elif diameter == 2:
        thumby.display.drawRectangle(x, y, 2, 2, colour)
        return
    elif diameter == 3:
        thumby.display.drawRectangle(x - 1, y - 1, 3, 3, colour)
        return

    evenModifier = -1 if diameter % 2 == 0 else 0 # Width/height reduction when the diamter is even

    radiusFloor = math.floor(diameter / 2)
    top = y - radiusFloor
    bottom = y + radiusFloor + evenModifier
    left = x - radiusFloor
    right = x + radiusFloor + evenModifier

    prevInset2 = circleSizes[diameter][0]

    # inset1 = loop iteration, inset2 = pixel offset
    for inset1, inset2 in enumerate(circleSizes[diameter]):
        if inset1 == 0:
            # Straight sides
            thumby.display.drawLine(left + inset2, top, right - inset2, top, colour) # Top
            thumby.display.drawLine(right, top + inset2, right, bottom - inset2, colour) # Right
            thumby.display.drawLine(right - inset2, bottom, left + inset2, bottom, colour) # Bottom
            thumby.display.drawLine(left, bottom - inset2, left, top + inset2, colour) # Left
        else:
            extra = prevInset2 - 1 - inset2 # Extra length possibly needed for this line

            # If the current inset2 has reduced by more than 1
            if extra > 0:
                # Draw lines
                thumby.display.drawLine(left + inset1, top + inset2, left + inset1, top + inset2 + extra, colour) # WNW
                thumby.display.drawLine(left + inset2, top + inset1, left + inset2 + extra, top + inset1, colour) # NNW
                thumby.display.drawLine(right - inset2, top + inset1, right - inset2 - extra, top + inset1, colour) # NNE
                thumby.display.drawLine(right - inset1, top + inset2, right - inset1, top + inset2 + extra, colour) # ENE
                thumby.display.drawLine(right - inset2, bottom - inset1, right - inset2 - extra, bottom - inset1, colour) # ESE
                thumby.display.drawLine(right - inset1, bottom - inset2, right - inset1, bottom - inset2 - extra, colour) # SSE
                thumby.display.drawLine(left + inset2, bottom - inset1, left + inset2 + extra, bottom - inset1, colour) # SSW
                thumby.display.drawLine(left + inset1, bottom - inset2, left + inset1, bottom - inset2 - extra, colour) # WSW
            else:
                # Otherwise draw dots
                thumby.display.setPixel(left + inset1, top + inset2, colour) # WNW
                thumby.display.setPixel(left + inset2, top + inset1, colour) # NNW
                thumby.display.setPixel(right - inset2, top + inset1, colour) # NNE
                thumby.display.setPixel(right - inset1, top + inset2, colour) # ENE
                thumby.display.setPixel(right - inset2, bottom - inset1, colour) # ESE
                thumby.display.setPixel(right - inset1, bottom - inset2, colour) # SSE
                thumby.display.setPixel(left + inset2, bottom - inset1, colour) # SSW
                thumby.display.setPixel(left + inset1, bottom - inset2, colour) # WSW

        prevInset2 = inset2

    # Possibly fill in the four corners
    if prevInset2 > len(circleSizes[diameter]):
        inset1 = inset1 + 1
        thumby.display.setPixel(left + inset1, top + inset1, colour) # NW
        thumby.display.setPixel(right - inset1, top + inset1, colour) # NE
        thumby.display.setPixel(right - inset1, bottom - inset1, colour) # SE
        thumby.display.setPixel(left + inset1, bottom - inset1, colour) # SW

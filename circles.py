import thumby
import math

# Supported circles diameters (including 1, 2 and 3)
circleSizes = {
    4: [1],
    5: [1],
    6: [1],
    7: [2, 1],
    8: [2, 1],
    9: [2, 1],
    10: [3, 1, 1],
    11: [3, 2, 1],
    12: [4, 2, 1, 1],
    13: [4, 2, 1, 1],
    14: [4, 3, 2, 1],
    15: [5, 3, 2, 1, 1],
    16: [5, 3, 2, 1, 1],
    17: [6, 4, 2, 2, 1, 1],
    18: [6, 4, 3, 2, 1, 1],
    19: [6, 4, 3, 2, 1, 1],
    20: [7, 5, 3, 2, 2, 1, 1],
    21: [7, 5, 4, 3, 2, 1, 1],
    22: [8, 5, 4, 3, 2, 1, 1, 1],
    23: [8, 6, 4, 3, 2, 2, 1, 1],
    24: [9, 6, 5, 4, 3, 2, 1, 1, 1],
    25: [9, 7, 5, 4, 3, 2, 2, 1, 1],
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

    for inset1, inset2 in enumerate(circleSizes[diameter]):
        extra = prevInset2 - 1 - inset2 # Extra length possibly needed for this line

        # If the current inset2 has reduced by more than 1
        if extra > 0:
            thumby.display.drawLine(left + inset1, top + inset2, left + inset1, top + inset2 + extra, colour) # Top left
            thumby.display.drawLine(right - inset2, top + inset1, right - inset2 - extra, top + inset1, colour) # Top right
            thumby.display.drawLine(right - inset1, bottom - inset2, right - inset1, bottom - inset2 - extra, colour) # Bottom right
            thumby.display.drawLine(left + inset2, bottom - inset1, left + inset2 + extra, bottom - inset1, colour) # Bottom left
        else:
            thumby.display.setPixel(left + inset1, top + inset2, colour) # Top left
            thumby.display.setPixel(right - inset2, top + inset1, colour) # Top right
            thumby.display.setPixel(right - inset1, bottom - inset2, colour) # Bottom right
            thumby.display.setPixel(left + inset2, bottom - inset1, colour) # Bottom left

        prevInset2 = inset2

    inset1 = inset1 + 1 # Increment once more for the straight sides

    thumby.display.drawLine(left + inset1, top, right - inset1, top, colour) # Top
    thumby.display.drawLine(right, top + inset1, right, bottom - inset1, colour) # Right
    thumby.display.drawLine(right - inset1, bottom, left + inset1, bottom, colour) # Bottom
    thumby.display.drawLine(left, bottom - inset1, left, top + inset1, colour) # Left

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
    33: [12, 9, 7, 6, 5],
    34: [13, 11, 9, 7, 6, 5],
    35: [13, 11, 9, 7, 6, 5],
    36: [14, 11, 9, 8, 7, 6],
    37: [15, 12, 10, 8, 7, 6],
    38: [15, 12, 10, 8, 7, 6],
    39: [15, 12, 10, 9, 7, 6],
    40: [16, 13, 11, 9, 8, 7],
    41: [16, 13, 11, 9, 8, 7],
    42: [17, 14, 12, 10, 9, 7],
    43: [18, 15, 13, 11, 9, 8, 7],
    44: [18, 15, 13, 11, 9, 8, 7],
    45: [18, 15, 13, 11, 9, 8, 7],
    46: [19, 15, 13, 11, 10, 9, 7],
    47: [19, 15, 13, 11, 10, 9, 7],
    48: [20, 16, 14, 12, 11, 9, 8],
    49: [20, 16, 14, 12, 11, 9, 8],
    50: [21, 17, 15, 13, 11, 10, 9, 8],
    51: [21, 17, 15, 13, 11, 10, 9, 8],
    52: [21, 18, 15, 13, 11, 10, 9, 8],
    53: [21, 18, 15, 13, 11, 10, 9, 8],
    54: [22, 19, 16, 14, 13, 11, 10, 9],
    55: [22, 19, 16, 14, 13, 11, 10, 9],
    56: [23, 19, 17, 15, 13, 12, 11, 9],
    57: [23, 19, 17, 15, 13, 12, 11, 9],
    58: [24, 20, 18, 16, 14, 13, 11, 10, 9],
    59: [24, 20, 18, 16, 14, 13, 11, 10, 9],
    60: [25, 21, 19, 16, 15, 13, 12, 11, 10, 9],
    61: [25, 21, 19, 16, 15, 13, 12, 11, 10, 9],
    62: [26, 22, 19, 17, 15, 14, 13, 11, 10],
    63: [26, 22, 19, 17, 15, 14, 13, 11, 10],
    64: [27, 23, 20, 18, 16, 15, 13, 12, 11, 10],
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

    evenModifier = -1 if diameter % 2 == 0 else 0 # Width/height reduction when the diameter is even

    # Cache objects
    setPixel = thumby.display.setPixel
    drawLine = thumby.display.drawLine
    steps = circleSizes.get(diameter, [])

    radiusFloor = math.floor(diameter / 2)
    top = y - radiusFloor
    bottom = y + radiusFloor + evenModifier
    left = x - radiusFloor
    right = x + radiusFloor + evenModifier

    prevInset2 = steps[0]

    # inset1 = loop iteration, inset2 = pixel offset
    for inset1, inset2 in enumerate(steps):
        if inset1 == 0:
            # Straight sides
            drawLine(left + inset2, top, right - inset2, top, colour) # Top
            drawLine(right, top + inset2, right, bottom - inset2, colour) # Right
            drawLine(right - inset2, bottom, left + inset2, bottom, colour) # Bottom
            drawLine(left, bottom - inset2, left, top + inset2, colour) # Left
        else:
            extra = prevInset2 - 1 - inset2 # Extra length possibly needed for this line

            # If the current inset2 has reduced by more than 1
            if extra > 0:
                # Draw lines
                drawLine(left + inset1, top + inset2, left + inset1, top + inset2 + extra, colour) # WNW
                drawLine(left + inset2, top + inset1, left + inset2 + extra, top + inset1, colour) # NNW
                drawLine(right - inset2, top + inset1, right - inset2 - extra, top + inset1, colour) # NNE
                drawLine(right - inset1, top + inset2, right - inset1, top + inset2 + extra, colour) # ENE
                drawLine(right - inset1, bottom - inset2, right - inset1, bottom - inset2 - extra, colour) # ESE
                drawLine(right - inset2, bottom - inset1, right - inset2 - extra, bottom - inset1, colour) # SSE
                drawLine(left + inset2, bottom - inset1, left + inset2 + extra, bottom - inset1, colour) # SSW
                drawLine(left + inset1, bottom - inset2, left + inset1, bottom - inset2 - extra, colour) # WSW
            else:
                # Otherwise draw dots
                setPixel(left + inset1, top + inset2, colour) # WNW
                setPixel(left + inset2, top + inset1, colour) # NNW
                setPixel(right - inset2, top + inset1, colour) # NNE
                setPixel(right - inset1, top + inset2, colour) # ENE
                setPixel(right - inset1, bottom - inset2, colour) # ESE
                setPixel(right - inset2, bottom - inset1, colour) # SSE
                setPixel(left + inset2, bottom - inset1, colour) # SSW
                setPixel(left + inset1, bottom - inset2, colour) # WSW

        prevInset2 = inset2

    # Possibly fill in the four corners
    if prevInset2 > len(steps):
        inset1 = inset1 + 1
        setPixel(left + inset1, top + inset1, colour) # NW
        setPixel(right - inset1, top + inset1, colour) # NE
        setPixel(right - inset1, bottom - inset1, colour) # SE
        setPixel(left + inset1, bottom - inset1, colour) # SW

def drawFilledCircle(x, y, diameter, colour = 1):
    if diameter == 1 or diameter == 2:
        drawCircle(x, y, diameter, colour)
        return

    # Cache objects
    setPixel = thumby.display.setPixel
    drawLine = thumby.display.drawLine
    drawFilledRectangle = thumby.display.drawFilledRectangle
    steps = circleSizes.get(diameter, [])

    if diameter == 3:
        setPixel(x, y, colour)
        setPixel(x - 1, y, colour)
        setPixel(x + 1, y, colour)
        setPixel(x, y - 1, colour)
        setPixel(x, y + 1, colour)
        return

    evenModifier = -1 if diameter % 2 == 0 else 0 # Width/height reduction when the diameter is even

    radiusFloor = math.floor(diameter / 2)
    top = y - radiusFloor
    bottom = y + radiusFloor + evenModifier
    left = x - radiusFloor
    right = x + radiusFloor + evenModifier

    prevInset2 = steps[0]

    # inset1 = loop iteration, inset2 = pixel offset
    for inset1, inset2 in enumerate(steps):
        if inset1 == 0:
            # Straight sides
            drawFilledRectangle(left, top + inset2, diameter, (bottom - inset2) - (top + inset2) + 1, colour) # Left-right
            drawLine(left + inset2, top, right - inset2, top, colour) # Top
            drawLine(right - inset2, bottom, left + inset2, bottom, colour) # Bottom
        else:
            extra = prevInset2 - 1 - inset2 # Extra length possibly needed for this line

            # If the current inset2 has reduced by more than 1
            if extra > 0:
                # Draw rectangles
                drawLine(left + inset2, top + inset1, right - inset2, top + inset1, colour) # Upper outer
                drawFilledRectangle(left + inset1, top + inset2, (right - inset1) - (left + inset1) + 1, 1 + extra, colour) # Upper inner
                drawFilledRectangle(left + inset1, bottom - inset2 - extra, (right - inset1) - (left + inset1) + 1, 1 + extra, colour) # Lower inner
                drawLine(left + inset2, bottom - inset1, right - inset2, bottom - inset1, colour) # Lower outer
            else:
                # Otherwise draw horizontal lines
                drawLine(left + inset2, top + inset1, right - inset2, top + inset1, colour) # Upper outer
                drawLine(left + inset1, top + inset2, right - inset1, top + inset2, colour) # Upper inner
                drawLine(left + inset1, bottom - inset2, right - inset1, bottom - inset2, colour) # Lower inner
                drawLine(left + inset2, bottom - inset1, right - inset2, bottom - inset1, colour) # Lower outer

        prevInset2 = inset2

    # Possibly fill in the two middle lines
    if prevInset2 > len(steps):
        inset1 = inset1 + 1
        drawLine(left + inset1, top + inset1, right - inset1, top + inset1, colour) # Upper
        drawLine(left + inset1, bottom - inset1, right - inset1, bottom - inset1, colour) # Lower

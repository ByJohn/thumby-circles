# Thumby Circles
Circle MicroPython library for the [Thumby](https://thumby.us/) games console.

## Usage

```python
import circles

# Displays a hollow circle with a diameter of 12 centred at position 36,20.
circles.drawCircle(36, 20, 12)

# Displays a filled circle with a diameter of 6 centred at position 10,15.
circles.drawFilledCircle(10, 15, 6)
```

## Testing
`CirclePreview.py` is a dedicated Thumby game to test the quality and performance of the circles library.
Add all the files to `/Games/CirclePreview/` on your Thumby and run `/Games/CirclePreview/CirclePreview.py`.

## Method
As a compromise between render speed and file size, the circles are not computed mathematically per se. Instead, pixel drawing instructions are manually pre-calculated for an eighth of a circle of each diameter. The pixels are draw with eight-way symmetry to complete the circle. It draws a circle in a similar way to the [midpoint circle algorithm](https://en.wikipedia.org/wiki/Midpoint_circle_algorithm) except the points are pre-calculated and the flat sides are drawn all at once. The filled circles are drawn with the same inputs but use horizontal lines to fill the shape.

## Supported Circle Sizes
By default, circles with a diameter between 1-64 are supported. These are defined in the `circleSizes` object. You can add you own sizes or remove ones that you do not need (to save space).

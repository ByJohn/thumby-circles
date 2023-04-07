# Thumby Circles
Circle MicroPython library for the [Thumby](https://thumby.us/) games console.

## Usage

```python
import circles

# Displays a hollow circle with a diameter of 12 centred at position 36,20.
circles.drawCircle(36, 20, 12)
```

## Method
As a compromise between render speed and file size, the circles are not computed mathematically per se. Instead, pixel drawing instructions are manually pre-calculated for an eighth of a circle of each diameter. The pixels are draw with eight-way symmetry to complete the circle. It draws a circle in a similar way to the [midpoint circle algorithm](https://en.wikipedia.org/wiki/Midpoint_circle_algorithm) except the points are pre-calculated and the flat sides are drawn all at once.

## Supported Circle Sizes
By default, circles with a diameter between 1-25 are supported. These are defined in the `circleSizes` object. You can add you own sizes or remove ones that you do not need (to save space).

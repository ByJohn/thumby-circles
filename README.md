# Thumby Circles
Circle MicroPython library for the [Thumby](https://thumby.us/) games console.

## Method
As a compromise between render speed and file size, the circles are not computed mathematically per se. Instead, pixel drawing instructions are manually pre-calculated for a quarter circle of each diameter. The pixels are draw with four-way symmetry to complete the circle.

## Usage

```python
import circles

# Displays a white (1), hollow circle with a diameter of 12 centred at position 36,20.
drawCircle(36, 20, 12, 1)
```
## Supported Circle Sizes
By default, circles with a diameter between 1-25 are supported. These are defined in the `circleSizes` object. You can add you own sizes or remove ones that you do not need (to save space).

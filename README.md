# Thumby Circles
Circle MicroPython library for the [Thumby](https://thumby.us/) games console.

## Usage

```python
import circles

# Display a hollow circle with a diameter of 12 centred at position 36,20.
circles.drawCircle(36, 20, 12)

# Display a filled circle with a diameter of 6 centred at position 10,15.
circles.drawFilledCircle(10, 15, 6)
```

## Testing
`CirclePreview.py` is a dedicated Thumby game to test the quality and performance of the circles library.
Add all the files to `/Games/CirclePreview/` on your Thumby and run `/Games/CirclePreview/CirclePreview.py`.

## Drawing Method
As a compromise between render speed and file size, the circles are not computed mathematically per se. Instead, pixel drawing instructions are manually pre-calculated for an eighth of a circle of each diameter. The pixels are drawn with eight-way symmetry to complete the circle.

The circles are drawn in a similar way to the [midpoint circle algorithm](https://en.wikipedia.org/wiki/Midpoint_circle_algorithm) except the pixel positions are pre-calculated (relative to the circle centre) and the flat sides are drawn all at once. The filled circles are drawn with the same inputs but use horizontal lines to fill the shape.

### Drawing Performance
Tests conducted using `CirclePreview.py` running on a real Thumby device (purchased 2023) with MicroPython v1.19.1.

| Circle Type | Diameter 4 | Diameter 64 |
| --- | --- | --- |
| Hollow | 0.43 ms | 2.47 ms |
| Filled | 0.45 ms | 4.04 ms |

#### Midpoint Circle Algorithm Implementation (for comparison)

| Circle Type | Diameter 4 | Diameter 64 |
| --- | --- | --- |
| Hollow | 1.46 ms | 12.06 ms |
| Filled | N/A | N/A |

## Supported Circle Sizes
By default, circles with a diameter between 1-64 are supported. These are defined in the `circleSizes` object. You can add you own sizes or remove ones that you do not need (to save space).

# thumby-circles
Circle library for the [Thumby console](https://thumby.us/).

As a compromise between generation speed and file size, the circles are not computed mathematically per se. Instead, pixel point locations for each circle size is pre-calculated manually for one quarter circle. The pixels are draw in a four-way symmetry to complete a circle.

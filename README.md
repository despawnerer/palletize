palletize
=========

[![PyPI version](https://badge.fury.io/py/palletize.svg)](https://badge.fury.io/py/palletize)

`palletize` extracts dominant colors from images using K-means algorithm. Meant to be used as a library, CLI script is included for ease of testing.

It uses pillow, numpy and scipy, so it's slow to initialize, but pretty snappy afterwards. K-means is a bit random, so expect results for the same image to vary slightly from time to time.


Installation
------------

	$ pip install palletize


Usage
-----

### Library

```python
from palletize import extract_dominant_colors

extract_dominant_colors(file_or_filename, count=3, clusters=None, iterations=30, resize_to=300)
```

Return a list of `count` dominant colors from the image as 3-tuples `(r, g, b)`.

- `count` is the number of colors you want to get;
- `clusters` is the number of color groups to build from the image before getting `count` of dominant colors, by default it's the same as `count` if you're extracting more than one color, or `3` if `count` is 1;
- `iterations` is the number of iterations for the algorithm to go through before settling: the higher it is, the better and more stable are the results, but the longer it takes;
- `resize_to` is the pixel size of the larger side of the image to downscale it to speed up processing: pass `None` to disable downscaling.


### CLI

```bash
palletize filename [filename ...]
```

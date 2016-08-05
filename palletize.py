from numpy import reshape, unique, argsort
from scipy.misc import imread, imresize
from scipy.cluster.vq import kmeans2


__all__ = ['extract_dominant_colors']


def extract_dominant_colors(
        file_or_filename, count=3, clusters=None, iterations=30,
        resize_to=300):
    assert count > 0
    assert clusters is None or clusters >= count
    assert iterations > 0
    assert resize_to > 0

    if clusters is None:
        clusters = count if count > 1 else 3

    # load and downsample the image
    image = imread(file_or_filename)
    width, height = image.shape[0], image.shape[1]
    if resize_to is not None:
        ratio = resize_to / max(width, height)
        width = int(width * ratio)
        height = int(height * ratio)
        image = imresize(image, (width, height))

    # find centroids of color clusters
    pixels = reshape(image, (width * height, 3))
    centroids, labels = kmeans2(
        pixels.astype(float), clusters, iterations, minit='points',
        check_finite=False,
    )

    # reorder them by prominence
    _, counts = unique(labels, return_counts=True)
    best_centroid_indices = argsort(counts)[::-1]
    dominant_colors = centroids[best_centroid_indices].astype(int)

    return [tuple(color) for color in dominant_colors[:count]]

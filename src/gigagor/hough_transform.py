import numpy as np
from typing import Tuple


def merge_histograms(h1: np.ndarray, h2: np.ndarray) -> np.ndarray:
    height: int = h1.shape[0]
    width: int = 1 if len(h1.shape) == 1 else h1.shape[1]
    n0: int = width * 2
    r: float = (width - 1) / (n0 - 1)
    h1, h2 = h1.reshape((height, width)), h2.reshape((height, width))
    result: np.ndarray = np.zeros((height, n0))
    for t in range(n0):
        t0: int = int(t * r)
        s: int = t - t0
        result[:, t] = h1[:, t0] + np.concatenate(
            [h2[s:height, t0], h2[0:s, t0]], axis=0
        )
    return result


def fast_hough_transform(Picture: np.ndarray) -> np.ndarray:
    n: int = Picture.shape[1]
    if n < 2:
        return Picture[:, 0]
    else:
        return merge_histograms(
            fast_hough_transform(Picture[:, 0 : int(n / 2)]),
            fast_hough_transform(Picture[:, int(n / 2) : n]),
        )


def find_max_value(picture: np.ndarray) -> Tuple[float, Tuple[float, float]]:
    result: float = 0
    a, b = picture.shape
    s, t = 0.0, 0.0
    for i in range(a):
        for j in range(b):
            if picture[i, j] > result:
                result = picture[i, j]
                s = i
                t = j
    return result, tuple((s, t))


def find_point(n: int, s: float, t: float) -> float:
    x: float = round((n - s) * n / t)
    return x

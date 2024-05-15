import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from .hough_transform import fast_hough_transform, find_max_value, find_point
from typing import Tuple, Union


def draw_line(
    image: np.ndarray, start: int, thickness: int, height: int, width: int
) -> np.ndarray:
    modified_image: np.ndarray = image.copy()
    line_thickness: int = 2
    if start + thickness > height:
        x_0: int = find_point(height, start, thickness)
        zero_matrix: np.ndarray = np.zeros((height, width))
        stacked_upper: np.ndarray = np.vstack([zero_matrix, image])[
            start : start + height, :
        ]
        stacked_lower: np.ndarray = np.vstack([image, zero_matrix])[
            start : start + height, :
        ]
        max_up: Tuple[float] = (find_max_value(fast_hough_transform(stacked_upper)),)
        max_low: Tuple[float] = (find_max_value(fast_hough_transform(stacked_lower)),)

        if max_up[0] > max_low[0]:
            cv.line(
                modified_image,
                (x_0, 0),
                (width - 1, start + thickness - height),
                (64, 0, 0),
                line_thickness,
            )
        else:
            cv.line(
                modified_image, (x_0, height), (0, start), (64, 0, 0), line_thickness
            )
        plt.imshow(modified_image)
    else:
        plt.imshow(
            cv.line(
                modified_image,
                (0, start),
                (width - 1, start + thickness),
                (64, 0, 0),
                line_thickness,
            )
        )
    return modified_image


def hough_transform(
    image: np.ndarray, threshold_ratio: float = 0.9, draw_lines: int = 0
) -> Union[Tuple[float, np.ndarray], Tuple[float, np.ndarray, np.ndarray]]:
    hough_space: np.ndarray = fast_hough_transform(image)
    print("after fast_hough")
    max_intensity, _ = find_max_value(hough_space)
    print("after find_max")
    threshold: float = max_intensity * threshold_ratio
    lines: np.ndarray = np.argwhere(hough_space >= threshold)
    height, width = image.shape
    if draw_lines != 0:
        image_with_lines: np.ndarray = image.copy()
        for start, thickness in lines:
            image_with_lines = draw_line(
                image_with_lines, start, thickness, height, width
            )
        return max_intensity, hough_space, image_with_lines
    else:
        return max_intensity, hough_space

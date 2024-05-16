"""Test module."""

import cv2  # type: ignore
import numpy as np  # type: ignore

from fast_hough_transform.draw_line import hough_transform
from fast_hough_transform.image_processing import read_image

FOLDER = "images/"


def transform_pixels(array: np.ndarray) -> np.array:
    """Transforms all non-zero pixels in the input array to 64.

    Args:
        array (np.ndarray): The input array.

    Returns:
        np.ndarray: The transformed array.
    """
    transformed_array = np.where(array != 0, 64, array)
    return transformed_array


def compare_images_with_lines(
    image1: np.ndarray, image2: np.ndarray, threshold: float = 0.7
) -> bool:
    """Compares two images to determine if they have similar lines drawn.

    Args:
        image1 (np.ndarray): The first image.
        image2 (np.ndarray): The second image.
        threshold (float): The correlation threshold. Defaults to 0.7.

    Returns:
        bool: True if the images have similar lines, False otherwise.
    """
    image1 = transform_pixels(image1)
    correlation = cv2.matchTemplate(image1, image2, cv2.TM_CCOEFF_NORMED)[0][0]
    return correlation >= threshold


def transform_rgb_pixels(array: np.ndarray) -> np.ndarray:
    """Transforms all non-dominant pixels in the input RGB array to 64.

    Args:
        array (np.ndarray): The input RGB array.

    Returns:
        np.ndarray: The transformed RGB array.
    """
    array_1d = array.flatten()
    unique_values, counts = np.unique(array_1d, return_counts=True)
    most_common_index = np.argmax(counts)
    most_common_value = unique_values[most_common_index]
    transformed_array = np.where(array != most_common_value, 64, array)
    return transformed_array


def compare_rgb_images_with_lines(
    image1: np.ndarray, image2: np.ndarray, threshold: float = 0.7
) -> bool:
    """Compares two RGB images to determine if they have similar lines drawn.

    Args:
        image1 (np.ndarray): The first RGB image.
        image2 (np.ndarray): The second RGB image.
        threshold (float): The correlation threshold. Defaults to 0.7.

    Returns:
        bool: True if the images have similar lines, False otherwise.
    """
    image1 = transform_rgb_pixels(image1)
    correlation = cv2.matchTemplate(image1, image2, cv2.TM_CCOEFF_NORMED)[0][0]
    return correlation >= threshold


def fill_blanks_rows(array_2d: np.ndarray) -> np.ndarray:
    """Fills blank rows in a 2D array with values from non-blank rows above.

    Args:
        array_2d (np.ndarray): The input 2D array.

    Returns:
        np.ndarray: The array with filled rows.
    """
    nonzero_rows = np.nonzero(np.sum(array_2d, axis=1))[0]

    if len(nonzero_rows) > 0:
        for row in nonzero_rows:
            value = array_2d[row, np.nonzero(array_2d[row])[0][0]]
            array_2d[row][array_2d[row] == 0] = value
    return array_2d


def fill_blanks_cols(array_2d: np.ndarray) -> np.ndarray:
    """Fills blank columns in a 2D array with values from non-blank columns to the left.

    Args:
        array_2d (np.ndarray): The input 2D array.

    Returns:
        np.ndarray: The array with filled columns.
    """
    nonzero_cols = np.nonzero(np.sum(array_2d, axis=0))[0]
    if len(nonzero_cols) > 0:
        for col in nonzero_cols:
            value = array_2d[np.nonzero(array_2d[:, col])[0][0], col]
            array_2d[:, col][array_2d[:, col] == 0] = value
    return array_2d


# In these tests we compare the lines from the original picture
# with the lines drawn after the function hough_transform
class TestClass:
    """Test class for the hough_transform function."""

    def test_horizontal(self: object) -> None:
        """Tests the hough_transform function on a horizontal line image."""
        img_new = read_image(FOLDER, "horizontal_line.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_images_with_lines(img_new, line_img) is True

    def test_vertical(self: object) -> None:
        """Tests the hough_transform function on a vertical line image."""
        img_new = read_image(FOLDER, "vertical_line.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_images_with_lines(img_new, line_img) is True

    def test_small_hor(self: object) -> None:
        """Tests the hough_transform function on a small horizontal line image (3x3)."""
        img_new = read_image(FOLDER, "horizontal_line_3x3.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_images_with_lines(img_new, line_img) is True

    def test_small_ver(self: object) -> None:
        """Tests the hough_transform function on a small vertical line image (3x3)."""
        img_new = read_image(FOLDER, "vertical_line_3x3.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_images_with_lines(img_new, line_img) is True

    def test_long_hor_1(self: object) -> None:
        """Tests the hough_transform function on a long horizontal line image (10x500)."""
        img_new = read_image(FOLDER, "horizontal_line_10x500.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_images_with_lines(img_new, line_img) is True

    def test_long_hor_2(self: object) -> None:
        """Tests the hough_transform function on a long vertical line image (500x10)."""
        img_new = read_image(FOLDER, "vertical_line_500x10.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_images_with_lines(img_new, line_img) is True

    def test_many_lines(self: object) -> None:
        """Tests the hough_transform function on an image with multiple lines."""
        img_new = read_image(FOLDER, "lines.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_images_with_lines(img_new, line_img) is True

    def test_many_rotated_lines(self: object) -> None:
        """Tests the hough_transform function on an image with multiple rotated lines."""
        img_new = read_image(FOLDER, "image_2.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_images_with_lines(img_new, line_img) is True

    def test_blured(self: object) -> None:
        """Tests the hough_transform function on a blurred image."""
        img_new = read_image(FOLDER, "blured.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_images_with_lines(img_new, line_img) is True

    def test_rotated_1(self: object) -> None:
        """Tests the hough_transform function on a rotated image."""
        img_new = read_image(FOLDER, "rotated.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_images_with_lines(img_new, line_img) is True

    def test_rectangle(self: object) -> None:
        """Tests the hough_transform function on an image with rectangle shape."""
        img_new = read_image(FOLDER, "rectangle1.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_images_with_lines(img_new, line_img) is True

    def test_rotated_2(self: object) -> None:
        """Tests the hough_transform function on another rotated image."""
        img_new = read_image(FOLDER, "rotated.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_images_with_lines(img_new, line_img) is True

    def test_intermittent_2_small_holes(self: object) -> None:
        """Tests the hough_transform function on an image with intermittent lines and small holes."""
        img_new = read_image(FOLDER, "intermittent.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        img = fill_blanks_rows(img_new)
        assert compare_images_with_lines(img, line_img) is True

    def test_intermittent_4_wide_holes(self: object) -> None:
        """Tests the hough_transform function on an image with intermittent lines and wide holes."""
        img_new = read_image(FOLDER, "intermittent2.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        img = fill_blanks_rows(img_new)
        assert compare_images_with_lines(img, line_img) is True

    def test_intermittent_vertical(self: object) -> None:
        """Tests the hough_transform function on an image with intermittent vertical lines."""
        img_new = read_image(FOLDER, "intermittent3.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        img = fill_blanks_cols(img_new)
        assert compare_images_with_lines(img, line_img) is True

    def test_wide(self: object) -> None:
        """Tests the hough_transform function on an image with a wide line."""
        img_new = read_image(FOLDER, "wide_line.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_images_with_lines(img_new, line_img) is True

    def test_rgb_1(self: object) -> None:
        """Tests the hough_transform function on an RGB image."""
        img_new = read_image(FOLDER, "rgb1.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_rgb_images_with_lines(img_new, line_img) is True

    def test_rgb_2(self: object) -> None:
        """Tests the hough_transform function on another RGB image."""
        img_new = read_image(FOLDER, "rgb2.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_rgb_images_with_lines(img_new, line_img) is True

    def test_rgb_3(self: object) -> None:
        """Tests the hough_transform function on yet another RGB image."""
        img_new = read_image(FOLDER, "rgb3.png")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_rgb_images_with_lines(img_new, line_img) is True

    def test_jpg(self: object) -> None:
        """Tests the hough_transform function on a JPG image."""
        img_new = read_image(FOLDER, "horizontal_line.jpg")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_rgb_images_with_lines(img_new, line_img) is True

    def test_jpeg(self: object) -> None:
        """Tests the hough_transform function on a JPEG image."""
        img_new = read_image(FOLDER, "horizontal_line.jpeg")
        res = hough_transform(img_new)
        line_img = len(res) > 2 and res[2] or None
        assert compare_rgb_images_with_lines(img_new, line_img) is True

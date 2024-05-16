"""Main module."""

from typing import Any

import matplotlib.pyplot as plt  # type: ignore

from fast_hough_transform.draw_line import hough_transform
from fast_hough_transform.image_processing import read_image

if __name__ == "__main__":
    """Main script to perform Hough transform on an image and save the results.

    Reads an image, performs Hough transform to detect lines, and saves the resulting images.

    """
    FOLDER: str = "images/"
    print("Input picture file name from /images folder:")

    pic_name: str = input()

    img_new: Any = read_image(FOLDER, pic_name)

    max_hft: float
    obr: Any
    line_img: Any
    res = hough_transform(img_new)
    max_hft, obr = res[0], res[1]
    line_img = len(res) > 2 and res[2] or None
    fig, ax = plt.subplots()
    ax.imshow(obr)
    fig.set_figwidth(12)
    fig.set_figheight(12)
    fig.suptitle("Hough Image")
    fig.savefig(f"test_output/hough_{pic_name}")

    fig, ax = plt.subplots()
    ax.imshow(line_img)
    fig.set_figwidth(12)
    fig.set_figheight(12)
    fig.suptitle("Hough Lines Image")
    fig.savefig(f"test_output/line_img_{pic_name}")

"""Image processing module."""

import cv2 as cv  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import numpy as np  # type: ignore


def read_image(FOLDER: str, name: str) -> np.ndarray:
    """Reads an image from the specified folder with the given name and performs resizing.

    Args:
        FOLDER (str): The folder path where the image is located.
        name (str): The name of the image file.

    Returns:
        np.ndarray: The resized image as a NumPy array.
    """
    final_img: np.ndarray = cv.imread(FOLDER + name, cv.IMREAD_GRAYSCALE)
    print("after final_img", final_img.shape)
    h, w = final_img.shape[:2]

    new_h: int = int(2 ** int(np.ceil(np.log2(h))))
    new_w: int = int(2 ** int(np.ceil(np.log2(w))))

    resized_img: np.ndarray = cv.resize(
        final_img, (new_w, new_h), interpolation=cv.INTER_LINEAR
    )

    plt.imshow(resized_img)
    return resized_img

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def read_image(FOLDER: str, name: str) -> np.ndarray:
    final_img: np.ndarray = cv.imread(FOLDER + name, cv.IMREAD_GRAYSCALE)
    print("after final_img", final_img.shape)
    h, w = final_img.shape[:2]

    new_h: int = 2 ** int(np.ceil(np.log2(h)))
    new_w: int = 2 ** int(np.ceil(np.log2(w)))

    resized_img: np.ndarray = cv.resize(
        final_img, (new_w, new_h), interpolation=cv.INTER_LINEAR
    )

    plt.imshow(resized_img)
    return resized_img

import matplotlib.pyplot as plt
from .image_processing import read_image
from .draw_line import hough_transform
from typing import Any

if __name__ == "__main__":
    FOLDER: str = "images/"
    print("Input picture file name from /images folder:")

    pic_name: str = input()
    # fig, ax = plt.subplots()
    # fig.set_figwidth(12)
    # fig.set_figheight(12)
    # fig.suptitle("Input Image")
    img_new: Any = read_image(FOLDER, pic_name)

    # fig, ax = plt.subplots()
    # fig.set_figwidth(12)
    # fig.set_figheight(12)
    # fig.suptitle("Lines Image")
    max_hft: float
    obr: Any
    line_img: Any
    max_hft, obr, line_img = hough_transform(img_new, draw=1)

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

    # plt.show()

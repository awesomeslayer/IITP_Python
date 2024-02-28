import cv2 as cv
import matplotlib.pyplot as plt

def read_image(folder, name):
    flow_img = cv.imread(folder + name)
    final_img = cv.imread(folder + name, flow_img.shape[0] * 2)
    plt.imshow(final_img)
    return final_img

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def read_image(FOLDER, name):
    final_img = cv.imread(FOLDER + name, cv.IMREAD_GRAYSCALE)
    print('after final_img',final_img.shape)
    h, w = final_img.shape[:2]
    
    new_h = 2 ** int(np.ceil(np.log2(h)))
    new_w = 2 ** int(np.ceil(np.log2(w)))

    resized_img = cv.resize(final_img, (new_w, new_h), interpolation=cv.INTER_LINEAR)
    
    plt.imshow(resized_img)
    return resized_img


import matplotlib.pyplot as plt
from image_processing import read_image
from hough_transform import fast_hough_transform, find_max_value
from draw_line import draw_line, hough_transform

if __name__ == '__main__':
    FOLDER = 'images/'
    print('Input picture file name from /images folder:')
    pic_name = input() 
    fig, ax = plt.subplots()
    fig.set_figwidth(12)    
    fig.set_figheight(12)
    fig.suptitle("Input Image")
    img_new = read_image(FOLDER, pic_name)

    fig, ax = plt.subplots()
    fig.set_figwidth(12)    
    fig.set_figheight(12)
    fig.suptitle("Lines Image")
    max_hft, obr = hough_transform(img_new, draw=1)

    fig, ax = plt.subplots()
    ax.imshow(obr)
    fig.set_figwidth(12)    
    fig.set_figheight(12)
    fig.suptitle("Hough Image")
    plt.show()

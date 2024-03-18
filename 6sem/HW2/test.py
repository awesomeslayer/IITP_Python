import cv2
import numpy as np
from draw_line import draw_line, hough_transform
from image_processing import read_image
FOLDER = 'images/'

# In this function we transform all pixels of the line in the source picture to 64 
#in order to compare it with the picture from the function, because there is a replacement by 64 there
def transform_pixels(array):
    transformed_array = np.where(array != 0, 64, array)
    return transformed_array

def compare_images_with_lines(image1, image2, threshold=0.7):
    image1 = transform_pixels(image1)
    correlation = cv2.matchTemplate(image1, image2, cv2.TM_CCOEFF_NORMED)[0][0]
    return correlation >= threshold

def transform_rgb_pixels(array):
    array_1d = array.flatten()
    unique_values, counts = np.unique(array_1d, return_counts=True)
    most_common_index = np.argmax(counts)
    most_common_value = unique_values[most_common_index]
    transformed_array = np.where(array != most_common_value, 64, array)
    print(most_common_value)
    return transformed_array

def compare_rgb_images_with_lines(image1, image2, threshold=0.7):
    image1 = transform_rgb_pixels(image1)
    correlation = cv2.matchTemplate(image1, image2, cv2.TM_CCOEFF_NORMED)[0][0]
    return correlation >= threshold

def fill_blanks_rows(array_2d):
    nonzero_rows = np.nonzero(np.sum(array_2d, axis=1))[0]

    if len(nonzero_rows) > 0:
        for row in nonzero_rows:
            value = array_2d[row, np.nonzero(array_2d[row])[0][0]]
            array_2d[row][array_2d[row] == 0] = value
    return array_2d


def fill_blanks_cols(array_2d):
    nonzero_cols = np.nonzero(np.sum(array_2d, axis=0))[0]
    if len(nonzero_cols) > 0:
        for col in nonzero_cols:
            value = array_2d[np.nonzero(array_2d[:, col])[0][0], col]
            array_2d[:, col][array_2d[:, col] == 0] = value
    return array_2d

#In these tests we compare the lines from the original picture 
#with the lines drawn after the function hough_transform
class TestClass:
    def test_horizontal(self):
        img_new = read_image(FOLDER, 'horizontal_line.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_images_with_lines(img_new, line_img) == True)

    def test_vertical(self):
        img_new = read_image(FOLDER, 'vertical_line.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_images_with_lines(img_new, line_img) == True)

    def test_small_hor(self):
        img_new = read_image(FOLDER, 'horizontal_line_3x3.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_images_with_lines(img_new, line_img) == True)

    def test_small_ver(self):
        img_new = read_image(FOLDER, 'vertical_line_3x3.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_images_with_lines(img_new, line_img) == True)

    def test_long_hor(self):
        img_new = read_image(FOLDER, 'horizontal_line_10x500.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_images_with_lines(img_new, line_img) == True)

    def test_long_hor(self):
        img_new = read_image(FOLDER, 'vertical_line_500x10.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_images_with_lines(img_new, line_img) == True)

    def test_many_lines(self):
        img_new = read_image(FOLDER, 'lines.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_images_with_lines(img_new, line_img) == True)
    
    def test_many_rotated_lines(self):
        img_new = read_image(FOLDER, 'image_2.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_images_with_lines(img_new, line_img) == True)
    
    def test_blured(self):
        img_new = read_image(FOLDER, 'blured.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_images_with_lines(img_new, line_img) == True)
    
    def test_rotated(self):
        img_new = read_image(FOLDER, 'rotated.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_images_with_lines(img_new, line_img) == True)
    
    def test_rectangle(self):
        img_new = read_image(FOLDER, 'rectangle1.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_images_with_lines(img_new, line_img) == True)
    
    def test_rotated(self):
        img_new = read_image(FOLDER, 'rotated.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_images_with_lines(img_new, line_img) == True)
    
    def test_intermittent_2_small_holes(self):
        img_new = read_image(FOLDER, 'intermittent.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        img = fill_blanks_rows(img_new)
        assert(compare_images_with_lines(img, line_img) == True)
    
    def test_intermittent_4_wide_holes(self):
        img_new = read_image(FOLDER, 'intermittent2.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        img = fill_blanks_rows(img_new)
        assert(compare_images_with_lines(img, line_img) == True)
        
    def test_intermittent_vertical(self):
        img_new = read_image(FOLDER, 'intermittent3.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        img = fill_blanks_cols(img_new)
        assert(compare_images_with_lines(img, line_img) == True)

    def test_wide(self):
        img_new = read_image(FOLDER, 'wide_line.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_images_with_lines(img_new, line_img) == True)
    
    def test_rgb_1(self):
        img_new = read_image(FOLDER, 'rgb1.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_rgb_images_with_lines(img_new, line_img) == True)
    
    def test_rgb_2(self):
        img_new = read_image(FOLDER, 'rgb2.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_rgb_images_with_lines(img_new, line_img) == True)
    
    def test_rgb_3(self):
        img_new = read_image(FOLDER, 'rgb3.png')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_rgb_images_with_lines(img_new, line_img) == True) 

    def test_jpg(self):
        img_new = read_image(FOLDER, 'horizontal_line.jpg')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_rgb_images_with_lines(img_new, line_img) == True) 
    
    def test_jpeg(self):
        img_new = read_image(FOLDER, 'horizontal_line.jpeg')
        _, _, line_img= hough_transform(img_new, draw=1)
        assert(compare_rgb_images_with_lines(img_new, line_img) == True) 
    






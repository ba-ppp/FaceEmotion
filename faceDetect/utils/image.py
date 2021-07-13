import cv2
from utils.math import solve_equation_2_var

def crop_image(img, box, constant): # crop object image and save
    h, w, c = img.shape
    w *= constant
    h *= constant
    img = cv2.resize(img, (0, 0), fx=constant, fy=constant)

    x1, x2 = solve_equation_2_var(2 * box[0] * w, box[2] * w)
    y1, y2 = solve_equation_2_var(2 * box[1] * h, box[3] * h)

    crop = img[y1:y2,x1:x2]
    return crop
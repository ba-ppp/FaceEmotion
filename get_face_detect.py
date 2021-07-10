from utils.file import *
from utils.image import crop_image
import cv2

image_path = 'data'
create_folder_result(image_path + '/result')
images = loop_all_files(image_path) # get all images

for image in images:
    img = cv2.imread(image) # read image
    index = 0
    
    labels = read_files(image_path + '/labels' + image[image.rindex('/'):-3] + 'txt') # read labels file

    for label in labels: # read line by line of label
        file_type = image[image.rindex('.'):]
        savepath = image_path + '/result' + image[image.rindex('/'):-4] + str(index) + file_type

        box = list(map(float, label.split(' ')[1:]))
        result = crop_image(img, box, 5)

        cv2.imwrite(savepath, result)
        index += 1
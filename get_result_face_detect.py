import cv2
import os

def solve_equation(x, y): # solve quation of 2
    return [round((x - y) / 2), round((x + y) / 2)]

def crop_image(img, box, savepath): # crop object image and save
    h, w, c = img.shape

    x1, x2 = solve_equation(2 * box[0] * w, box[2] * w)
    y1, y2 = solve_equation(2 * box[1] * h, box[3] * h)

    crop = img[y1:y2,x1:x2]
    cv2.imwrite(savepath, crop) # write image crop to data

def read_labels(filename): # read object detected
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content
    

def loop_all_files(directory, type):
    path = []
    for file in os.listdir(directory):
        if file.endswith(type):
            path.append(os.path.join(directory, file).replace('\\', '/'))
    return path


def main():
    image_path = 'exp6'
    images = loop_all_files(image_path, 'jpg') # get all images

    for image in images:
        img = cv2.imread(image) # read image
        index = 0
        
        labels = read_labels(image_path + '/labels' + image[image.rindex('/'):-3] + 'txt') # read labels file

        for label in labels: # read line by line of label
            savepath = image_path + '/result' + image[image.rindex('/'):-4] + str(index) + '.jpg'

            box = list(map(float, label.split(' ')[1:]))
            crop_image(img, box, savepath)

            index += 1
main()



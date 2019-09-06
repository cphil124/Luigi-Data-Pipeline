import luigi
from keras.preprocessing.image import ImageDataGenerator
import cv2

img_height, img_width = 100, 100

images_train_path = 'dataset\\Training\\'
images_test_path  = 'dataset\\Test\\'

imageGenTrain = ImageDataGenerator(rescale=1. / 255)
imageGenTest = ImageDataGenerator(rescale=1. / 255)

train_data = imageGenTrain.flow_from_directory(images_train_path, target_size=(img_height, img_width),
color_mode = 'rgb', batch_size=32)
test_data = imageGenTest.flow_from_directory(images_test_path, target_size=(img_height, img_width), color_mode='rgb', batch_size=32) 

path = images_test_path
correct = 0.0
for i in range(0, test_data.n):
    label = test_data.classes[i]
    img = cv2.imread(f'{path}/{test_data.filenames[i]}')
    im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(im, cv2.HOUGH_GRADIENT, dp=2, minDist=15, param1=100, param2=70)

    if circles is not None:
        if label == 1:
            correct += 1
        elif circles is None:
            if label == 0:
                correct += 1
print(f'Accuracy: {correct/test_data.n}')
    


import os
import glob
import numpy as np
import cv2

from sklearn .model_selection import train_test_split


def data_split(dir_path, split_range):
    folder_list = os.listdir(dir_path)

    for folder_name in folder_list:
        image_path_list = glob.glob(os.path.join(dir_path, folder_name, '*', '*'))

        if len(image_path_list) > 0:
            train_data, valid_data = train_test_split(image_path_list, test_size=0.1, shuffle=True, random_state=20230113)

            temp_dict = {
                'train': train_data,
                'valid': valid_data
            }
            
            for task, data in temp_dict.items():
                copy_data(task, data, split_range)
        else: 
            print('List is empty!', os.path.join(dir_path, folder_name))
            

def copy_data(task, data, split_range):
    for index, image_path in enumerate(data):
        gender = 'M' if image_path.split('\\')[-2] == '111' else 'F'

        age_label = image_path.split('\\')[-3]
        temp_num1 = int(age_label) // split_range
        temp_num2 = split_range // 10 - 1
        tenplace = int(split_range * temp_num1 / 10)
        label = '{tensplace1}0-{tenplace2}9_{gender}'.format(
            tensplace1=tenplace, tenplace2=(tenplace + temp_num2), gender=gender)
        
        dataset_dir_path = os.path.join('../', '{}_age_range_dataset'. format(split_range), task, label)
        os.makedirs(dataset_dir_path, exist_ok=True)
        
        image_dest_path = os.path.join(dataset_dir_path, '{}_{}.png'.format(label, index))
        image = make_square_image(image_path)

        if image is None:
            print(image_path)
            continue

        cv2.imwrite(image_dest_path, image)


def make_square_image(image_path):
    origin_image = cv2.imread(image_path)
    
    try:
        height, width, channels = origin_image.shape
    except:
        print(image_path, '#' * 10)
        return
    
    x = height if height > width else width
    y = height if height > width else width
    
    if 224 > x and 224 > y:
        x, y = 224, 224
    
    squre_image = np.zeros((x, y, channels), np.uint8)
    squre_image[int((y - height) / 2):int(y - (y - height) / 2), 
                int((x - width) / 2):int(x - (x - width) / 2)] = origin_image
    
    return squre_image

    
dir_path = os.path.join('./', 'AFAD-Full')
data_split(dir_path, 10)
print('first done!', '#' * 30)

data_split(dir_path, 20)
print('finish!', '#' * 30)
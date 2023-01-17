from torch.utils.data import Dataset
import json
import os
import glob
import cv2


# json값 확인
# with open("./metal_damaged_detection/anno/annotation.json", 'r') as f:

#     json_data = json.load(f)

# for i in json_data:
#     print(i) # img_01_3402617700_00001.jpg
#     print(json_data[i]) # {'filename': 'img_01_3402617700_00001.jpg', 'width': 2048, 'height': 1000, 'anno': [{'label': 'crescent_gap', 'bbox': [1738, 806, 1948, 993]}]}
#     print(json_data[i]["anno"]) # [{'label': 'crescent_gap', 'bbox': [1738, 806, 1948, 993]}]
#     print(json_data[i]["anno"][0]["bbox"]) # [1738, 806, 1948, 993]


def img_cut(img, x1, y1, x2, y2):
    cuted_img = img[y1: y2, x1: x2]
    return cuted_img

class json_custom(Dataset):

    # 주어진 json 파일로부터 데이터를 받음.
    def __init__(self, path, json_path, transform = None):
        with open(json_path, 'r') as f:
            self.json_data = json.load(f)
        
        # path = Dataset/images/
        self.all_image_path = glob.glob(os.path.join(path,"*.jpg"))

        self.transform = transform


    def __getitem__(self, index):
        img_path = self.all_image_path[index]
        img_name = os.path.basename(img_path)

        cur_json = self.json_data[img_name]["anno"][0]

        x1, y1, x2, y2, label = cur_json["bbox"][0], cur_json["bbox"][1], cur_json["bbox"][2], cur_json["bbox"][3], cur_json["label"]
        
        img = cv2.imread(img_path)
        # print(type(img)) # <class 'numpy.ndarray'>
        img = img_cut(img, x1, y1, x2, y2)

        if self.transform is not None:
            img = self.transform(img)

        return img, label

    # 길이 반환
    def __len__(self):
        return len(self.all_image_path)



if __name__ == "__main__":

    # (self, path, json_path, transform = None)
    test = json_custom("./metal_damaged_detection/images", "./metal_damaged_detection/anno/annotation.json" , transform=None)
    for image,label in test :
        cv2.imshow('img', image)
        print(label)
        cv2.waitKey(0)

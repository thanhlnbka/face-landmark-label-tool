from glob import glob
import os 
import cv2 


pth_labels = glob("output/*")

for pth_label in pth_labels:
    name_img = pth_label.split("/")[-1][:-4]
    pth_img = os.path.join("images", name_img+".jpg")
    image = cv2.imread(pth_img)
    with open(pth_label, "r") as fs:
        data = fs.readlines()
        data = [d.strip() for d in data]
        # print(data)
        for bbox in data:
            d = bbox.split(" ")
            cls = d[0]
            landmark = [int(i) for i in d[5:]]
            box = [int(i) for i in d[1:5]]
            # print(cls, landmark, box)
            cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (255,22,22), 1)
    cv2.imshow("hihi", image)
    cv2.waitKey(2000)
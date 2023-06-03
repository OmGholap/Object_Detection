import cv2
import os
from os import sys
# Opencv DNN
net = cv2.dnn.readNet("D:\Om data\Om code\Human DEtection project\dnn_model-220107-114215\dnn_model\yolov4-tiny.weights", "dnn_model-220107-114215\dnn_model\yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size =(320, 320),scale = 1/255) # 

#load class list 
classes = []
with open("dnn_model-220107-114215\dnn_model\classes.txt","r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)

# print(classes)
    

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True:
    #get frames

    ret, frame =cap.read()
    #obejject detection
    class_ids, score, bboxes = model.detect(frame)
    for class_id,score,bbox in zip(class_ids,score,bboxes):
        x,y,w,h = bbox
        class_name = classes[class_id]


        # print(x,y,w,h)
        cv2.putText(frame, str(class_name),(x,y-10),cv2.FONT_HERSHEY_PLAIN,2,(200,0,50), 2)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(200,0,50), 3)
    


    for name in class_name:
        if class_name != "person":
                None

                if class_name == "person":
                    print("get out")
                    print("flight not Engaged")
                    break
                
    


    # print("class ids",class_ids )
    # print("score",score )
    # print("bboxes",bboxes )


    cv2.imshow("Frame",frame)
    cv2.waitKey(1)
    


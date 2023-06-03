# Object_Detection
Object Detection using Open CV

This code is a Python script that uses OpenCV's DNN module to perform object detection in real-time using the YOLOv4-tiny model. The script initializes the DNN model by reading the pre-trained weights and configuration files. It also loads a list of class names from a text file.

The code then initializes the camera and sets its resolution. Inside a while loop, it continuously reads frames from the camera and performs object detection on each frame. Detected objects are annotated with bounding boxes and class labels using OpenCV's drawing functions.

The script also includes a condition to check if any detected object is a person. If a person is detected, it prints the message "get out" and "flight not Engaged" and breaks out of the loop. However, if no person is detected, the code does nothing.

The processed frames with annotations are displayed in a window using OpenCV's `imshow()` function. The loop continues until the user presses a key.

Note: The code assumes that the necessary model weights, configuration files, and class list file are present in specific directories. Modify the file paths accordingly to match your setup.

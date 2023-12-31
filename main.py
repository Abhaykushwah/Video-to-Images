# In this project my aim is to build a tool that can extract images(number of image will be equal to FPS*length of video in sec) from given video

# library opencv
    ## pip install opencv-python

import cv2

file = "ReCode.mkv"
capture = cv2.VideoCapture(file)

# exiting program in case of any error
if not capture.isOpened():
    print("Error opening video file")
    exit()

# Initialize a frame counter
frame_count = 0

# working on video while True
while True:
    # return true while capturing
    # return_cap = capture.read() ## at the end of the video the value of this variable will be false 
    return_cap, frame = capture.read() ## returning two values, and using tuple unpacking only single fram at a time

    if not return_cap:
        break
    # Save the frame as an image
    else:
        image_filename = f"frame_{frame_count:04d}.jpg"  ## saveing image && 04d is a format specifier which is d = decimal and 04 = 0001 - 9999
        # Extract the frame from the tuple before writing
        cv2.imwrite(image_filename, frame)  # SYNTAX : cv2.imwrite(filename, img)

        frame_count += 1

# Release the video capture object
capture.release()

import cv2
import numpy as np
import os
from glob import glob


video_paths = glob('*.mp4')
for video_path in video_paths:
    os.system(f'mkdir images\\{video_path[:-4]}')
    count = 0
    vidcap = cv2.VideoCapture(video_path)
    vidcap.set(3, 400)
    vidcap.set(4, 300)
    flag = 0
    stack = 0
    frame = 0
    ret, prev = vidcap.read()
    while(vidcap.isOpened()):
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        ret, image = vidcap.read()
        if not ret:
            stack += 1
            if stack > 20:
                break
            continue
        frame += 150
        stack = 0
        prev_gray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        diff = np.subtract(prev_gray, image_gray, dtype=np.int16)
        diff = np.abs(diff)
        diff = cv2.resize(diff, (400, 300))
        sum_diff = np.sum(diff>10)
        # print(sum_diff)
        if sum_diff > 10000:
            print('Saved frame number : ' + str(frame))
            cv2.imwrite("images/{}/{}_{}.jpg".format(video_path[:-4], count, sum_diff), prev)
            print('Saved frame%d.jpg' % count)
            count += 1
        prev = image
    cv2.imwrite("images/{}/{}_{}.jpg".format(video_path[:-4], count, sum_diff), prev)
    vidcap.release()
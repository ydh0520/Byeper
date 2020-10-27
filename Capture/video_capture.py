import cv2
import numpy as np
import os
from glob import glob
import datetime
# video_path = 'algo_1.mp4'
video_paths = glob('*.mp4')
print(video_paths)
now = datetime.datetime.now()
for video_path in video_paths:
    os.system(f'mkdir images\\{video_path[:-4]}')
    count = 0
    vidcap = cv2.VideoCapture(video_path)
    flag = 0
    stack = 0
    while(vidcap.isOpened()):
        ret, image = vidcap.read()
        # vidcap.grab(20)
        if not ret:
            if flag == vidcap.get(1):
                stack += 1
                if stack > 100:
                    break
            continue
        stack = 0
        flag = vidcap.get(1)
        if(int(vidcap.get(1)) == 1):
            prev = image
            height, width, channel = prev.shape
        elif(int(vidcap.get(1)) % 300 == 0):
            prev_gray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            diff = np.subtract(prev_gray, image_gray, dtype=np.int16)
            diff = np.abs(diff)
            diff = cv2.resize(diff, (400, 300))
            sum_diff = np.sum(diff>10)
            # print(sum_diff)
            if sum_diff > 10000:
                print('Saved frame number : ' + str(int(vidcap.get(1))))
                cv2.imwrite("images/{}/{}_{}.jpg".format(video_path[:-4], count, sum_diff), prev)
                print('Saved frame%d.jpg' % count)
                count += 1
            prev = image
    cv2.imwrite("images/{}/{}_{}.jpg".format(video_path[:-4], count, sum_diff), prev)
    vidcap.release()
    print(datetime.datetime.now()-now)
    break
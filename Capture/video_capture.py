import cv2
import numpy as np
import os
import pafy

url = 'https://www.youtube.com/watch?v=nlT-FuOaeJc'
video = pafy.new(url)

title = 'youtubetest'
print(title)
os.system('mkdir {}'.format(title))

print('title = ', title)

best = video.getbest()
cap = cv2.VideoCapture(best.url)

os.system(f'mkdir images\\{title}')

vidcap = cv2.VideoCapture(best.url)
count = 0
vidcap.set(3, 400)
vidcap.set(4, 225)
flag = 0
stack = 0
frame = 0
ret, prev = vidcap.read()
cv2.imwrite("images/{}/{}.jpg".format(title, count), prev)
while(vidcap.isOpened()):
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, frame)
    ret, image = vidcap.read()
    if not ret:
        stack += 1
        if stack > 5:
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
    if sum_diff > 7500:
        print('Saved frame number : ' + str(frame))
        cv2.imwrite("images/{}/{}_{}.jpg".format(title, count, sum_diff), image)
        count += 1
    prev = image
# cv2.imwrite("images/{}/{}_{}.jpg".format(title, count, sum_diff), prev)
vidcap.release()
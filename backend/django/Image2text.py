from google.cloud import vision
import os, cv2, io, re
check_kor = re.compile('[가-힣]+')
#check_eng = re.compile('[a-z|A-Z]+')

def image_processing(path):
    imgs = []
    
    is_json = os.path.join(path, path[-11:]+'.json')
    
    if not os.path.isdir(path) or not os.path.isfile(is_json):
        return -1


    for f in os.listdir(path):
        if f[-3:] == 'jpg':
            tmp = cv2.imread(os.path.join(path, f), 0)
            imgs.append(cv2.resize(tmp, (854, 480)))
    img = cv2.vconcat(imgs)
    target_dir = path[-11:]
    tmp_image = os.path.join(path, target_dir+'.jpg')

    cv2.imwrite(tmp_image, img)
    client = vision.ImageAnnotatorClient()

    with io.open(tmp_image, 'rb') as image_path:
        content = image_path.read()

    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    texts = response.text_annotations
    
    sentence = ''

    for text in texts[0].description.split('\n'):
        if not check_kor.search(text): continue
        sentence += text
        if sentence and sentence[-1] in ('은', '는', '이', '가', '을', '를'):
            sentence += ' '
        else:
            sentence += '\n'
            
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    os.remove(tmp_image)
    return sentence

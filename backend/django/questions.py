from Image2text import image_processing
from textblob import TextBlob
# result = image_processing('C:\\Users\\multicampus\\Desktop\\s03p31b108\\backend\\django\\tmp\\tQHw2EovIOM')
# with open('foo.txt', 'w', encoding='utf-8') as f:
#     f.write(result)

with open('foo.txt', 'r', encoding="utf-8") as f:
    result = f.read()


origin = TextBlob(result)
eng = origin.translate('ko', 'en')
# print(origin)
# print(eng)
# print('----------------')
# print(set(eng.noun_phrases))
arr = []
for texts in set(eng.noun_phrases):
    for text in texts.split():
        if len(text) < 3: break
    else:
        arr.append(texts)
        # print(texts)

for sen in eng.split('\n'):
    for answer in arr:
        if answer in sen:
            print(sen.replace(answer, '_______'), '||', answer)
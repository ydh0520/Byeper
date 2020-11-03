import pandas as pd

### Pickling
import _pickle as cPickle
from pathlib import Path

def dumpPickle(fileName, content):
    pickleFile = open(fileName, 'wb')
    cPickle.dump(content, pickleFile, -1)
    pickleFile.close()

def loadPickle(fileName):    
    file = open(fileName, 'rb')
    content = cPickle.load(file)
    file.close()    
    return content
    
def pickleExists(fileName):
    file = Path(fileName)
    
    if file.is_file():
        return True
    
    return False

import spacy
nlp = spacy.load('en_core_web_md')

def extractAnswers(qas, doc):
    answers = []
    senStart = 0
    senId = 0
    for sentence in doc.sents:
        senLen = len(sentence.text)
        for answer in qas:
            answerStart = answer['answers'][0]['answer_start']
            if (answerStart >= senStart and answerStart < (senStart + senLen)):
                answers.append({'sentenceId': senId, 'text': answer['answers'][0]['text']})
        senStart += senLen
        senId += 1
    return answers

#TODO - Clean answers from stopwords?
def tokenIsAnswer(token, sentenceId, answers):
    for i in range(len(answers)):
        if (answers[i]['sentenceId'] == sentenceId):
            if (answers[i]['text'] == token):
                return True
    return False

#Save named entities start points
def getNEStartIndexs(doc):
    neStarts = {}
    for ne in doc.ents:
        neStarts[ne.start] = ne
    return neStarts 

def getSentenceStartIndexes(doc):
    senStarts = []
    for sentence in doc.sents:
        senStarts.append(sentence[0].i)
    return senStarts
    
def getSentenceForWordPosition(wordPos, senStarts):
    for i in range(1, len(senStarts)):
        if (wordPos < senStarts[i]):
            return i - 1
        
def addWordsForParagrapgh(newWords, text):
    doc = nlp(text)
    neStarts = getNEStartIndexs(doc)
    senStarts = getSentenceStartIndexes(doc)
    i = 0
    while (i < len(doc)):
        if (i in neStarts):
            word = neStarts[i]
            currentSentence = getSentenceForWordPosition(word.start, senStarts)
            wordLen = word.end - word.start
            shape = ''
            for wordIndex in range(word.start, word.end):
                shape += (' ' + doc[wordIndex].shape_)

            newWords.append([word.text,
                            0,
                            0,
                            currentSentence,
                            wordLen,
                            word.label_,
                            None,
                            None,
                            None,
                            shape])
            i = neStarts[i].end - 1
        else:
            if (doc[i].is_stop == False and doc[i].is_alpha == True):
                word = doc[i]

                currentSentence = getSentenceForWordPosition(i, senStarts)
                wordLen = 1

                newWords.append([word.text,
                                0,
                                0,
                                currentSentence,
                                wordLen,
                                None,
                                word.pos_,
                                word.tag_,
                                word.dep_,
                                word.shape_])
        i += 1

def oneHotEncodeColumns(df):
    columnsToEncode = ['NER', 'POS', "TAG", 'DEP']
    for column in columnsToEncode:
        one_hot = pd.get_dummies(df[column])
        one_hot = one_hot.add_prefix(column + '_')
        df = df.drop(column, axis = 1)
        df = df.join(one_hot)
    return df

### Predict whether a word is a keyword
def generateDf(text):
    words = []
    addWordsForParagrapgh(words, text)
    wordColums = ['text', 'titleId', 'paragrapghId', 'sentenceId','wordCount', 'NER', 'POS', 'TAG', 'DEP','shape']
    df = pd.DataFrame(words, columns=wordColums)
    return df

def prepareDf(df):
    wordsDf = oneHotEncodeColumns(df)
    columnsToDrop = ['text', 'titleId', 'paragrapghId', 'sentenceId', 'shape']
    wordsDf = wordsDf.drop(columnsToDrop, axis = 1)
    predictorColumns = ['wordCount','NER_CARDINAL','NER_DATE','NER_EVENT','NER_FAC','NER_GPE','NER_LANGUAGE','NER_LAW','NER_LOC','NER_MONEY','NER_NORP','NER_ORDINAL','NER_ORG','NER_PERCENT','NER_PERSON','NER_PRODUCT','NER_QUANTITY','NER_TIME','NER_WORK_OF_ART','POS_ADJ','POS_ADP','POS_ADV','POS_CCONJ','POS_DET','POS_INTJ','POS_NOUN','POS_NUM','POS_PART','POS_PRON','POS_PROPN','POS_PUNCT','POS_SYM','POS_VERB','POS_X','TAG_''','TAG_-LRB-','TAG_.','TAG_ADD','TAG_AFX','TAG_CC','TAG_CD','TAG_DT','TAG_EX','TAG_FW','TAG_IN','TAG_JJ','TAG_JJR','TAG_JJS','TAG_LS','TAG_MD','TAG_NFP','TAG_NN','TAG_NNP','TAG_NNPS','TAG_NNS','TAG_PDT','TAG_POS','TAG_PRP','TAG_PRP$','TAG_RB','TAG_RBR','TAG_RBS','TAG_RP','TAG_SYM','TAG_TO','TAG_UH','TAG_VB','TAG_VBD','TAG_VBG','TAG_VBN','TAG_VBP','TAG_VBZ','TAG_WDT','TAG_WP','TAG_WRB','TAG_XX','DEP_ROOT','DEP_acl','DEP_acomp','DEP_advcl','DEP_advmod','DEP_agent','DEP_amod','DEP_appos','DEP_attr','DEP_aux','DEP_auxpass','DEP_case','DEP_cc','DEP_ccomp','DEP_compound','DEP_conj','DEP_csubj','DEP_csubjpass','DEP_dative','DEP_dep','DEP_det','DEP_dobj','DEP_expl','DEP_intj','DEP_mark','DEP_meta','DEP_neg','DEP_nmod','DEP_npadvmod','DEP_nsubj','DEP_nsubjpass','DEP_nummod','DEP_oprd','DEP_parataxis','DEP_pcomp','DEP_pobj','DEP_poss','DEP_preconj','DEP_predet','DEP_prep','DEP_prt','DEP_punct','DEP_quantmod','DEP_relcl','DEP_xcomp']
    for feature in predictorColumns:
        if feature not in wordsDf.columns:
            wordsDf[feature] = 0
    return wordsDf

def predictWords(wordsDf, df):
    predictorPickleName = '../../../data/nb-predictor.pkl'
    predictor = loadPickle(predictorPickleName)
    y_pred = predictor.predict_proba(wordsDf)
    labeledAnswers = []
    for i in range(len(y_pred)):
        labeledAnswers.append({'word': df.iloc[i]['text'], 'prob': y_pred[i][0]})
    return labeledAnswers

def blankAnswer(firstTokenIndex, lastTokenIndex, sentStart, sentEnd, doc):
    leftPartStart = doc[sentStart].idx
    leftPartEnd = doc[firstTokenIndex].idx
    rightPartStart = doc[lastTokenIndex].idx + len(doc[lastTokenIndex])
    rightPartEnd = doc[sentEnd - 1].idx + len(doc[sentEnd - 1])
    question = doc.text[leftPartStart:leftPartEnd] + '_____' + doc.text[rightPartStart:rightPartEnd-1]
    return question

def addQuestions(answers, text):
    doc = nlp(text)
    currAnswerIndex = 0
    qaPair = []
    for sent in doc.sents:
        for token in sent:
            if currAnswerIndex >= len(answers): break
            answerDoc = nlp(answers[currAnswerIndex]['word'])
            answerIsFound = True
            for j in range(len(answerDoc)):
                if token.i + j >= len(doc) or doc[token.i + j].text != answerDoc[j].text:
                    answerIsFound = False
            if answerIsFound:    
                sentence = str(sent).strip()
                question = blankAnswer(token.i, token.i + len(answerDoc) - 1, sent.start, sent.end, doc)
                qaPair.append({'question' : question, 'answer': answers[currAnswerIndex]['word'], 'prob': answers[currAnswerIndex]['prob'], 'origin': sentence})
                currAnswerIndex += 1
    return qaPair

def sortAnswers(qaPairs):
    orderedQaPairs = sorted(qaPairs, key=lambda qaPair: qaPair['prob'])
    return orderedQaPairs

model = loadPickle('../../../data/word2vec_model')

def generate_distractors(answer, count):
    answer = str.lower(answer)
    try:
        closestWords = model.most_similar(positive=[answer], topn=count)
    except:
        return []
    distractors = list(map(lambda x: x[0], closestWords))[0:count]
    return distractors

def addDistractors(qaPairs, count):
    for qaPair in qaPairs:
        distractors = generate_distractors(qaPair['answer'], count)
        qaPair['distractors'] = distractors
    return qaPairs

### Main function
def generateQuestions(text, count):

    df = generateDf(text)
    wordsDf = prepareDf(df)

    labeledAnswers = predictWords(wordsDf, df)

    qaPairs = addQuestions(labeledAnswers, text)

    orderedQaPairs = sortAnswers(qaPairs)

    questions = addDistractors(orderedQaPairs[:10], 4)
    
    # for q in questions:
    #     print(q['question'])
    #     print(q['answer'])
    #     print(q['distractors'])
    #     print(q['origin'])
    #     print()
    print(orderedQaPairs)


# text = "Oxygen is a chemical element with symbol O and atomic number 8. It is a member of the chalcogen group on the periodic table, a highly reactive nonmetal, and an oxidizing agent that readily forms oxides with most elements as well as with other compounds. By mass, oxygen is the third-most abundant element in the universe, after hydrogen and helium. At standard temperature and pressure, two atoms of the element bind to form dioxygen, a colorless and odorless diatomic gas with the formula O2. Diatomic oxygen gas constitutes 20.8% of the Earth's atmosphere. As compounds including oxides, the element makes up almost half of the Earth's crust."
# text = """nice to meet you. i'm jaeho, 27 years old this year."""

def main(text):
    # text = """Dijkstra Algorithm: Improved Implementation Method Performance Analysis * The time complexity of Dijkstra&#39;s algorithm using heap data structure is 0(&amp;8709『). * Loop statements (\|6 statements) that take out and check nodes one by one are not processed as a number of times greater than the number of nodes V. * As a result, the total number of times to check the node pulled out of the current priority queue and other nodes connected to it can be calculated as much as the maximum number of trunk lines (6). * Intuitively, the whole process is very similar to the operation of putting c elements into the priority queue and then removing them all. * Time complexity can be judged as 0(ElogE)2. * If you do not include redundant edges, you can organize them as 0(8(00『). + 0(ElogE) -» 0(ElogV?) ㅜㅠ 0(2ElogV) — 0O(ElogV) """
    generateQuestions(text, 10)

print(main('hi'))
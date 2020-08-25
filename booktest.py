def read_data(filename):
    with open(filename, 'r',  encoding='utf-8' ) as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        # txt 파일의 헤더(id document label)는 제외하기
        data = data[1:]
    return data

train_data = read_data('book_train.txt')


print(len(train_data))
print(len(train_data[0]))

from konlpy.tag import Okt

okt = Okt()

import json
import os
from pprint import pprint

def tokenize(doc):
    # norm은 정규화, stem은 근어로 표시하기를 나타냄
    return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

if os.path.isfile('train_docs.json'):
    with open('train_docs.json', encoding='UTF8') as f:
        train_docs = json.load(f)
else:
    train_docs = [(tokenize(row[2]), row[0]) for row in train_data]
    with open('train_docs.json', 'w', encoding="utf-8") as make_file:
        json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")

pprint(train_docs[0])

tokens = [t for d in train_docs for t in d[0]]
print(len(tokens))

import nltk
text = nltk.Text(tokens, name='NMSC')
print("중복제외 토큰 개수: ")
print( len(set(text.tokens)))
pprint("최다 빈도 top ten")
print(text.vocab().most_common(10))

selected_words = [f[0] for f in text.vocab().most_common(1000)]

def term_frequency(doc):
    return [doc.count(word) for word in selected_words]
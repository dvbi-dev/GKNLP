from gensim.models import Word2Vec
import warnings
import re
from nltk import  sent_tokenize
from nltk.corpus import words
vocab = {}
path=r"D:\pythonProject2\text3.txt"
ar=[]
count = 0
with open(path, mode='r', encoding="utf-8") as f:
    while True:
        data = f.read()
        if data == '':
            break
        print(data)
        document = sent_tokenize(data)
        processed_docs = [doc.lower().replace(".", "") for doc in document]
        for doc in processed_docs:
            for word in doc.split():
                if word not in vocab:
                    count = count + 1
                    vocab[word] = count
    print(document)
for v in vocab.keys():
    ar.append(v)
print(ar)




warnings.filterwarnings('ignore')
corpus=[ar ,ar ]
model_cbow = Word2Vec(corpus, min_count=1, sg=0)
words = list(model_cbow.wv.vocab)
print(words)
print(model_cbow["they"])
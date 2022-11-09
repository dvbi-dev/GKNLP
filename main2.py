
from nltk import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import re
count_vect = CountVectorizer()

path=r"D:\pythonProject2\text2.txt"
with open(path, mode='r', encoding="utf-8") as f:
    while True:
        data = f.read()
        if data == '':
            break
        print(data)
        document = sent_tokenize(data)
        processed_docs = [doc.lower().replace(".", "") for doc in document]
        bow_rep = count_vect.fit_transform(processed_docs)
        print(str(count_vect.vocabulary_))
        print(str(bow_rep[0].toarray()))
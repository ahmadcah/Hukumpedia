from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
### YOUR CODE HERE
from tensorflow.keras import regularizers
###
import tensorflow.keras.utils as ku
import re
import numpy as np

with open('MergedData.txt', 'rb') as f:
    data = ''.join([x.decode('utf8') for x in f.readlines()])
    print(data)
    corpus = data.lower().split("\r\n")
    corpus = [re.sub('\d', '', y) for y in corpus]
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(corpus)
    total_words = len(tokenizer.word_index) + 1
    print(total_words)
    var = tokenizer.word_index
    print(var)
"""
target = input("keyword: ")
with open("temp.txt", encoding='utf8') as openfile:
    for line in openfile:
        for part in line.split():
            if target in part:
                print(line)
                """

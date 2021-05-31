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
    data = ''.join([x.decode('utf8')for x in f.readlines()])
    corpus = data.lower().split('\n')
    print(corpus)

"""
target = input("keyword: ")
with open("temp.txt", encoding='utf8') as openfile:
    for line in openfile:
        for part in line.split():
            if target in part:
                print(line)
                """

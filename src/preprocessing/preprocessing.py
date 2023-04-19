
"""

"""
from keras_preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical


class Preprocessing ():
    def __init__(self):
        self.x= None
        self.y= None
        self.words_id = None
        self.label_id = None
        self.label_id = None
        self.words_id = None
        
    def tokenization (self, word_df, sent_df):
        uniq_words= word_df.select(['word']).unique()        
        uniq_label = word_df.select(['label']).unique()

        self.words_id = {w:i+2 for i,w in enumerate(list(uniq_words['word']))}
        self.words_id["PAD"] = 0
        self.words_id["UNK"] = 1 

        self.label_id = {t:i+1 for i,t in enumerate(list(uniq_label['label']))}
        self.label_id["PAD"] = 0

        x = [[self.words_id[w] for w in list(s)] for s in list(sent_df['text'])]
        y = [[self.label_id[w] for w in list(s)] for s in list(sent_df['label'])]
        
        return x, y 
    
    def padding (self, maxlen):
        maxlen = 160
        self.x = pad_sequences(maxlen=maxlen, sequences=self.x, padding='post', 
                          value=self.words_id['PAD'])
        self.y = pad_sequences(maxlen=maxlen, sequences=self.y, padding='post', 
                          value=self.label_id["PAD"])

    def train_test_data (self):
        self.y = [to_categorical(i, num_classes = len(self.label_id)) for i in self.y] 


        return train_test_split(self.x, self.y, test_size=0.2)

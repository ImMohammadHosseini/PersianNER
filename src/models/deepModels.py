
"""

"""

import keras
from keras import layers
from keras_contrib.layers import CRF


def BiLSTM_Softmax (max_len, words_num):
    model = keras.Sequential([
        layers.Input(shape=(max_len,)),
        layers.Embedding(words_num, 300, trainable=True, input_length=max_len),
        layers.Bidirectional(layers.LSTM(30, return_sequences=True, dropout=0.5,
                                         recurrent_dropout=0.5)),
        layers.TimeDistributed(layers.Dense(30, activation="softmax")),
        layers.Dense(14, activation="softmax")
        ]
    )
    model.compile(loss='categorical_crossentropy',
                  optimizer=keras.optimizers.Adam(lr=0.001), 
                  metrics=['accuracy'])
    return model


def BiLSTM_CNNs_CRF (max_len, words_num):
    crf = CRF(14)
    model = keras.Sequential([
        layers.Input(shape = (max_len,)),
        layers.Embedding(words_num, 300, trainable=True, input_length=max_len),
        layers.Bidirectional(layers.LSTM(60, dropout=0.5, recurrent_dropout=0.5, 
                                  return_sequences = True)),
        layers.Conv1D(50, 2, activation='softmax', padding='same'),
        layers.TimeDistributed(layers.Dropout(0.25)),
        layers.Conv1D(30, 3, activation='sigmoid', padding='same'),
        layers.TimeDistributed(layers.Dropout(0.25)),
        layers.TimeDistributed(layers.Flatten()),
        layers.TimeDistributed(layers.Dense(20, activation='softmax')),
        CRF(14)
        ]
    )
    
    model.compile(optimizer=keras.optimizers.Adam(lr=0.001),
                  loss=crf.loss_function, metrics=[crf.accuracy])
    return model
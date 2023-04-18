
"""

"""

import tensorflow as tf
from keras.layers import GRU

class Bi_directional_lSTM_softmax(tf.keras.Model):

	def __init__(self):
    super().__init__()
	inp = Input(shape=(maxlen,))
	x = Embedding(len(words_id),300, trainable=True, input_length=maxlen)(inp)
x = Bidirectional(LSTM(60, return_sequences=True,dropout=0.5,recurrent_dropout=0.5))(x)
x = TimeDistributed(Dense(30, activation="softmax"))(x)

    self.dense1 = tf.keras.layers.Dense(4, activation=tf.nn.relu)
    self.dense2 = tf.keras.layers.Dense(5, activation=tf.nn.softmax)

  def call(self, inputs):
    x = self.dense1(inputs)
    return self.dense2(x)



"""

"""
import optparse
import tensorflow as tf
import numpy as np 

from src.read_data.load_arman_dataset import read_data
from src.preprocessing.preprocessing import Preprocessing
from src.models.deepModels import BiLSTM_CNNs_CRF, BiLSTM_Softmax, BiLSTM_CRF
from src.visualization.model_visulize import visulize


usage = "usage: python main.py -d <dataset> -m <models>"

parser = optparse.OptionParser(usage=usage)
parser.add_option("-d", "--dataset", action="store", dest="dataset", default="ArmanNER", 
				  help="In first version, just use ArmanNER(default)")
parser.add_option("-m", "--models", action="store", dest="models", 
                  default=["BiLSTM_Softmax",
                           "BiLSTM_CRF",
                           "BiLSTM_CNNs_CRF"])
opts, args = parser.parse_args()

cpu = tf.config.experimental.list_physical_devices('CPU')[0]
gpu = tf.config.experimental.list_physical_devices('GPU')
if len(gpu)>0:
    gpu = gpu[0]
    tf.config.experimental.set_memory_growth(gpu, True)
    #tf.config.experimental.set_visible_devices(cpu)
    print("GPU known")
else :
    print("GPU unknown")

if opts.dataset == 'ArmanNER':
    DATA_PATH = 'data/ArmanPersoNERCorpus.txt'

MAX_LEN = 160
BATCH_SIZE = 64
EPOCHS = 5

if __name__ == "__main__":        
    word_df, sent_df = read_data(DATA_PATH) 
    preprocessing = Preprocessing()
    preprocessing.tokenization(word_df, sent_df)
    preprocessing.padding(MAX_LEN)
    x_train, x_test, y_train, y_test = preprocessing.train_test_data()
    
    for model_name in opts.models:
        print(model_name+" model")
        model = eval(model_name+"(MAX_LEN, preprocessing.get_words_num())")

        model.summary()
        hist = model.fit(x_train, np.array(y_train), batch_size=BATCH_SIZE, 
                         epochs=EPOCHS, validation_split=0.2)
        visulize(hist)

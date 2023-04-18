
"""

"""
import optparse
import tensorflow as tf

from src.read_data.load_arman_dataset import read_data


usage = "usage: python main.py -d <dataset> -m <models>"

parser = optparse.OptionParser(usage=usage)
parser.add_option("-d", "--dataset", action="store", dest="dataset", default="ArmanNER", 
				  help="In first version, just use ArmanNER(default)")
parser.add_option("-m", "--models", action="store", dest="models", 
                  default="[]")
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


if __name__ == "__main__":        
    

"""
"""
import matplotlib.pyplot as plt


def visulize (hist):
    plt.plot(hist.history["accuracy"])
    plt.plot(hist.history["val_accuracy"])
    plt.title("Accuracy")
    plt.xlabel("Epochs")
    plt.ylabel("BiLSTM")
    plt.legend(['train', 'test'], loc = 'lower right')
    plt.show()

    plt.plot(hist.history['loss'])
    plt.plot(hist.history['val_loss'])
    plt.title("Loss")
    plt.xlabel('Epochs')
    plt.ylabel('BiLSTM')
    plt.legend(['train', 'test'], loc='upper right')
    plt.show()
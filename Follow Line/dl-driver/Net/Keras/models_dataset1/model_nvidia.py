# Based on: https://arxiv.org/pdf/1604.07316.pdf

from keras.models import Sequential
from keras.layers import Flatten, Dense, Conv2D, BatchNormalization
from keras.optimizers import Adam
import keras.backend as K


# def myAccuracy_regression(y_true, y_pred):
#     # Absolute difference between correct and predicted values
#     diff = K.abs(y_true-y_pred)
#     # Tensor with 0 for false values and 1 for true values
#     correct = K.less(diff,0.05)
#     # Sum all 1's and divide by the total
#     return K.mean(correct)


def pilotnet_model(img_shape):
    '''
    Model of End to End Learning for Self-Driving Cars (NVIDIA)
    '''
    model = Sequential()
    model.add(BatchNormalization(epsilon=0.001, axis=-1, input_shape=img_shape))
    model.add(Conv2D(24, (5, 5), strides=(2, 2), activation="relu"))
    model.add(Conv2D(36, (5, 5), strides=(2, 2), activation="relu"))
    model.add(Conv2D(48, (5, 5), strides=(2, 2), activation="relu"))
    model.add(Conv2D(64, (3, 3), strides=(1, 1), activation="relu"))
    model.add(Conv2D(64, (3, 3), strides=(1, 1), activation="relu"))
    model.add(Flatten())
    model.add(Dense(1164, activation="relu"))
    model.add(Dense(100, activation="relu"))
    model.add(Dense(50, activation="relu"))
    model.add(Dense(10, activation="relu"))
    model.add(Dense(1))
    adam = Adam(lr=0.0001)
    model.compile(optimizer=adam, loss="mse", metrics=['accuracy', 'mse', 'mae'])
    return model

import numpy as np
import codecs
from io import BytesIO
import matplotlib.pylab as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras import optimizers

def predict():
    x_train=np.genfromtxt('wx_train',delimiter=';',dtype = int)
    y_train=np.genfromtxt('wy_train',delimiter=';', dtype=int)
    x_test=np.genfromtxt('wx_test',delimiter=';', dtype=float)
    y_test=np.genfromtxt('wy_test',delimiter=';', dtype=float)

    model = Sequential()
    model.add(Dense(512, activation='relu', input_shape=(x_train.shape[1],), kernel_initializer="normal"))
    model.add(Dense(6))
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])

    model.fit(x_train, y_train, epochs=100, batch_size=1, verbose=1)
    pred = model.predict(x_test)
    mse, mae = model.evaluate(x_test, y_test, verbose=0)
    print("Средняя абсолютная ошибка :", mae)
    print(pred)
    return pred

predict()
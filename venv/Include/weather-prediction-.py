import numpy as np
import codecs
from io import BytesIO
import matplotlib.pylab as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras import optimizers

x_train=np.genfromtxt("C:/Users/Elina/Documents/Keras/dataset/wx_train.txt",delimiter=';',dtype = int)
y_train=np.genfromtxt("C:/Users/Elina/Documents/Keras/dataset/wy_train.txt",delimiter=';', dtype=int)
x_test=np.genfromtxt("C:/Users/Elina/Documents/Keras/dataset/wx_test.txt",delimiter=';', dtype=float)
y_test=np.genfromtxt("C:/Users/Elina/Documents/Keras/dataset/wy_test.txt",delimiter=';', dtype=float)

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(x_train.shape[1],), kernel_initializer="normal"))
model.add(Dense(6))
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

model.fit(x_train, y_train, epochs=100, batch_size=1, verbose=1)
pred = model.predict(x_test)
mse, mae = model.evaluate(x_test, y_test, verbose=0)
print("Средняя абсолютная ошибка :", mae)
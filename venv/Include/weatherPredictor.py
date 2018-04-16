import numpy as np
import codecs
import h5py
from keras.models import model_from_json
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

    # model = Sequential()
    # model.add(Dense(512, activation='relu', input_shape=(x_train.shape[1],), kernel_initializer="normal"))
    # model.add(Dense(6))
    # model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    #
    # model.fit(x_train, y_train, epochs=100, batch_size=1, verbose=1)
    # model_json = model.to_json()
    # # Записываем модель в файл
    # json_file = open("mnist_model.json", "w")
    # json_file.write(model_json)
    # json_file.close()
    # model.save_weights("mnist_model.h5")


    json_file = open("mnist_model.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("mnist_model.h5")
    loaded_model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])
    scores = loaded_model.evaluate(x_test, y_test, verbose=0)
    pred = loaded_model.predict(x_test)
    print(pred)
    return pred

predict()
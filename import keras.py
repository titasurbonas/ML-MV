import keras
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()

model.add(Dense(input_dim = 2, units = 10, activation='relu', kernel_initializer='uniform'))

model.add(Dense(units = 20, activation='relu', kernel_initializer='uniform'))

model.add(Dense(units = 1, activation='sigmoid', kernel_initializer='uniform'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train,Y_train,batch_size=500, epochs=10)
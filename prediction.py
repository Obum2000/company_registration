

# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/prediction')
# def prediction():

        #!/usr/bin/env python
    # coding: utf-8

    # In[109]:
    # univariate cnn code
from numpy import array
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
import pickle
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from numpy import loadtxt
from tensorflow.keras.models import load_model
    
    # In[110]:
model = tf.keras.models.load_model('trained_RF_model_lstm1.h5')

    # In[111]:
    # demonstrate prediction
n_steps = (7)
n_features = 1
x_input = array([9760, 8567, 6750, 7950, 9450, 10200, 9870])
y_input = array([1, 2, 3, 4, 5, 6, 7])
x_input1 = x_input.reshape((1, n_steps, n_features))
    
#x_input1 = total_revenue.reshape((1, n_steps, n_features))
yhat = model.predict(x_input1, verbose=0)
print(yhat)


# In[112]:

#x_input2 = x_input.tolist()
#y_input2 = y_input.tolist()

# In[129]:


#x_input2 = x_input.tolist()
#y_input2 = y_input.tolist()
x_input3 = np.append(x_input1, yhat)
y_input3 = np.append(y_input, 8)

plt.plot(y_input3, x_input3, color = 'blue', label = 'Next-Day Forecast')
plt.plot(y_input, x_input, color = 'red', label = '1 Week Revenue')
plt.title('Revenue Per day')
plt.xlabel('Day')
plt.ylabel('Revenue')
plt.legend()
plt.show()


# In[ ]:







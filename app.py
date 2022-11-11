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

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
# @app.route("/home")

# def home():
#     return render_template('main.html')

@app.route("/prediction")

def result():
    # output = request.form.to_dict()
    # name = output['name']

    storeA = [];
    storeB = [];
    storeC = [];

    # storeA.push(float(request.args.get("week1a")))
    # storeA.push(float(request.args.get("week2a")))
    # storeA.push(float(request.args.get("week3a")))
    # storeA.push(float(request.args.get("week4a")))

    # storeB.push(float(request.args.get("week1a")))
    # storeB.push(float(request.args.get("week2a")))
    # storeB.push(float(request.args.get("week3a")))
    # storeB.push(float(request.args.get("week4a")))

    # storeC.push(float(request.args.get("week1a")))
    # storeC.push(float(request.args.get("week2a")))
    # storeC.push(float(request.args.get("week3a")))
    # storeC.push(float(request.args.get("week4a")))

    storeA.push(document.getElementById("week1a").value);
    storeA.push(document.getElementById("week2a").value);
    storeA.push(document.getElementById("week3a").value);
    storeA.push(document.getElementById("week4a").value);

    storeB.push(document.getElementById("week1b").value);
    storeB.push(document.getElementById("week2b").value);
    storeB.push(document.getElementById("week3b").value);
    storeB.push(document.getElementById("week4b").value);

    storeC.push(document.getElementById("week1c").value);
    storeC.push(document.getElementById("week2c").value);
    storeC.push(document.getElementById("week3c").value);
    storeC.push(document.getElementById("week4c").value);
    
    
    total_revenue = storeA + storeB + storeC

    model = tf.keras.models.load_model('trained_RF_model_lstm1.h5')

    # In[111]:
    # demonstrate prediction
    # x_input = array([7890, 7670, 6650, 7880, 8950, 11200, 9870])
    # x_input1 = x_input.reshape((1, n_steps, n_features))
    
    y_input = array([1, 2, 3, 4, 5, 6, 7])
    n_steps = (7)
    n_features = 1
    x_input1 = total_revenue.reshape((1, n_steps, n_features))
    yhat = model.predict(x_input1, verbose=0)
    print(yhat)

    # In[129]:


    #x_input2 = x_input.tolist()
    #y_input2 = y_input.tolist()
    x_input3 = np.append(x_input1, yhat)
    y_input3 = np.append(y_input, 8)

    plt.plot(y_input3, x_input3, color = 'blue', label = 'Next-Day Forecast')
    plt.plot(y_input, x_input1, color = 'red', label = '1 Week Revenue')
    plt.title('Revenue Per day')
    plt.xlabel('Day')
    plt.ylabel('Revenue')
    plt.legend()
    plt.show()
    plt.savefig("prediction_graph.png")


    print(total_revenue)

    
    return render_template('main.html', "prediction_graph.png")

if __name__ == '__main__':
    app.run(debug=True,port=5001)



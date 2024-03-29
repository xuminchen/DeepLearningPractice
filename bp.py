# import tensorflow as tf
import numpy as np

w = [0.1, 0.15, 0.2, 0.225, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65]
b = [0.35, 0.65]
I = [5, 10]


# activate function
def sigmoid(z):
    return 1.0 / (1 + np.e**(-z))


# hidden layer
def f1(w, b, I):
    # calculate FP
    h1 = sigmoid(w[0] * I[0] + w[1] * I[1] + b[0])
    h2 = sigmoid(w[2] * I[0] + w[3] * I[1] + b[0])
    h3 = sigmoid(w[4] * I[0] + w[5] * I[1] + b[0])
    o1 = sigmoid(w[6] * h1 + w[8] * h2 + w[10] * h3 + b[1])
    o2 = sigmoid(w[7] * h1 + w[9] * h2 + w[11] * h3 + b[1])

    # bp derivative of output
    t1 = -(0.01 - o1) * o1 * (1 - o1)
    t2 = -(0.99 - o2) * o2 * (1 - o2)

    # update w
    w[6] = w[6] - 0.5 * (t1 * h1)
    w[8] = w[8] - 0.5 * (t1 * h2)
    w[10] = w[10] - 0.5 * (t1 * h3)
    w[7] = w[7] - 0.5 * (t2 * h1)
    w[9] = w[9] - 0.5 * (t2 * h2)
    w[11] = w[11] - 0.5 * (t2 * h3)

    w[0] = w[0] - 0.5 * (t1 * w[6] + t2 * w[7]) * h1 * (1 - h1) * I[0]
    w[1] = w[1] - 0.5 * (t1 * w[6] + t2 * w[7]) * h1 * (1 - h1) * I[1]
    w[2] = w[2] - 0.5 * (t1 * w[8] + t2 * w[9]) * h2 * (1 - h2) * I[0]
    w[3] = w[3] - 0.5 * (t1 * w[8] + t2 * w[9]) * h2 * (1 - h2) * I[1]
    w[4] = w[4] - 0.5 * (t1 * w[10] + t2 * w[11]) * h3 * (1 - h3) * I[0]
    w[5] = w[5] - 0.5 * (t1 * w[10] + t2 * w[11]) * h3 * (1 - h3) * I[1]
    print(w)
    return w


for i in range(1000):
    print("No.%d" % i)
    f1(w, b, I)
    print("*"*20)

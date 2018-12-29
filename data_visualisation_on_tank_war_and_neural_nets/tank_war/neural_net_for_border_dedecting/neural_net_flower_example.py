from matplotlib import pyplot as plt
import numpy as np
import json


"""
data = [[3,   1.5, 1],
        [2,   1,   0],
        [4,   1.5, 1],
        [3,   1,   0],
        [3.5, .5,  1],
        [2,   .5,  0],
        [5.5,  1,  1],
        [1,    1,  0]]

"""

with open('training_data.json', 'r') as file_object:
    train_data = json.load(file_object)

data = train_data

print(data)

for i in range(len(data)):
    data[i][0] = data[i][0]/100
    data[i][1] = data[i][1]/100





#    mysteri_flower = [4.5, 1]

w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()

def sigmoid(x):
    return 1/(1 + np.exp(-x))


# Derivative of sigmoid fucntion
def sigmoid_p(x):
    return sigmoid(x) * (1 - sigmoid(x))


# Training loop

learning_rate = 0.2
costs = []

for i in range(50000):
    ri = np.random.randint(len(data))
    point = data[ri]

    z = point[0] * w1 + point[1] * w2 + b
    pred = sigmoid(z)

    target = point[2]
    cost = np.square(pred - target)

    dcost_pred = 2 * (pred - target)
    dpred_dz = sigmoid_p(z)

    dz_dw1 = point[0]
    dz_dw2 = point[1]
    dz_db = 1

    dcost_dz = dcost_pred * dpred_dz

    # can t understand very well
    dcost_dw1 = dcost_dz * dz_dw1
    dcost_dw2 = dcost_dz * dz_dw2
    dcost_db = dcost_dz * dz_db

    w1 = w1 - learning_rate * dcost_dw1
    w2 = w2 - learning_rate * dcost_dw2
    b = b - learning_rate * dcost_db


    if i % 100 == 0:
        cost_sum = 0
        for i in range(len(data)):
            point = data[i]
            print(point)
            z = point[0] * w1 + point[1] * w2 + b
            pred = sigmoid(z)

            print("pred: {}".format(pred))

            target = point[2]
            cost_sum += np.square(pred - target)

        costs.append(cost_sum/len(data))




unknown_place = [2.3, 3.97]

# for checking 
z = unknown_place[0] * w1 + unknown_place[1] * w2 + b

print("_________________________")
pred = sigmoid(z)
print("pred: {}".format(pred))




plt.plot(costs)
plt.show()


"""
# Scattering data
plt.axis([0, 6, 0, 6])
plt.grid()
for i in range(len(data)):
    point = data[i]
    color = "r"
    if point[2] == 0:
        color = "b"
    plt.scatter(point[0], point[1], c=color)

plt.show()
"""



"""
# Scattering sigmoid and sigmd_p
T = np.linspace(-5, 5, 100)
plt.plot(T, sigmoid(T), c='r')
plt.plot(T, sigmoid_p(T), c='b')
plt.show()
"""

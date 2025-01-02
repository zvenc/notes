import numpy as np
import matplotlib.pyplot as plt

# feature array
x_train = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])

# target array
y_train = np.array([300.0, 500.0, 580.0, 830.0, 900.0, 1100.0 ])

w = 170 # weight
b = 100 # bias

def compute_model_output(x, w, b):
    """
    Computes the prediction of a linear model
    args:
        x (ndarray (m,))    : data, size m
        w, b (scalar)       : model parameters
    returns:
        f_wb (ndarray (m,)) : model prediction
    """
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
    return f_wb

# i = 0
# x_i, y_i = x_train[i], y_train[i]
# print(f"(x^i, y^i) = ({x_i}, {y_i})")

x_i = 1.2
cost_1200sqft = w * x_i + b
print(f"cost of a 1200 sq. ft. house is predicted to be ${cost_1200sqft:.0f}K")

f_wb = compute_model_output(x_train, w, b)
plt.scatter(x_train, y_train, marker='.', c='black')
plt.plot(x_train, f_wb, c='black', label='model prediction')
plt.xlabel("size of house in 1000s sq. ft.")
plt.ylabel("price of house in $1000s")
plt.show()

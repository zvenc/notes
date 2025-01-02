import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([1, 2, 3, 4, 5, 6])
y_train = np.array([300, 500, 580, 830, 900, 1100])


def cost_function(x, y, W, B):
    y_hat = W[:, :, np.newaxis] * x + B[:, :, np.newaxis]
    squared_error = (y_hat - y)**2
    return np.mean(squared_error, axis=2) / 2


# create a grid of w and b values
w_values = np.linspace(160, 180, 100)
b_values = np.linspace(80, 120, 100)
W, B = np.meshgrid(w_values, b_values)
J = np.zeros_like(W)

# compute the cost function for each (w, b) pair
J = cost_function(x_train, y_train, W, B)
# print(f"J: {J}")

# plot the paraboloid
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(W, B, J, cmap='viridis', alpha=0.8)

# Add labels
ax.set_xlabel('W (Weight)')
ax.set_ylabel('B (Bias)')
ax.set_zlabel('J(W, B) (Cost)')
ax.set_title('Paraboloid of the Cost Function')
plt.show()

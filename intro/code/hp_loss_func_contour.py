import numpy as np
import matplotlib.pyplot as plt

# Training data
x_train = np.array([1, 2, 3, 4, 5, 6])
y_train = np.array([300, 500, 580, 830, 900, 1100])

# Cost function
def cost_function(x, y, W, B):
    y_hat = W[:, :, np.newaxis] * x + B[:, :, np.newaxis]
    squared_error = (y_hat - y)**2
    return np.mean(squared_error, axis=2) / 2

# Create a grid of w and b values
w_values = np.linspace(80, 180, 100)  # Adjusted range to include both points
b_values = np.linspace(80, 400, 100)  # Adjusted range to include both points
W, B = np.meshgrid(w_values, b_values)

# Compute the cost function for each (w, b) pair
J = cost_function(x_train, y_train, W, B)

# Hardcoded values for the marked points
w1, b1 = 170, 100  # First point
w2, b2 = 155.57, 157.54  # Second point
w_range = [80, 180]  # Adjusted range for w axis
b_range = [80, 400]  # Adjusted range for b axis

# Create the plot
fig, ax = plt.subplots(1, 1, figsize=(8, 6))

# Contour plot (using default colors)
CS = ax.contour(W, B, np.log(J), levels=12, linewidths=2, alpha=0.7)
ax.set_title('Cost(w,b)')
ax.set_xlabel('w', fontsize=10)
ax.set_ylabel('b', fontsize=10)
ax.set_xlim(w_range)
ax.set_ylim(b_range)

# Scatter plot for the marked points
cscat1 = ax.scatter(w1, b1, s=100, zorder=10, label="Point 1 (w=170, b=100)")
cscat2 = ax.scatter(w2, b2, s=100, zorder=10, label="Point 2 (w=155.57, b=157.54)")

# Horizontal and vertical lines for the first point
ax.hlines(b1, ax.get_xlim()[0], w1, lw=4, ls='dotted')
ax.vlines(w1, ax.get_ylim()[0], b1, lw=4, ls='dotted')

# Horizontal and vertical lines for the second point
ax.hlines(b2, ax.get_xlim()[0], w2, lw=4, ls='dotted')
ax.vlines(w2, ax.get_ylim()[0], b2, lw=4, ls='dotted')

# Add legend
ax.legend()

# Show the plot
plt.show()


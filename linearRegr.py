import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")

X = data["hours_studied"].values
Y = data["grade"].values

Xmean = np.mean(X)
Ymean = np.mean(Y)

numerator = np.sum((X - Xmean)*(Y - Ymean))
denominator = np.sum(((X - Xmean)*(X - Xmean)))

m = numerator/denominator

b = Ymean - (m * Xmean)

Ypred = m*X + b
# Plot the data points
plt.scatter(X, Y, color='red', label='Data Points')

# Plot the regression line
plt.plot(X, Ypred, color='blue', label='Regression Line')

# Add labels and a legend
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Show the plot
plt.savefig("linearRegr.png")

HoursStudied = int(input("Enter the hours studied: "))
Prediction = m*HoursStudied + b
print("Predicted grades: ", Prediction)
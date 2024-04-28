import numpy as np
import json

# Define coefficients obtained from logistic regression model
coefficients = np.array([0.610870, 0.061321, 0.061321, 0.061321, 0.061321, 0.061321, 0.061321, 0.061321, 0.061321, 0.061321, 0.061321, 0.061321, 0.061321, 0.228137, 0.003241, 0.001955, 0.337615, 0.796090, 0.268883, 0.007434, -0.052784])  # Coefficients for predictor variables

# Define logistic function (sigmoid function)
def logistic_function(X, coefficients):
    z = np.dot(X, coefficients)  # Calculate the weighted sum of predictor variables and coefficients
    return 1 / (1 + np.exp(-z))  # Apply the logistic function to get probability

# Example predictor variables for your dataset (should be standardized if necessary)
# Replace this with your actual predictor variable values
# user = np.array([1, 1, 0, 40, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 13, 1, 1]),  # Example values for sample 1
f = open('./test_1.json')
data = json.load(f)
# print(data)
# print(data["myArray"])

# Calculate probability of binary variable occurring for each sample
probabilities = logistic_function(data['myArray'], coefficients)

# Print probabilities
print(probabilities)
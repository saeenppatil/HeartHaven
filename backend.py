import numpy as np
import json

# Define coefficients obtained from logistic regression model
coefficients = np.array([0.610870, 0.061321, 0.061321, 0.061321, 0.061321, 0.061321, 0.061321, 0.061321, 0.061321, 0.061321, 0.061321, 0.061321, 0.061321, 0.228137, 0.003241, 0.001955, 0.337615, 0.796090, 0.268883, 0.007434, -0.052784])  # Coefficients for predictor variables

# Define logistic function (sigmoid function)
def logistic_function(X, coefficients):
    z = np.dot(X, coefficients)  # Calculate the weighted sum of predictor variables and coefficients
    return 1 / (1 + np.exp(-z))  # Apply the logistic function to get probability

def age_group(age):
    if((age > 17) & (age < 24)):
        return ("18","23")
    elif((age > 24) & (age < 29)):
        return ("24","29")      
    elif((age > 29) & (age < 34)):
        return ("30","34")
    elif((age > 34) & (age < 39)):
        return ("35","39")
    elif((age > 39) & (age < 44)):
        return ("40","44")
    elif((age > 44) & (age < 49)):
        return ("44","49")
    elif((age > 49) & (age < 54)):
        return ("50","54")
    elif((age > 54) & (age < 59)):
        return ("55", "59")
    elif((age > 59) & (age < 64)):
        return ("60", "64")
    elif((age > 64) & (age < 69)):
        return ("65", "69")
    elif((age > 69) & (age < 74)):
        return ("70", "74")
    elif((age > 74) & (age < 79)):
        return ("75", "79")
    else:
        return ("80", "80+")
# Example predictor variables for your dataset (should be standardized if necessary)
# Replace this with your actual predictor variable values
# user = np.array([1, 1, 0, 40, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 13, 1, 1]),  # Example values for sample 1
f = open('./test_1.json')
data = json.load(f)
# print(data["myArray"])

# Calculate probability of binary variable occurring for each sample
probabilities = logistic_function(data['myArray'], coefficients)

# Print probabilities
print(probabilities)
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes


diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target


age = X[:, 0]
bmi = X[:, 2]


class1 = y < 100
class2 = (y >= 100) & (y <= 200)
class3 = y > 200


plt.figure(figsize=(10, 6))

plt.scatter(age[class1], bmi[class1], c='blue', label='Target < 100', alpha=0.6)
plt.scatter(age[class2], bmi[class2], c='green', label='100 ≤ Target ≤ 200', alpha=0.6)
plt.scatter(age[class3], bmi[class3], c='red', label='Target > 200', alpha=0.6)

plt.xlabel('Age (standardized)')
plt.ylabel('BMI (standardized)')
plt.title('Scatter Plot of Age vs BMI for Diabetes Dataset')
plt.legend()
plt.grid(True)
plt.show()
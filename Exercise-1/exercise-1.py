import numpy as np


# 3 måter å gjøre det på:
# y = np.dot(X,a)
# y = X.dot(a)
# y = X@a


# 1a

# Vektorer a og b i R^n
a = np.array([2, 2, 2])  # a = np.array([a1, a2, a3, ..., an])
b = np.array([1, 2, 3])  # b = np.array([b1, b2, b3, ..., bn])

# Matrisen X i R^(M x N)
# X = np.array([
#     [x11, x12, ..., x1N],  # erstatt med faktiske verdier
#     [x21, x22, ..., x2N],  # erstatt med faktiske verdier
#     # ...
#     [xM1, xM2, ..., xMN]
# ])

X = np.array([
    [1, 2, 3],  
    [10, 20, 30],  
    [100, 200, 300]
])

# Matrise-vektor-multiplikasjon
# Dette gir en ny vektor y som vil være avhengig av dimensjonene
y = np.dot(X, a)  # X * a hvis a har passende dimensjon

# Alternativt, hvis man ønsker å utføre operasjonen X.T * b (hvis dimensjonene passer)
y_trans = np.dot(b,X.T)  # X.T * b

# Resultatene kan nå brukes i videre beregninger
# print("Resultat y:", y)
# print("Resultat y_trans:", y_trans)


# * 1b Write this sum as a mathematical vector operation
a = np.array([1, 2, 3])  # a = np.array([a1, a2, a3, ..., an])
b = np.array([4, 5, 6]) # b = np.array([b1, b2, b3, ... , bn])
dot_product = np.dot(a, b)
# print(dot_product)


# * 1c Write this for loop as a mathematical vector operation and as vectorised code.
# Assuming a and b are numpy arrays
a = np.array([1, 2, 3])  # Replace with actual values
b = np.array([4, 5, 6])  # Replace with actual values
# Vectorized operation
y = np.dot(a, b)
# print(y)


# * 1d Write this for loop as a mathematical vector operation and vectorised code (assume N = n)
# Assuming X is an M x n matrix and a is an n-dimensional vector
X = np.array([
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]
  ])  # Replace with actual M x n matrix
a = np.array([1, 2, 3])  # Replace with actual n-dimensional vector

# Vectorized operation
y = np.dot(X, a)
# print(y)


# * 1e Vectorise the following algorithm (answer with code). This shouldn’t be done with traditional matrix multiplications alone:
# Assume X is an M x n matrix and a is an n-dimensional vector
X = np.array([
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]
  ]) 

a = np.array([1, 2, 3])

# Perform element-wise multiplication between X and a
# This requires broadcasting `a` to match the dimensions of `X`
elementwise_product = X * a  # This uses broadcasting, resulting in an M x n matrix

# Sum all elements of the resulting matrix
x = np.dot(X, a)
y = np.sum(elementwise_product) # Correct way

# print(x)

# print(f"Y: {y}")
# print(f"B: {b}")


# * 1f Let Z ∈ RP ×M and zij ∈ Z be the entry in row i and column j.

# Assume Z is a P x M matrix and X is an M x N matrix
Z = np.array([...])  # Replace with the actual P x M matrix
X = np.array([...])  # Replace with the actual M x N matrix
# Perform matrix multiplication
# Y = np.dot(Z, X) 

X = np.array([
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]
  ]) 

Z = np.array([
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]
  ]) 

Y = np.dot(X, Z)
print(f"{Y}")

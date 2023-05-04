from vector import Vector

# print("Range:")
# range_vector = Vector((5, 10))
# print("column:")
# column = Vector([[1.], [2.], [3.], [0]])

print("# Column vector of shape n * 1")
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1 * 5
print(v2)

print("\n# row vector of shape 1 * n")
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v1.shape)
v2 = v1 * 5
print(v2)

print("Division")
v2 = v1 / 2.0
print(v2)

# v1 / 0.0
2.0 / v1
print("\nshape1:")
print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)

print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)

print("\nshape2:")
print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)

print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)

# Example 1:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1.shape)

print("\nTranspose:")
print(v1.T())
# Expected output:
# Vector([[0.0, 1.0, 2.0, 3.0]])

print("\nTranspose:")
print(v2.T().shape)
# Expected output:
# (4,1)

print("# Example 1:")
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
print(v1.dot(v2))


print("\n# Example 2:")
v3 = Vector([[1.0, 3.0]])
v4 = Vector([[2.0, 4.0]])
print(v3.dot(v4))

print("Exemple 3:")
print(v1)
def scalar_product(vector1, vector2):
    if len(vector1) != len(vector2):
        return print("Vector dimensions are not equal")
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result


def input_vector():
    vector = []
    n = int(input("Enter the dimension of the vector: "))
    for i in range(n):
        value = int(input(f"Enter the {i + 1}th element of the vector: "))
        vector.append(value)
    return vector


vector1 = input_vector()
vector2 = input_vector()
product = scalar_product(vector1, vector2)
print("The scalar product of the two vectors is:", product)

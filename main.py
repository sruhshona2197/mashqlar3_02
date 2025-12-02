# 1-mashq
list1 = [2, 4, 6]
list2 = [3, 5, 7]

result = list(map(lambda x, y: x * y, list1, list2))
print(result)

# 2-mashq
texts = ["ab12c!", "he3llo@", "py#45thon"]

result = list(map(lambda s: ''.join(filter(str.isalpha, s)), texts))
print(result)

# 3-mashq
numbers = [2, 3, 4]
degree = 3

result = list(map(lambda x: x ** degree, numbers))
print(result)

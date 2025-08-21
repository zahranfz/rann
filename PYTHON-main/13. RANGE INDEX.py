
list_a = [1, 2, 3, 4, 5]

result_1 = list_a[:3]
result_2 = list_a[1:4]
result_3 = list_a[::2]
result_4 = list_a[1::2]
print(result_1)  # [1, 2, 3]
print(result_2)  # [2, 3, 4]
print(result_3)  # [1, 3, 5]
print(result_4)  # [2, 4]

print(7 in list_a)  # False
print(3 in list_a)  # True
print(3 not in list_a)  # False
print(7 not in list_a)  # True
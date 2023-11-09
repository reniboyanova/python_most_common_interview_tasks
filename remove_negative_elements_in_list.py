# Python3 code to demonstrate working of
# Remove Negative Elements in List
# Using filter() + lambda

# initializing list
test_list = [5, 6, -3, -8, 9, 11, -12, 2]

# printing original list
print("The original list is : " + str(test_list))

# Remove Negative Elements in List
# Using filter() + lambda
res = list(filter(lambda x: x > 0, test_list))

# printing result
print("List after filtering : " + str(res))


# 2nd Variant:
# Python3 code to demonstrate working of
# Remove Negative Elements in List

# initializing list
test_list = [5, 6, -3, -8, 9, 11, -12, 2, 0]

# printing original list
print("The original list is : " + str(test_list))

# Remove Negative Elements in List
x = list(map(str, test_list))
res = []
for i in range(0, len(x)):
    if not x[i].startswith("-") and x[i] != "0":
        res.append(test_list[i])

# printing result
print("List after filtering : " + str(res))


# 3 variant:
# Python3 code to demonstrate working of
# Remove Negative Elements in List
# Using list comprehension

# initializing list
test_list = [5, 6, -3, -8, 9, 11, -12, 2]

# printing original list
print("The original list is : " + str(test_list))

# Remove Negative Elements in List
# Using list comprehension
res = [ele for ele in test_list if ele > 0]

# printing result
print("List after filtering : " + str(res))


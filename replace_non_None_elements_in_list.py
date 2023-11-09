# Python3 code to demonstrate working of
# Replace Non-None with K
# Using map() + lambda()

# initializing list
test_list = [59, 236, None, 3, '', None, 12, 'Reni', None, 2600, 6, 9.898]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 'You are hired in Strypes, Reni!'

# Replace Non-None with K
# Using map() + lambda()
res = list(map(lambda element: K if element else element, test_list))

# printing result
print("List after replacement : " + str(res))

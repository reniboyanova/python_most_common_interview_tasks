# above code with map, filter and lambda

# Declare a list
list_with_numbers = [2, 3, 4, 5, 6]
list_with_numbers = list(filter(lambda num: num % 2, list_with_numbers))
list_with_numbers = list(map(lambda value: value * 5, list_with_numbers))

# Perform the same operation as in above post
# final_list = list(map(lambda value: value * 5, filter(lambda num: num % 2, list_with_numbers)))

if __name__ == "__main__":
    print(list_with_numbers)

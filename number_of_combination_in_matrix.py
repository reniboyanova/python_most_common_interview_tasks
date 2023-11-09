# Python3 code to demonstrate working of
# Most common Combination in Matrix

# initializing list
test_list = [[4, 5, 6, 2], [7, 6, 3, 2],
             [4, 2, 6, 7], [1, 2, 4, 6]]

# printing original list
print("The original list is : " + str(test_list))

# initialize dictionary to keep track of combination frequencies
comb_count = {}

# loop through each sublist in the input list
for sublist in test_list:
    # loop through each combination of 2 or
    # more elements in the sublist
    for i in range(len(sublist)):

        for j in range(i + 1, len(sublist)):
            comb = tuple(sorted([sublist[i], sublist[j]]))

            if comb in comb_count:
                comb_count[comb] += 1
            else:
                comb_count[comb] = 1

# find the most common combination(s) by
# looping through the dictionary
max_freq = 0
most_common_comb = []

for comb, freq in comb_count.items():

    # Update frequency if it is greater than max frequency
    if freq > max_freq:
        max_freq = freq
        most_common_comb = [comb]

    # Else do not update
    elif freq == max_freq:
        most_common_comb.append(comb)

# print the most common combination(s)
print("The Most common combination : " + str(most_common_comb))

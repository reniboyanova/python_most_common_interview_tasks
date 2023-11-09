numbers_of_searching = 0
def find_fake_bag(bags, nums, coin):
    left, right = 0, len(bags) - 1

    while left < right:
        nums += 1
        mid = (left + right) // 2
        print("mid: ", mid, " right: ", right, " left: ", left)
        sum_of_left = sum(bags[left:mid+1])
        print("bags[left:mid+1]  ", bags[left:mid+1])
        sum_of_right = sum(bags[mid+1:right+1])
        print("bags[mid+1:right+1]   ", bags[mid+1:right+1])

        if sum_of_left < sum_of_right:
            left = mid + 1
        else:
            right = mid

    return left, nums

not_real_coin = 1.1
bags = [1.0, 1.0, 1.0, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0, 1.0]
fake_bag = find_fake_bag(bags, numbers_of_searching, not_real_coin)
print(f"The fake bag is at position {fake_bag[0] + 1}\nNumber of searching: {fake_bag[1]}")





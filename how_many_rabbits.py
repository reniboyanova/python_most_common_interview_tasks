def fibonacci(n=12):

    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number_of_rabbits = 12
print(f"Number of couples are: {fibonacci(number_of_rabbits)}\nNumber of rabbits are: {fibonacci(number_of_rabbits) * 2}")

def count_rabbits(months):
    current, prev = 1, 1
    for _ in range(months - 1):
        current, prev = prev, current + prev
    return current


print(f"Rabbits couples are: {count_rabbits(12)}")

def fibonacci_generator(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

months = 12
total_rabbits = list(fibonacci_generator(months))[-1]
print(f"Total rabbits {total_rabbits} couples")
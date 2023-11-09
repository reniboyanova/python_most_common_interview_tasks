#11 . Write a decorator that would be used on a function that print a random number from 1 to 100 and
# decorators should be repeat n times function.

# Input : print_random_int --> While repeat_decorator(times=5)
# Output: 15, 20, 18, 13, 92

from random import randint


def repeat(times):
    def repeat_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                result = func(*args, **kwargs)
                if i == times - 1:
                    print(result)
                    return
                print(result, end=', ')

        return wrapper
    return repeat_decorator


@repeat(times=5)
def print_random_int(start, stop):
    """
    Function that returns a random value from 1 to 100 (including)
    To use it from random import randint
    :param start: integer to start iteration from
    :param stop: integer to stop iteration
    :return: a random number from start to stop using randint
    """
    random_num = randint(start, stop)
    return random_num

if __name__ == "__main__":
    print_random_int(1, 100)
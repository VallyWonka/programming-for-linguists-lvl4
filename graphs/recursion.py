def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def my_sum(array):
    if not array:
        return 0
    return array.pop(-1) + my_sum(array)

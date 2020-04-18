# Factorial implementation 1: iterative
def factorial_iterative(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


# Factorial implementation 2: recursive
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# Factorial implementation 2 improved: tail recursive
def factorial_tail_recursive(n):
    def tail_recursion(num, res):
        if num == 1:
            return res
        else:
            return tail_recursion(num - 1, res * num)

    return tail_recursion(n, 1)


# Factorial implementation 3: reduce (map/reduce)
def reduce_iterative(arr, func):
    res = arr[0]
    for num in arr[1:]:
        res = func(res, num)
    return res


def reduce_recursive(arr, func):
    if len(arr) == 1:
        return arr[0]
    else:
        return reduce_recursive([func(arr[0], arr[1])] + arr[2:], func)


# Factorial implementation 3: reduce (map/reduce)
def factorial_reduce(n):
    arr = [i for i in range(1, n + 1)]

    def multiply(a, b):
        return a * b

    return reduce_recursive(arr, multiply)


print(factorial_reduce(5))


# Factorial implementation 4: high order function
def higher_order(func_in):
    def func_out(n):
        arr = [i for i in range(1, n + 1)]
        from functools import reduce
        return reduce(func_in, arr)

    return func_out


factorial_higher_order = higher_order(lambda x, y: x * y)
factorial_higher_order(5)

# side effect
l = [1, 2, 3]
# [1, 2, 3]
print(l)


def list_append(arr, num):
    arr.append(num)


list_append(l, 4)
# [1, 2, 3, 4]
print(l)

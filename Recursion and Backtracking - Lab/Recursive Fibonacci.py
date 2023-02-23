def iterative_fib(number):
    num0 = 1
    num1 = 1
    result = 0
    for _ in range(number - 1):
        result = num0 + num1
        num0, num1 = num1, result
    return result


num = int(input())
print(iterative_fib(num))

def calc_fib(number):
    if number <= 1:
        return 1
    return calc_fib(number - 1) + calc_fib(number - 2)


print(calc_fib(num))
# print(calc_fib(50)) # This will hang!

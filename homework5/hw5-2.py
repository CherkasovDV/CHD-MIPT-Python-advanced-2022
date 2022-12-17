def fib(N):
    num0, num1 = 0, 1
    for k in range(N):
        yield num1
        num0, num1 = num1, num0 + num1

print(*fib(20))

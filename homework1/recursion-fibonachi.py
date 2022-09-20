def fibonachi(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n < 0:
        return "error"
    else:
        return Fib(n-1) + Fib(n-2)

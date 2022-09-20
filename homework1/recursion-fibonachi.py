def fibonachi(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n < 0:
        return "error"
    else:
        return fibonachi(n-1) + fibonachi(n-2)

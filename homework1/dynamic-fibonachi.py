def fibonachi_dinamic(n,ans=[]):
    if n<0:
        print("error")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        ans=[1,1]+[0]*(n-1)
        if ans[n] != 0:
            return ans[n]
        else:
            ans[n] = fibonachi_dinamic(n - 1) + fibonachi_dinamic(n - 2)
        return ans[n]

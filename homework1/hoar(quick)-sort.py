from random import random

def mstr(x):
    return str(round(x, 2))

def qsort(A, left=0, right=None):
    ''' quick sort of list A '''
    if right is None:
        right = len(A) - 1

    if right - left < 1:
        return
    i = left
    j = right - 1
    while i < j:
        while  A[i] < A[right]:
            i += 1
        while j > left and A[j] >= A[right]:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    
    A[right], A[i] = A[i], A[right]
    print('step :', left, i, right,'\t' ,' '.join(map(mstr, A)))
    qsort(A, left, i-1)
    qsort(A, i + 1, right)


A = [random() for _ in range(15)]
print('Start:\t\t', ' '.join(map(mstr, A)))
qsort(A)
print('Finish\t\t', ' '.join(map(mstr, A)))

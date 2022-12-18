import time
import multiprocessing as mp
import functools


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        return time.time() - start_time

    return wrapper


@time_decorator
def multiplier(matrix_1, matrix_2):
    res = []
    for count in range(len(matrix_1)):
        res.append([])
        for count1 in range(len(matrix_2[count])):
            x = 0
            for count2 in range(len(matrix_1[count])):
                x += matrix_1[count][count2] * matrix_2[count2][count1]
            res[count].append(x)
    return res


def dot_product(vector, matrix):
    res = []
    for count in range(len(matrix[0])):
        x = 0
        for count1 in range(len(vector)):
            x += vector[count1] * matrix[count1][count]
        res.append(x)
    return res


@time_decorator
def matrix_product(matrix_1, matrix_2, cores):
    pool = mp.Pool(cores)
    res = pool.map(functools.partial(dot_product, matrix=matrix_2), matrix_1)
    return res


with open("Matrix_1.csv", mode="r") as m1_csv:
    m1_str = m1_csv.readlines()
    sign = 1
    x = ""
    m1 = []
    for i in range(len(m1_str)):
        m1.append([])
        for j in m1_str[i]:
            if j == "-":
                sign = -1
            elif j == ";":
                m1[i].append(int(x) * sign)
                sign = 1
                x = ""
            elif j == "\n":
                pass
            else:
                x += j
        m1[i].append(int(x) * sign)
        sign = 1
        x = ""

with open("Matrix_2.csv", mode="r") as m2_csv:
    m2_str = m2_csv.readlines()
    sign = 1
    x = ""
    m2 = []
    for i in range(len(m2_str)):
        m2.append([])
        for j in m2_str[i]:
            if j == "-":
                sign = -1
            elif j == ";":
                m2[i].append(int(x) * sign)
                sign = 1
                x = ""
            elif j == "\n":
                pass
            else:
                x += j
        m2[i].append(int(x) * sign)
        sign = 1
        x = ""

if __name__ == "__main__":
    print(multiplier(m1, m2))
    print(matrix_product(m1, m2, 3))

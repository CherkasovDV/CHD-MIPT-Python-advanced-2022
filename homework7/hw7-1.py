def inverter(func):
    def wrapper(*args):
        arr = args
        arr = arr[::-1]
        func(*arr)
    return wrapper

def arg_printer(func):
    def wrapper(*args):
        func(*args)
        print("arguments: ")
        print(" ".join(_ for _ in args))
        print()
    return wrapper

def trier(func):
    def wrapper(*args):
        try:
            func(*args)
        except Exception:
            print("Error")
    return wrapper

def test_foo(*args):
    print(*args)

@inverter
def test_inverter(*args):
    test_foo(*args)

@arg_printer
def list_printer_test(*args):
    print("\nmax =", max(args))

@trier
def test_linear_printer(a1, a2):
    print(a1, a2)

test_input_list = [3, 14, 16, 23]
test_foo(*test_input_list)
test_inverter(*test_input_list)
list_printer_test(*test_input_list)
test_linear_printer(15, 45)

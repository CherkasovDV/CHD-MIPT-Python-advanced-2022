class Node:
    def __init__(self, value,
                 prev_pointer=None, next_pointer=None):
        self.set_value(value)
        self.set_prev(prev_pointer)
        self.set_next(next_pointer)

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next_pointer

    def get_prev(self):
        return self._prev_pointer

    def set_value(self, value):
        self._value = value

    def set_prev(self, prev_pointer):
        self._prev_pointer = prev_pointer

    def set_next(self, next_pointer):
        self._next_pointer = next_pointer

    def __str__(self):
        return str(self.get_value())

class LinkedList:
    def __init__(self, collection = None):
        self._start_pointer = Node(0)
        self._finish_pointer = Node(0)
        self._length = 0
        if collection:
            for k in range(len(collection)):
                self.append(collection[k])

    def __len__(self):
        return self._length

    def append(self, value):
        if self._length == 0:
            self._start_pointer = Node(value)
            self._finish_pointer = self._start_pointer
            self._length = 1
        else:
            self._finish_pointer.set_next(Node(value, self._finish_pointer))
            self._finish_pointer = self._finish_pointer.get_next()
            self._length += 1

    def __getitem__(self, i):
        if i < 0 or i >= self._length:
            return False
        elif i <= self._length/2:
            curr_pointer = self._start_pointer
            for j in range(i):
                curr_pointer = curr_pointer.get_next()
            return curr_pointer.get_value()
        else:
            curr_pointer = self._finish_pointer
            for j in range(self._length - 1 - i):
                curr_pointer = curr_pointer.get_prev()
            return curr_pointer.get_value()


    def __str__(self):
        arr = []
        for i in range(self._length):
            arr.append(str(self[i]))
        return "[" + ", ".join(arr) + "]"

    def pop(self, index):
        curr_point = self._start_pointer
        current_point = self._start_pointer
        for i in range(index + 1):
            curr_point = curr_point.get_next()
        for j in range(index - 1):
            current_point = current_point.get_next()
        current_point.set_next(curr_point)
        self._length -= 1

    def __add__(self, other):
        curr_p = other._start_pointer
        for i in range(other._length - 1):
            self.append(curr_p.get_value())
            curr_p = curr_p.get_next()
        return self


example1 = LinkedList()
for num1 in range(5):
    example1.append(num1)
print(example1)
example1.pop(3)
print(example1)
example21 = LinkedList()
example22 = LinkedList()
for num21 in range(10):
    example21.append(num21)
for num22 in range(5):
    example22.append(num22)
print(example22[0])
print(example22.__add__(example21))
example3 = LinkedList(collection=[3, 12, 18, 543])
print(example3[3])

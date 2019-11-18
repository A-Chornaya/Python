# Heap

class Heap:
    def __init__(self):
        self.heap_list = []

    def left(self, n):
        return self.heap_list[2*n+1] if (2*n+1) < len(self.heap_list) else None

    def right(self, n):
        return self.heap_list[2*n+2] if (2*n+2) < len(self.heap_list) else None

    def add(self, n):
        self.heap_list.append(n)
        tmp_position = len(self.heap_list) - 1
        parent_position = (tmp_position - 1) // 2
        while tmp_position > 0 and n > self.heap_list[parent_position]:
            self.heap_list[tmp_position], self.heap_list[parent_position] = self.heap_list[parent_position], self.heap_list[tmp_position]
            tmp_position = parent_position
            parent_position = (tmp_position - 1) // 2

    def get_root(self):
        root = self.heap_list[0] if self.heap_list else None
        self.heap_list[0] = self.heap_list.pop()
        temp_root = [self.heap_list[0], 0]
        while True:
            left = (self.left(temp_root[1]), 2 * temp_root[1] + 1)
            right = (self.right(temp_root[1]), 2 * temp_root[1] + 2)
            if left[0]:
                if right[0]:
                    max_child = max(left, right, key=lambda x: x[0])
                else:
                    max_child = left
            else:
                max_child = None

            if not (max_child and temp_root[0] < max_child[0]):
                break

            self.heap_list[temp_root[1]], self.heap_list[max_child[1]] = max_child[0], temp_root[0]
            temp_root[1] = max_child[1]

        return root

    def print(self):
        print(str(self.heap_list))

h = Heap()
h.add(20)
h.add(15)
h.add(11)
h.add(6)
h.add(9)
h.add(7)
h.add(8)
h.add(1)
h.add(3)
h.add(5)
h.print()

h.add(17)
h.print()

print(h.get_root())
h.print()

# [20, 15, 11, 6, 9, 7, 8, 1, 3, 5]
# ##### add new elem = 17 #####
# [20, 17, 11, 6, 15, 7, 8, 1, 3, 5, 9]
# ##### extract top (max elem) #####
# 20
# [17, 15, 11, 6, 9, 7, 8, 1, 3, 5]

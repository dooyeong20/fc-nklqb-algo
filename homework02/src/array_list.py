import array


class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('l', [0]*capacity)

    def is_empty(self):
        if self.length < 1:
            return True

        return False

    def prepend(self, value):
        if self.length >= self.capacity:
            self.increase_capacity()

        for i in range(self.length, 0, -1):
            self.array[i] = self.array[i-1]

        self.array[0] = value
        self.length += 1

    def append(self, value):
        if self.length >= self.capacity:
            self.increase_capacity()

        self.array[self.length] = value
        self.length += 1

    # 해당 메서드는 솔루션 코드를 참고하였습니다.
    def set_head(self, index):
        self.array = self.array[index:]
        self.length -= index
        self.capacity -= index

    def access(self, index):
        return self.array[index]

    def insert(self, index, value):
        if self.length >= self.capacity:
            self.increase_capacity()

        for i in range(self.length, index, -1):
            self.array[i] = self.array[i-1]

        self.array[index] = value
        self.length += 1

    def remove(self, index):
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i+1]
        self.length -= 1

    def print(self):
        for i in range(self.length):
            print(self.array[i], end=' ')
        print()

    def increase_capacity(self):
        self.capacity *= 2
        tmp = array.array('l', [0] * self.capacity)

        for i in range(self.length):
            tmp[i] = self.array[i]

        self.array = tmp


a = ArrayList(3)    # 3칸 짜리 생성
a.print()           # 빈 array list
print('is list empty?', a.is_empty())

a.prepend(5)        # a : [5]
a.print()

a.prepend(7)        # a : [7, 5]
a.prepend(9)        # a : [9, 7, 5]
a.print()


# 여기서 list capacity 두 배 증가
a.append(3)         # a : [9, 7, 5, 3]
a.append(10)        # a : [9, 7, 5, 3, 10]
a.print()

print('is list empty ?', a.is_empty())

a.remove(2)         # a : [9, 7, 3, 10]
a.print()

a.insert(1, 96)     # a : [9, 96, 7, 3, 10]
a.print()

print(f'list[2] : {a.access(2)}')  # a[2] : 7

a.set_head(2)       # a : [7, 3, 10]
a.print()

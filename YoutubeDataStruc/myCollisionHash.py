class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for data in range(self.MAX)]

    def get_hash(self, keys):
        h = 0
        for key in keys:
            h += ord(key)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        found = False
        # changing the value of an existing element
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        # for element in self.arr[h]:
        #     if element[0] == key:
        #         self.arr[h].remove(element)
        # OR
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


t = HashTable()
print(t.get_hash('march 6'))
t['march 6'] = 88
t['march 6'] = 99
t['march 17'] = 108
print(t.arr)
print(t['march 6'])
del t['march 17']
print(t.arr)
print(len(t.arr))

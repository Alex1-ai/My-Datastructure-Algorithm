# chaining solution
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    # adding key value peer
    # to get the functionality of add['march 2'] = 220
    # we need to use the python operators like __setItem__ instead of add
    # def add(self, key, val):
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        #self.arr[h] = val
        # updating values
        found = False
        for idx, element in enumerate(self.arr[h]):

            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break

        if not found:
            self.arr[h].append((key, val))

    # def get(self, key):
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


t = HashTable()
print(t.get_hash('march 6'))

print(t.get_hash('march 17'))

t['march 6'] = 120
t['march 6'] = 75
t['march 8'] = 67
t['march 9'] = 4
t['march 17'] = 459

# it has be
print(t['march 6'])
print(t['march 17'])

del t['march 17']
print(t.arr)

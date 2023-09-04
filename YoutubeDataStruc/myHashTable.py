class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for data in range(self.MAX)]

    def get_hash(self, val):
        h = 0
        for va in val:
            h += ord(va)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


h = HashTable()
print(h.get_hash('march 6'))
print(h.get_hash('march 15'))
# h.set_item('march 6', 73)
# h.set_item('march 15', 70)
# h.delete_item('march 15')
# print(h.arr)
# print(h.get_item('march 6'))

h['march 6'] = 73
h['march 15'] = 70
del h['march 15']
print(h.arr)


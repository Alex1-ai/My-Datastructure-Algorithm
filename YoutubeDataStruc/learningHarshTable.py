# def get_hash(key):
#     h = 0
#     for char in key:
#         # ord('a')
#         # finds the ascii value for a

#         h += ord(char)
#         # 100 is the number of element in the dictionary
#     return h % 100


# print(get_hash('march 6'))


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

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
        self.arr[h] = val

    # def get(self, key):
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()
# print(t.get_hash('march 6'))
# print(t.add('march 6', 130))

# print(t.arr)
# print(t.get('march 6'))
t['march 6'] = 130
t['march 1'] = 20
t['march 17'] = 27
print(t['march 6'])
print(t.arr)
del t['march 6']
print(t.arr)

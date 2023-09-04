class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] == None:
            self.arr[h] = (key,value)

        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key,value)
        print(self.arr)

    def __getitem__(self,key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]
    
    def find_slot(self, key,index):
        probe_range = self.get_prob_range(index)
        for prob_index in probe_range:
            # to set item
            if self.arr[prob_index] is None:
                return prob_index
            
            # to get item
            if self.arr[prob_index][0] == key:
                return prob_index 

        raise Exception("Hash Map Full")

    def get_prob_range(self, index):
        # getting from the index that is full to the end and also getting 
        # from the begining of array to that index

        return [*range(index, len(self.arr))] + [*range(0,index)]

    def __delitem__(self,key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return # item not found so return
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
            print(self.arr)


t = HashTable()
t['march 6'] = 20
t['march 17'] = 88
t['march 33'] = 234
t['march 33'] = 999
t['april 2'] = 123
t['april 4'] = 91






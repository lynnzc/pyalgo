# !/usr/bin/python
# coding:utf-8


class HashTable:

    def __init__(self, tableSize=10):
        self.table = [[] for i in range(tableSize)]
        # current number of entries in the hash table
        self.size = 0
        self.maxSize = tableSize
        # default factor for rehashing
        self.factor = 3 / 4

    # return whether a entry with correspondind key exists in the hash table
    def contains(self, key):
        if self.isEmpty():
            return

        hashIndex = self.hashFun(key)

        for entry in self.table[hashIndex]:
            if entry.key == key:
                return True

        return False

    # put a entry with corresponding key and value to the hash table
    def put(self, key, value):
        if self.contains(key):
            print("the key already exists")
            return

        hashIndex = self.hashFun(key)

        entry = self.Entry(key, value)
        self.table[hashIndex].append(entry)
        # rehash
        if self.size >= self.maxSize * self.factor:
            # double the size
            self.table += [[] for i in range(self.maxSize)]
            self.maxSize *= 2

        self.size += 1

    # return the value of its corresponding key
    def get(self, key):
        if self.isEmpty():
            return None

        hashIndex = self.hashFun(key)

        for entry in self.table[hashIndex]:
            if entry.key == key:
                return entry.value
        return None

    # remove the entry with corresponding key
    def remove(self, key):
        if self.isEmpty():
            return False

        hashIndex = self.hashFun(key)

        for entry in self.table[hashIndex]:
            if entry.key == key:
                self.table[hashIndex].remove(entry)
                self.size -= 1
                return True

        return False

    # very simple hash function of the key to compute the index
    def hashFun(self, key):
        return (int(key) % self.maxSize)

    # return whether the hash table is empty or not
    def isEmpty(self):
        return (self.size == 0)

    # return the current number of entries of the hash table
    def itemCount(self):
        return self.size

    class Entry:

        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value

        def __str__(self):
            print('key: %s \n value: %s' % (str(self.key), str(self.value)))

"""
Project 7 - Hash Tables
CSE331 - F19
Created By: Wendy Fogland
"""


class HashNode:
    """
    DO NOT EDIT
    """

    def __init__(self, key, value, available=False):
        self.key = key
        self.value = value
        self.is_available = available

    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value


class HashTable:
    """
    Hash Table Class
    """

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity=7):
        """
        DO NOT EDIT
        Initializes hash table
        :param capacity: how much the hash table can hold
        """

        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

        for prime in self.primes:
            if self.capacity <= prime:
                self.prime = prime
                break

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """

        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        """
        DO NOT EDIT
        Represents the table as a string
        :return: string representation of the hash table
        """

        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent

    def _is_available(self, j):
        """
        DO NOT EDIT
        Check if the index in the table is available/empty
        :param j: index in the table
        :return: True if available or empty, false otherwise
        """
        return self.table[j] is None or self.table[j].is_available is True

    def hash_first(self, key):

        """
        DO NOT EDIT
        Converts key, a string, into a bin number for the hash table
        :param key: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if val is an empty string
        """

        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def hash_second(self, key):
        """
        Hashes key based on prime number for double hashing
        DO NOT EDIT
        :param key: key to be hashed
        :return: a hashed value
        """

        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        hashed_value = self.prime - (hashed_value % self.prime)
        if hashed_value % 2 == 0:
            hashed_value += 1

        return hashed_value

    def double_hashing(self, key, inserting=False):
        """
        Finds index where the key can be inserted
        :param key: [string] value used to hash
        :param inserting: [bool] value that tells function whether inserting or not
        :return: [int] index of the element if already exists, otherwise next open index
        """
        first_hash = self.hash_first(key)
        second_hash = self.hash_second(key)
        # if inserting
        if inserting is True:
            # when inserting use the is_available attribute to spot open values
            if self.table[first_hash] is None or self.table[first_hash].is_available:
                return first_hash
            else:  # if Node in spot check to see if key is duplicate
                if self.table[first_hash].key == key:
                    return first_hash
                else:
                    i = 0
                    hash_step = (first_hash + i * second_hash) % self.capacity
                    # if index is None return index
                    while self.table[hash_step] is not None and \
                            (self.table[hash_step].is_available is False):
                        i += 1
                        hash_step = (first_hash + i * self.hash_second(key)) % self.capacity
                    return hash_step
        # if searching or deleting
        else:  # is_available attribute not needed for deleting or searching
            if self.table[first_hash] is None:
                return first_hash
            else:  # if Node in spot check to see if key is duplicate
                if self.table[first_hash].key == key:
                    return first_hash
                else:
                    i = 0
                    hash_step = (first_hash + i * second_hash) % self.capacity
                    # if index is None return index
                    while self.table[hash_step] is not None and \
                            (self.table[hash_step].is_available or self.table[hash_step].key != key):
                        i += 1
                        hash_step = (first_hash + i * self.hash_second(key)) % self.capacity
                    return hash_step

    def insert(self, key, value):
        """
        Inserts key value pair into hash table
        :param key: [string] key to insert
        :param value: [int] value to insert
        :return: no return, Node is placed into hash table
        """
        index = self.double_hashing(key, True)
        if self.table[index] is None or self.table[index].key is None:
            self.size += 1
        self.table[index] = HashNode(key, value)
        while self.size / self.capacity >= 0.4:
            self.grow()

    def search(self, key):
        """
        Searches the hash table for the key
        :param key: [string] key to search for
        :return: [HashNode] Node if found, None if not found
        """
        index = self.double_hashing(key, False)
        searchNode = self.table[index]
        if searchNode is None or searchNode.key != key:
            return None
        else:
            return searchNode

    def grow(self):
        """
        Grows the hash table if load factor surpasses 0.4 and rehashes
        :return: no return, but table is doubled in size
        """
        self.capacity = self.capacity * 2
        for prime in self.primes:
            if self.capacity < prime:
                self.prime = prime
                break
        self.rehash()

    def rehash(self):
        """
        rehashes the table after it is doubled in size
        :return: No return but Nodes are rehashed into their new indexes of large table
        """
        old = self.table  # use iteration to record existing items
        self.table = self.capacity * [None]  # then reset table to desired capacity
        self.size = 0  # n recomputed during subsequent adds
        for node in old:
            if node is not None:
                if node.key is not None:
                    self.insert(node.key, node.value)

    def delete(self, key):
        """
        Deletes the node from the table
        :param key: [string] key to delete
        :return: No return but key is deleted from table if present
        """
        deleteNode = self.search(key)
        if deleteNode is not None:
            deleteNode.key = None
            deleteNode.value = None
            deleteNode.is_available = True
            self.size -= 1


def anagrams(string1, string2):
    """
    Determines if two strings are anagrams
    :param string1: [string] first string
    :param string2: [string2] second string
    :return: [bool] True if anagrams, False otherwise
    """
    ht1 = HashTable(1)
    ht2 = HashTable(1)
    # puts first string into a hash table
    for i in string1:
        i = i.lower()
        if i == ' ':
            continue
        search = ht1.search(i)
        if search is not None:
            search.value += 1 # keeps count of each character
        else:
            ht1.insert(i, 1)
    # puts second string into hash table
    for i in string2:
        i = i.lower()
        if i == ' ':
            continue
        search = ht2.search(i)
        if search is not None:
            search.value += 1  # keeps count of each character
        else:
            ht2.insert(i, 1)
    # determines if both hash tables contain the same variables with count
    for i in string1:
        i = i.lower()
        if i == ' ':
            continue
        if ht2.search(i) is None:
            return False
        if ht1.search(i) != ht2.search(i):
            return False
    return True

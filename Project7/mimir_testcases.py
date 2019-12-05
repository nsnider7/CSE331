import unittest

from HashTable import HashNode, HashTable, anagrams


class TestProject7(unittest.TestCase):

    def test_double_hashing(self):
        ht = HashTable()

        index = ht.double_hashing("abc", True)
        assert (index == 0)

        index = ht.double_hashing("def", True)
        assert (index == 3)

        index = ht.double_hashing("dog", True)
        assert (index == 1)


        test = ht.double_hashing("a", True)
        test = ht.double_hashing("def", True)
        test = ht.double_hashing("bb", True)

    def test_insert(self):
        ht = HashTable()  # if first isnt enough!!!!

        solution = [HashNode("abc", 4), None, None, HashNode("def", 12), None, None, None]
        ht.insert("abc", 4)
        index = ht.double_hashing("abc", True)
        assert index == 0
        ht.insert("def", 12)

        assert (ht.size == 2)
        assert (ht.capacity == 7)

        assert (ht.table == solution)
        index1 = ht.hash_first('aa')

        ht.insert("abc", 44)  # Reassignment
        assert (ht.table[0].value == 44)
        ht.insert("aaa", 6)
        ht.insert("bbb", 22)

        ht = HashTable(4)
        ht.insert("a", 3)
        ht.insert("aa", 3)
        print(ht)

    def test_search(self):
        ht = HashTable()
        ht.insert("frog", 2)
        ht.insert("cow", 12)
        ht.insert("tiger", 1)
        ht.insert("ostrich", 10)

        found_node = ht.search("frog")
        sol_node = HashNode("frog", 2)

        print(ht)
        assert (sol_node == found_node)

    def test_grow(self):
        ht = HashTable()

        for i in range(1, 5):
            ht.insert(i * 'a', i)
        assert ht.size == 4
        assert ht.capacity == 14

    def test_delete(self):
        ht = HashTable(12)
        reassignment = [None,None,None,None,HashNode('test', 5),None,HashNode('abc', 3),None,HashNode('brain', 1),None,HashNode('bean', 4),
                        None,None,None,None,None,None,None,HashNode('five', 5),None,None,None,None,None]
        solution1 = [None, None, None, None, HashNode('test', 3), None,
                     HashNode('abc', 1), HashNode('five', 5), None, None, HashNode('bean', 4), None]
        solution = [None, None, None, None, HashNode(None, None), None,
                    HashNode(None, None), HashNode(None, None), None, None, HashNode(None, None), None]
        rehashed_solution = [None, None, None, None, None, None, None, None, None, None, None, None]
        ht.insert("abc", 1)
        ht.insert("test", 3)
        ht.insert("bean", 4)
        ht.insert("five", 5)
        print(ht.table[0].is_available)
        # assert (solution1 == ht.table)
        # assert ht.size == 4
        # ht.delete("abc")
        # ht.delete("test")
        # ht.delete("five")
        # ht.delete("bean")
        # assert ht.size == 0
        # ht.insert("abc", 1)
        # ht.insert("test", 3)
        # ht.insert("bean", 4)
        # ht.insert("five", 5)
        # ht.insert('abc', 3)  # over write without increasing size
        # ht.insert("test", 5)
        # ht.insert("brain", 1)
        # ht.insert("brain", 1)
        # assert (reassignment == ht.table)
        # assert ht.size == 5
        #
        # solution = [None, None, None, None, HashNode(None, None), None,
        #             HashNode(None, None), HashNode(None, None), None, None, HashNode(None, None), None]
        # ht = HashTable()
        # ht.insert("abc", 1)
        # assert ht.size == 1
        # print(ht)
        # ht.delete("abs")
        # assert ht.size == 1
        # # ht.insert("abc", 9)
        # # print(ht)

    def test_anagrams(self):
        # is_anagram = anagrams("listen", "silent")
        # assert is_anagram

        # is_anagram = anagrams("countryroad", "dountryroad")
        # assert not is_anagram

        is_anagram = anagrams("Jumping Jamber", "big men jump jar")
        assert is_anagram

        # Even though all letters are used, the period makes it not an anagram
        is_anagram = anagrams("kinder.", "red ink")
        assert not is_anagram


if __name__ == '__main__':
    unittest.main()

import unittest
from LinkedList import insert, remove, remove_all, to_string, search, sum_list, \
    count, reverse, length, remove_fake_requests, LinkedNode


class TestProject2(unittest.TestCase):
    def test_insert(self):
        linked_list = insert(0)
        insert(1, linked_list)
        insert(2, linked_list)

        for i in range(0, 3):
            assert linked_list.value == i
            linked_list = linked_list.next

    def test_to_string(self):
        list1 = insert(0)
        insert(1, list1)
        insert(2, list1)
        insert(3, list1)
        test = to_string(list1)


        assert to_string(list1) == "0, 1, 2, 3"
    #
    def test_length(self):
        list1 = insert(1)
        insert(2, list1)
        insert(3, list1)
        insert(7, list1)
        print(length(list1))

        assert length(list1) == 4

    def test_search(self):
        list1 = insert(0)
        insert(1, list1)
        insert(2, list1)
        value = search(2, list1)
        print(value)
        assert search(2, list1)
        assert not search(3, list1)

    def test_count(self):
        list1 = insert(0)
        insert(1, list1)
        insert(2, list1)

        assert count(0, list1) == 1
        assert count(1, list1) == 1
        assert count(2, list1) == 1
    #
    def test_sum_list(self):
        list1 = insert(0)
        insert(1, list1)
        insert(2, list1)
        insert(45, list1)
        assert sum_list(list1) == 48

    def test_remove(self):
        test = LinkedNode(5)

        list1 = insert(0)
        insert(1, list1)
        # insert(2, list1)
        # insert(3, list1)
        list1 = remove(1, list1)
        assert list1.value == 0
        # for i in [1, 2]:
        #     assert list1.value == i
        #     list1 = list1.next
        # #
        # assert list1 == None
    #
    # def test_remove_all(self):
        # if ele is head or 2/3 at head check
        # if ele is tail or 2/3 at tail check
        # if ele is head and tail check
        # if len = 1 and ele = value check
        # if len = 2 and 2 values that need to be removed check
        # if len = 1 and ele and != value check
        # if all elements need removal check
        # regular scattered removal check
        # middle 2 check
        # middle 3 check
        # middle 4 check

        list1 = insert(0)
        insert(2, list1)

        insert(2, list1)
        insert(2, list1)
        insert(2, list1)
        insert(4, list1)
        # insert(2, list1)

        list1 = remove_all(2, list1)
        # assert list1 == None
        for i in [0,4]:
            assert list1.value == i
            list1 = list1.next

        # assert test_list == None
    #
    def test_reverse(self):
        list1 = insert(1)
        insert(2, list1)
        insert(3, list1)
        # insert(3, list1)

        list1 = reverse(list1)
        print(list1.value)
        for i in [3, 2, 1]:
            assert list1.value == i
            list1 = list1.next

    def test_fake_requests(self):
        # no dups check
        # head 2 check
        # head 3 check
        # head 4 check
        # middle 2 check
        # middle 3 check
        # middle 4 check
        # tail 2 check
        # tail 3 check
        # remove all 2v2, 2v3, 3v2, 3v3, all (any size) check
        # 1 ele check
        # only 2,3,4 to remove check


        # if no duplicates
        requests = insert(0)
        insert(1, requests)
        insert(2, requests)
        insert(3, requests)
        insert(4, requests)
        insert(5, requests)
        real_requests = remove_fake_requests(requests)
        for i in [0,1,2,3,4,5]:
            assert real_requests.value == i
            real_requests = real_requests.next

        # head 2
        requests = insert(0)
        insert(0, requests)
        insert(2, requests)
        insert(3, requests)
        insert(4, requests)
        insert(5, requests)
        real_requests = remove_fake_requests(requests)
        for i in [2,3,4,5]:
            assert real_requests.value == i
            real_requests = real_requests.next

        # head 3
        requests = insert(0)
        insert(0, requests)
        insert(0, requests)
        insert(3, requests)
        insert(4, requests)
        insert(5, requests)
        real_requests = remove_fake_requests(requests)
        for i in [3,4,5]:
            assert real_requests.value == i
            real_requests = real_requests.next

        # head 4
        requests = insert(0)
        insert(0, requests)
        insert(0, requests)
        insert(0, requests)
        insert(4, requests)
        insert(5, requests)
        insert(6, requests)
        real_requests = remove_fake_requests(requests)
        for i in [4,5,6]:
            assert real_requests.value == i
            real_requests = real_requests.next

        # middle 2
        requests = insert(0)
        insert(1, requests)
        insert(2, requests)
        insert(2, requests)
        insert(3, requests)
        insert(4, requests)
        real_requests = remove_fake_requests(requests)
        for i in [0,1,3,4]:
            assert real_requests.value == i
            real_requests = real_requests.next

        # middle 3
        requests = insert(0)
        insert(1, requests)
        insert(2, requests)
        insert(2, requests)
        insert(2, requests)
        insert(4, requests)
        real_requests = remove_fake_requests(requests)
        for i in [0, 1, 4]:
            assert real_requests.value == i
            real_requests = real_requests.next

        # middle 4
        requests = insert(0)
        insert(1, requests)
        insert(2, requests)
        insert(2, requests)
        insert(2, requests)
        insert(2, requests)
        insert(5, requests)
        real_requests = remove_fake_requests(requests)
        for i in [0, 1, 5]:
            assert real_requests.value == i
            real_requests = real_requests.next

        # tail 2/3/4 check
        requests = insert(0)
        insert(1, requests)
        insert(2, requests)
        insert(5, requests)
        insert(5, requests)
        insert(5, requests)
        insert(5, requests)
        real_requests = remove_fake_requests(requests)
        for i in [0, 1, 2]:
            assert real_requests.value == i
            real_requests = real_requests.next

        # multiple
        requests = insert(0)
        insert(0, requests)
        insert(0, requests)
        insert(5, requests)
        insert(5, requests)
        insert(5, requests)
        # insert(6, requests)
        real_requests = remove_fake_requests(requests)
        assert real_requests == None

        # multiple
        requests = insert(1)
        insert(1, requests)
        insert(1, requests)
        # insert(3, requests)
        insert(2, requests)
        insert(2, requests)
        insert(2, requests)
        # insert(5, requests)

        real_requests = remove_fake_requests(requests)
        assert real_requests == None
        # for i in [4,5]:
        #     assert real_requests.value == i
        #     real_requests = real_requests.next




if __name__ == "__main__":
    unittest.main()

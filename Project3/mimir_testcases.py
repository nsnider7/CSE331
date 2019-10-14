import unittest
<<<<<<< HEAD
from QuickSort import quick_sort
=======
# from QuickSort import quick_sort
from QuickSort import *

>>>>>>> f39e3b14ac55bc1f92fc152e7e5a0672b52e0cc7
from DoublyLinkedList import DLL
from InsertionSort import insertion_sort


class TestProject1(unittest.TestCase):

    # def test_accessors(self):
    #     dll = DLL([])
    #
    #     assert dll.get_size() == 0
    #     assert dll.get_head() is None
    #     assert dll.get_tail() is None
    #
    #     orig = [2,1,4,5,3]
    #     dll = DLL(orig)
    #     quick_sort(dll, dll.head, dll.tail, dll.size, 0)

        # test large inputs
        # largelist = []
        # i = 0
        # while i < 999:
        #     largelist.append(i)
        #     i+=1
        # dll = DLL(largelist[::-1])
        # quick_sort(dll, dll.head, dll.tail, dll.size, 100)
        # assert dll == DLL(largelist)
        # assert dll.get_size() == 999
        # assert dll.get_head().get_value() == 0
        # assert dll.get_tail().get_value() == 998
        #

        orig = [9,2,7,1,3,6,4,5]
        dll = DLL(orig)
        quick_sort(dll, dll.head, dll.tail, dll.size, 4)
        print(dll)
        assert dll == DLL(sorted(orig))
        assert dll.get_size() == 8
        assert dll.get_head().get_value() == 1
        assert dll.get_tail().get_value() == 9
<<<<<<< HEAD
        #
        # orig = [1, 1, 1, 0, 1, 1, 1]
        #
        # dll = DLL(orig)
        # quick_sort(dll, dll.head, dll.tail, dll.size, 0)
        #
        # # print(dll)
        # assert dll == DLL(sorted(orig))
        # assert dll.get_size() == 7
        # assert dll.get_head().get_value() == 0
        # assert dll.get_tail().get_value() == 1
        #
        # orig = [-1,4,5,-2,0]
        # dll = DLL(orig)
        # quick_sort(dll, dll.head, dll.tail, dll.size, 0)
        # # print(dll)
        # # print(dll.c)
        # assert dll == DLL(sorted(orig))
        # assert dll.c == 0
        #
        # orig = [3,2,1]
        # dll = DLL(orig)
        # quick_sort(dll, dll.head, dll.tail, dll.size, 0)
        # # print(dll)
        # # print(dll.c)
        # assert dll == DLL(sorted(orig))
        # assert dll.c == 0



    def test_insertion(self):
        dll = DLL([])

        assert dll.get_size() == 0
        assert dll.get_head() is None
        assert dll.get_tail() is None

        # normal
        orig = [6, 1, 4, 7, 3, 5, 10, 8, 9, 2]
        dll = DLL(orig)
        insertion_sort(dll, dll.get_head(), dll.get_tail())
        assert dll == DLL(sorted(orig))

        # size 1
        orig = [6]
        dll = DLL(orig)
        insertion_sort(dll, dll.get_head(), dll.get_tail())
        assert dll == DLL(sorted(orig))

        # acending
        orig = [6,5,4,3,2,1]
        dll = DLL(orig)
        insertion_sort(dll, dll.get_head(), dll.get_tail())
        assert dll == DLL(sorted(orig))

        # scattered
        orig = [1,8,2,7,3,6,4,6]
        dll = DLL(orig)
        insertion_sort(dll, dll.get_head(), dll.get_tail())
        assert dll == DLL(sorted(orig))

        # size 2
        orig = []
        dll = DLL(orig)
        insertion_sort(dll, dll.get_head(), dll.get_tail())
        assert dll == DLL([])

    def test_quick_sort(self):
        orig = [9, 2, 7, 1, 3, 6, 4, 5]
        dll = DLL(orig)
        quick_sort(dll, dll.head, dll.tail, dll.size, 0)
        assert dll == DLL(sorted(orig))
        assert dll.c == 0

        orig = [-636, -676, 387, -203, 673, -844, 883, -711, -814, -774, -491, 40, 633, 425, -168, 711, -173, -375, 286,
                142, 383, -891, -240, 203, -262, -247, -525, 550, 62, 343, 740, 711, -152, -756, -105, -289, -406, -471,
                798, -688, 851, 730, -989, -357, -297, -785, 777, -39, -148, -74, 603, -282, -44, 506, 345, 226, 866,
                597, 960, 224, 891, 197, -793, 641, 978, -462, -86, -689, -342, 858, -500, 458, -885, 718, 831, -426,
                319, 459, 653, -710, 854, 812, -666, 464, -326, 573, 153, -529, -782, 736, -296, -841, 817, 62, 289,
                -777, -698, 829, -34, -16, 948, 344, 449, -937, 143, 607, 134, 27, 718, -921, -317, 973, 6, -703, -838,
                718, 905, -372, 630, -858, -329, -446, 429, 760, 236, -487, -593, 274, -397, -228, 269, 842, 840, -597,
                1000, -857, 919, 139, -78, -339, 701, -410, -508, 603, -214, 208, 661, -733, 313, -326, 888, 994, 996,
                -798, -597, 18, 260, 853, -850, -713, -842, 541, 346, -79, 782, 658, -174, -670, -593, 909, -725, -192,
                -507, 995, -68, 216, 851, -454, 550, -74, 37, 441, -227, 227, 624, 606, -550, -341, 589, -702, -64, -30,
                -56, 724, 590, -665, 928, -538, -932, 237, 75, -489, 931, -937, -261, -260, -129, 177, 244, 126, -481,
                -962, 588, -457, -116, 364, -856, 665, -299, -59, -698, -105, -157, -603, -398, -529, 727, 874, 440,
                -311, -697, 388, 300, -195, 551, -225, -485, -702, 77, 82, 620, -595, -122, 132, -962, 176, -949, 218,
                -785, -13, -302, -74, -560, -113, -411, -152, 288, -659, -257, -276, -552, -821, -435, -278, 579, 978,
                934, -33, -987, 147, 474, 451, 132, -450, -22, -347, 591, -671, -361, -83, 5, 890, 946, -669, -910, -69,
                -850, 29, 118, -28, -700, -123, 958, 159, -845, 59, -67, -48, -705, -991, -231, 171, 865, -430, -642,
                938, -309, -490, 812, 976, -882, 965, -267, -115, 776, -892, -997, -283, -848, -383, 472, 719, -856,
                -521, -279, 12, 99, -431, 604, 247, -366, 785, 346, 90, 762, -737, 500, 650, 548, -206, 778, 493, 235,
                -723, 475, -569, -338, -146, -477, 512, -915, -536, 975, 59, 583, 852, -292, -825, -475, -164, -384,
                482, 385, -823, 394, -913, -313, 233, 623, 185, 976, 19, -303, 440, -500, 265, -317, -416, 126, -191,
                592, 12, 626, -244, -78, -488, -413, 259, 817, 199, -739, -3, -365, -120, -21, 782, 461, -128, -368,
                739, -425, 396, 616, 446, -120, -997, 774, 515, -810, 541, 180, -786, -977, -425, 904, -853, 372, -496,
                -688, -58, 46, -624, -677, 455, -409, 224, 631, -79, 873, 120, 895, 351, 686, -647, -579, 112, 72, -505,
                7, -437, -54, -951, -199, -866, 865, -298, 320, -36, 443, -811, 916, -391, 474, 122, -474, -993, 201,
                -385, 841, 976, 679, 23, -277, -92, -351, 522, 270, -502, -974, 466, -329, -414, 837, 268, 248, 184,
                129, -643, 727, 912, -260, 207, -294, 414, -210, -660, -551, 908, 876, -181, -502, -707, -730, 923, 152,
                -364, -749, -859, -169, -821, -786, -228, -993, -717, -686, 626, 922, 780, -967, 155, -898, -342, -88,
                674, 429, -873, 10, -190, -404, 144, 958, 119, -74, -348, -420, -373, -41, -224, -142, 682, 420, -681,
                -242, -125, -959, 575, -303, -779, 100, -442, 625, -69, 438, 889, 383, 551, 117, -137, 556, 848, -865,
                100, -598, -355, 684, -957, 174, -157, -195, -253, 383, -1, -453, -521, 336, 704, -25, 929, 566, -83,
                846, 560, 189, -830, 294, 84, 598, 790, 837, 559, -81, -964, -511, 817, 638, 914, -279, 236, 747, 42,
                -18, 927, 924, 694, -187, -504, 444, 229, 716, -858, 988, -94, 907, -747, -232, 938, -674, -119, -369,
                118, 652, -136, 801, -995, 531, 615, 444, -27, 315, 431, 941, 210, 110, -245, -244, -395, 291, -722,
                752, -762, 415, -771, -777, 479, 720, 581, -673, -918, -254, -586, 355, -230, -340, -216, 50, -345, -50,
                458, 142, -335, -413, 539, 702, 866, -9, 569, -589, 194, 785, -409, 59, -320, 138, 309, -277, 632, -530,
                -368, 811, -742, -658, -138, 568, 25, -369, -436, -508, -255, 520, -514, -797, 814, -5, 860, -15, -590,
                819, -854, 732, -167, -425, -205, -564, -320, -395, -389, -743, -816, -751, 885, 812, -377, -872, -736,
                -461, -845, 446, 776, -324, 932, 588, 123, 340, -590, 421, -819, -52, -603, 391, -868, 98, 680, 172, 12,
                -49, 298, -936, -638, 441, 587, 719, -118, 131, 707, -37, 200, -450, -626, -397, 849, -474, -607, 885,
                502, -215, 91, -774, 514, 928, -527, -53, 993, -326, 957, 238, 657, -164, -911, 535, 554, -224, 522,
                -490, -638, -231, 637, -436, 785, -125, -680, 224, -918, -672, 373, -371, -125, -206, -899, 805, 271,
                -395, 123, -93, -38, -770, 666, 551, 651, -584, -388, 180, -242, -691, 970, 160, 622, 473, 740, 202,
                -664, 925, 567, 294, 280, -759, 207, 110, -478, -314, -495, 485, -265, 142, -865, -909, 329, 121, 666,
                -163, 783, -156, 186, 107, 502, 950, -827, -737, -822, 823, 2, 910, 618, -836, -716, 726, 362, 573,
                -476, -516, 714, -417, 343, 198, 515, 842, 657, -77, -719, 49, 971, 328, -750, -316, 740, -857, -768,
                -147, 419, 322, -678, -67, -535, -492, -599, 305, 182, -674, -147, 109, 123, 817, -294, -420, -904,
                -132, 43, 855, 825, 666, 93, 961, 295, -354, -10, 860, -292, 881, -787, 128, 831, 364, 382, -222, 394,
                724, -221, -869, 637, 571, -352, -789, -756, 191, 143, 464, -236, 669, 379, -42, -653, -856, 64, -89,
                -636, -473, -147, -712, 758, -597, 692, -520, 677, 410, 560, -516, 304, 961, 547, 189, 929, -995, -894,
                -46, -316, 189, -343, -146, -802, 677, 566, 966, -736, -194, -50, 435, -37, 581, -654, -982, 423, -587,
                975, -652, 547, -545, -89, -226, 309, -982, -370, 612, 518, -805, 904, 927, -382, 467, 3, -100, -624,
                614, 885, -379, -893, -166, -665, -590, -584, -868, -334, 122, -730, -286, -873, -983, -329, 630, -417,
                609, 451, -488, 778, 39, 648, -367, -949, -96, -1000, -157, 949]
        # dll = DLL(orig)
        # quick_sort(dll, dll.head, dll.tail, dll.size, 4)
        # print(dll)
        # print(dll.c)
        # assert dll == DLL(sorted(orig))

    def test_guick_insertion(self):
        # checking c value
        # orig = [20, 18, 4, 2, 5, 7, 13, 10, 11, 3, 1, 17, 16, 9, 6, 8, 15, 12, 14, 19]
        # dll = DLL(orig)
        # quick_sort(dll, dll.head, dll.tail, dll.size, 15)
        # assert dll == DLL(sorted(orig))
        # assert dll.c == 2

        # c value check
        orig = [1,1,1,1,1,1,1,0]
        dll = DLL(orig)
        quick_sort(dll, dll.head, dll.tail, dll.size, 2)
        print(dll.c)
        assert dll == DLL(sorted(orig))
        # assert dll.c == 7

    def test_application(self):
        # simple test
        dll = DLL([2,1,1])
        dll.count_unique()
        assert dll == DLL([2,1,2])

        #mimir test
        dll = DLL([1,3,3,4,4,4])
        dll.count_unique()
        assert dll == DLL([1,3,2,4,3])
        assert dll.get_head().get_value() == 1
        assert dll.get_tail().get_value() == 3
        assert dll.get_size() == 5

        # two items that are the same
        dll = DLL([4,4])
        dll.count_unique()
        assert dll == DLL([4,2])
        assert dll.get_head().get_value() == 4
        assert dll.get_tail().get_value() == 2
        assert dll.get_size() == 2

        # 3 items that are the same
        dll = DLL([1,1,1,1,1,1,1,1])
        dll.count_unique()
        assert dll == DLL([1,8])
        assert dll.get_head().get_value() == 1
        assert dll.get_tail().get_value() == 8
        assert dll.get_size() == 2

        # 3 items that are the same
        dll = DLL([])
        dll.count_unique()
        assert dll == DLL([])
        # assert dll.get_head().get_value() == 1
        # assert dll.get_tail().get_value() == 3
        # assert dll.get_size() == 2

        # 2 numbers that are duplicated a lot
        dll = DLL([0,0,0,0,0,0,1,1,1,1,1])
        dll.count_unique()
        # print(dll)
        assert dll == DLL([0,6,1,5])
        assert dll.get_head().get_value() == 0
        assert dll.get_tail().get_value() == 5
        assert dll.get_size() == 4

        # regular test
        dll = DLL([0,1,1,2,3,3,3,3,4,5,5,6])
        dll.count_unique()
        # print(dll)
        assert dll == DLL([0,1,2,2,3,4,4,5,2,6])
        assert dll.get_head().get_value() == 0
        assert dll.get_tail().get_value() == 6
        assert dll.get_size() == 10

        # 100 1's
        dll = DLL([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
        dll.count_unique()
        # print(dll)
        assert dll == DLL([1,1,0,0])
        assert dll.get_head().get_value() == 1
        assert dll.get_tail().get_value() == 0
        assert dll.get_size() == 4

        # triple digit
        dll = DLL([1,1,1,1,1,1,1,1,1,1,1,1,2,2,2])
        dll.count_unique()
        # print(dll)
        assert dll == DLL([1,1,2,2,3])
        assert dll.get_head().get_value() == 1
        assert dll.get_tail().get_value() == 3
        assert dll.get_size() == 5

        # # 20 1's
        # dll = DLL([4,3,2,1])
        # dll.count_unique()
        # print(dll)
        # assert dll == DLL([1,2,3,4])
        # assert dll.get_head().get_value() == 1
        # assert dll.get_tail().get_value() == 4
        # assert dll.get_size() == 3


    #
    # def test_partition(self):
    #     # 1 ele check
    #     dll = DLL([2])
    #     test = partition(dll.get_head(), dll.get_tail())
    #     # print(dll)
    #     # print(test)
    #
    #     # 2 ele unsorted check
    #     dll = DLL([2,1])
    #     test = partition(dll.get_head(), dll.get_tail())
    #     # print(dll)
    #     # print(test)
    #     # decending list of 4 check
    #     dll = DLL([4,3,2,1])
    #     test = partition(dll.get_head(), dll.get_tail())
    #     # print(dll)
    #     # print(test)
    #
    #     # random unordered list of 4
    #     dll = DLL([4,1,2,3])
    #     test = partition(dll.get_head(), dll.get_tail())
    #     # print(dll)
    #     # print(test)
    #     # duplicate list
    #     dll = DLL([1,1,1,1,0,1,1,1])
    #     test = partition(dll.get_head(), dll.get_tail())
    #     # print(dll)
    #     # print(test)
    #
    #     dll = DLL([3,6,5,4])
    #     test = partition(dll.get_head().get_next(), dll.get_tail())
    #     # print(dll)
    #     # print(test)
    #     # dll = DLL([2,1])
=======
        # #
        orig = [1, 1, 1, 0, 1, 1, 1]

        dll = DLL(orig)
        quick_sort(dll, dll.head, dll.tail, dll.size, 0)

        # print(dll)
        assert dll == DLL(sorted(orig))
        assert dll.get_size() == 7
        assert dll.get_head().get_value() == 0
        assert dll.get_tail().get_value() == 1
        # #
        orig = [-1,4,5,-2,0]
        dll = DLL(orig)
        quick_sort(dll, dll.head, dll.tail, dll.size, 0)
        # print(dll)
        # print(dll.c)
        # print(dll)
        assert dll == DLL(sorted(orig))
        # assert dll.c == 0
        #
        # orig = [3,2,1]
        # dll = DLL(orig)
        # quick_sort(dll, dll.head, dll.tail, dll.size, 0)
        # print(dll)
        # # print(dll.c)
        # assert dll == DLL(sorted(orig))
        # assert dll.c == 0


    #
    # def test_insertion(self):
    #     dll = DLL([])
    #
    #     assert dll.get_size() == 0
    #     assert dll.get_head() is None
    #     assert dll.get_tail() is None
    #
    #     # normal
    #     orig = [6, 1, 4, 7, 3, 5, 10, 8, 9, 2]
    #     dll = DLL(orig)
    #     insertion_sort(dll, dll.get_head(), dll.get_tail())
    #     assert dll == DLL(sorted(orig))
    #
    #     # size 1
    #     orig = [6]
    #     dll = DLL(orig)
    #     insertion_sort(dll, dll.get_head(), dll.get_tail())
    #     assert dll == DLL(sorted(orig))
    #
    #     # acending
    #     orig = [6,5,4,3,2,1]
    #     dll = DLL(orig)
    #     insertion_sort(dll, dll.get_head(), dll.get_tail())
    #     assert dll == DLL(sorted(orig))
    #
    #     # scattered
    #     orig = [1,8,2,7,3,6,4,6]
    #     dll = DLL(orig)
    #     insertion_sort(dll, dll.get_head(), dll.get_tail())
    #     assert dll == DLL(sorted(orig))
    #
    #     # size 2
    #     orig = []
    #     dll = DLL(orig)
    #     insertion_sort(dll, dll.get_head(), dll.get_tail())
    #     assert dll == DLL([])
    #
    # def test_quick_sort(self):
    #     orig = [9, 2, 7, 1, 3, 6, 4, 5]
    #     dll = DLL(orig)
    #     quick_sort(dll, dll.head, dll.tail, dll.size, 0)
    #     assert dll == DLL(sorted(orig))
    #     assert dll.c == 0
    #
    #     orig = [-636, -676, 387, -203, 673, -844, 883, -711, -814, -774, -491, 40, 633, 425, -168, 711, -173, -375, 286,
    #             142, 383, -891, -240, 203, -262, -247, -525, 550, 62, 343, 740, 711, -152, -756, -105, -289, -406, -471,
    #             798, -688, 851, 730, -989, -357, -297, -785, 777, -39, -148, -74, 603, -282, -44, 506, 345, 226, 866,
    #             597, 960, 224, 891, 197, -793, 641, 978, -462, -86, -689, -342, 858, -500, 458, -885, 718, 831, -426,
    #             319, 459, 653, -710, 854, 812, -666, 464, -326, 573, 153, -529, -782, 736, -296, -841, 817, 62, 289,
    #             -777, -698, 829, -34, -16, 948, 344, 449, -937, 143, 607, 134, 27, 718, -921, -317, 973, 6, -703, -838,
    #             718, 905, -372, 630, -858, -329, -446, 429, 760, 236, -487, -593, 274, -397, -228, 269, 842, 840, -597,
    #             1000, -857, 919, 139, -78, -339, 701, -410, -508, 603, -214, 208, 661, -733, 313, -326, 888, 994, 996,
    #             -798, -597, 18, 260, 853, -850, -713, -842, 541, 346, -79, 782, 658, -174, -670, -593, 909, -725, -192,
    #             -507, 995, -68, 216, 851, -454, 550, -74, 37, 441, -227, 227, 624, 606, -550, -341, 589, -702, -64, -30,
    #             -56, 724, 590, -665, 928, -538, -932, 237, 75, -489, 931, -937, -261, -260, -129, 177, 244, 126, -481,
    #             -962, 588, -457, -116, 364, -856, 665, -299, -59, -698, -105, -157, -603, -398, -529, 727, 874, 440,
    #             -311, -697, 388, 300, -195, 551, -225, -485, -702, 77, 82, 620, -595, -122, 132, -962, 176, -949, 218,
    #             -785, -13, -302, -74, -560, -113, -411, -152, 288, -659, -257, -276, -552, -821, -435, -278, 579, 978,
    #             934, -33, -987, 147, 474, 451, 132, -450, -22, -347, 591, -671, -361, -83, 5, 890, 946, -669, -910, -69,
    #             -850, 29, 118, -28, -700, -123, 958, 159, -845, 59, -67, -48, -705, -991, -231, 171, 865, -430, -642,
    #             938, -309, -490, 812, 976, -882, 965, -267, -115, 776, -892, -997, -283, -848, -383, 472, 719, -856,
    #             -521, -279, 12, 99, -431, 604, 247, -366, 785, 346, 90, 762, -737, 500, 650, 548, -206, 778, 493, 235,
    #             -723, 475, -569, -338, -146, -477, 512, -915, -536, 975, 59, 583, 852, -292, -825, -475, -164, -384,
    #             482, 385, -823, 394, -913, -313, 233, 623, 185, 976, 19, -303, 440, -500, 265, -317, -416, 126, -191,
    #             592, 12, 626, -244, -78, -488, -413, 259, 817, 199, -739, -3, -365, -120, -21, 782, 461, -128, -368,
    #             739, -425, 396, 616, 446, -120, -997, 774, 515, -810, 541, 180, -786, -977, -425, 904, -853, 372, -496,
    #             -688, -58, 46, -624, -677, 455, -409, 224, 631, -79, 873, 120, 895, 351, 686, -647, -579, 112, 72, -505,
    #             7, -437, -54, -951, -199, -866, 865, -298, 320, -36, 443, -811, 916, -391, 474, 122, -474, -993, 201,
    #             -385, 841, 976, 679, 23, -277, -92, -351, 522, 270, -502, -974, 466, -329, -414, 837, 268, 248, 184,
    #             129, -643, 727, 912, -260, 207, -294, 414, -210, -660, -551, 908, 876, -181, -502, -707, -730, 923, 152,
    #             -364, -749, -859, -169, -821, -786, -228, -993, -717, -686, 626, 922, 780, -967, 155, -898, -342, -88,
    #             674, 429, -873, 10, -190, -404, 144, 958, 119, -74, -348, -420, -373, -41, -224, -142, 682, 420, -681,
    #             -242, -125, -959, 575, -303, -779, 100, -442, 625, -69, 438, 889, 383, 551, 117, -137, 556, 848, -865,
    #             100, -598, -355, 684, -957, 174, -157, -195, -253, 383, -1, -453, -521, 336, 704, -25, 929, 566, -83,
    #             846, 560, 189, -830, 294, 84, 598, 790, 837, 559, -81, -964, -511, 817, 638, 914, -279, 236, 747, 42,
    #             -18, 927, 924, 694, -187, -504, 444, 229, 716, -858, 988, -94, 907, -747, -232, 938, -674, -119, -369,
    #             118, 652, -136, 801, -995, 531, 615, 444, -27, 315, 431, 941, 210, 110, -245, -244, -395, 291, -722,
    #             752, -762, 415, -771, -777, 479, 720, 581, -673, -918, -254, -586, 355, -230, -340, -216, 50, -345, -50,
    #             458, 142, -335, -413, 539, 702, 866, -9, 569, -589, 194, 785, -409, 59, -320, 138, 309, -277, 632, -530,
    #             -368, 811, -742, -658, -138, 568, 25, -369, -436, -508, -255, 520, -514, -797, 814, -5, 860, -15, -590,
    #             819, -854, 732, -167, -425, -205, -564, -320, -395, -389, -743, -816, -751, 885, 812, -377, -872, -736,
    #             -461, -845, 446, 776, -324, 932, 588, 123, 340, -590, 421, -819, -52, -603, 391, -868, 98, 680, 172, 12,
    #             -49, 298, -936, -638, 441, 587, 719, -118, 131, 707, -37, 200, -450, -626, -397, 849, -474, -607, 885,
    #             502, -215, 91, -774, 514, 928, -527, -53, 993, -326, 957, 238, 657, -164, -911, 535, 554, -224, 522,
    #             -490, -638, -231, 637, -436, 785, -125, -680, 224, -918, -672, 373, -371, -125, -206, -899, 805, 271,
    #             -395, 123, -93, -38, -770, 666, 551, 651, -584, -388, 180, -242, -691, 970, 160, 622, 473, 740, 202,
    #             -664, 925, 567, 294, 280, -759, 207, 110, -478, -314, -495, 485, -265, 142, -865, -909, 329, 121, 666,
    #             -163, 783, -156, 186, 107, 502, 950, -827, -737, -822, 823, 2, 910, 618, -836, -716, 726, 362, 573,
    #             -476, -516, 714, -417, 343, 198, 515, 842, 657, -77, -719, 49, 971, 328, -750, -316, 740, -857, -768,
    #             -147, 419, 322, -678, -67, -535, -492, -599, 305, 182, -674, -147, 109, 123, 817, -294, -420, -904,
    #             -132, 43, 855, 825, 666, 93, 961, 295, -354, -10, 860, -292, 881, -787, 128, 831, 364, 382, -222, 394,
    #             724, -221, -869, 637, 571, -352, -789, -756, 191, 143, 464, -236, 669, 379, -42, -653, -856, 64, -89,
    #             -636, -473, -147, -712, 758, -597, 692, -520, 677, 410, 560, -516, 304, 961, 547, 189, 929, -995, -894,
    #             -46, -316, 189, -343, -146, -802, 677, 566, 966, -736, -194, -50, 435, -37, 581, -654, -982, 423, -587,
    #             975, -652, 547, -545, -89, -226, 309, -982, -370, 612, 518, -805, 904, 927, -382, 467, 3, -100, -624,
    #             614, 885, -379, -893, -166, -665, -590, -584, -868, -334, 122, -730, -286, -873, -983, -329, 630, -417,
    #             609, 451, -488, 778, 39, 648, -367, -949, -96, -1000, -157, 949]
    #     # dll = DLL(orig)
    #     # quick_sort(dll, dll.head, dll.tail, dll.size, 4)
    #     # print(dll)
    #     # print(dll.c)
    #     # assert dll == DLL(sorted(orig))
    #
    # def test_guick_insertion(self):
    #     # checking c value
    #     # orig = [20, 18, 4, 2, 5, 7, 13, 10, 11, 3, 1, 17, 16, 9, 6, 8, 15, 12, 14, 19]
    #     # dll = DLL(orig)
    #     # quick_sort(dll, dll.head, dll.tail, dll.size, 15)
    #     # assert dll == DLL(sorted(orig))
    #     # assert dll.c == 2
    #
    #     # c value check
    #     orig = [1,1,1,1,1,1,1,0]
    #     dll = DLL(orig)
    #     quick_sort(dll, dll.head, dll.tail, dll.size, 2)
    #     print(dll.c)
    #     assert dll == DLL(sorted(orig))
    #     # assert dll.c == 7
    #
    # def test_application(self):
    #     # simple test
    #     dll = DLL([2,1,1])
    #     dll.count_unique()
    #     assert dll == DLL([2,1,2])
    #
    #     #mimir test
    #     dll = DLL([1,3,3,4,4,4])
    #     dll.count_unique()
    #     assert dll == DLL([1,3,2,4,3])
    #     assert dll.get_head().get_value() == 1
    #     assert dll.get_tail().get_value() == 3
    #     assert dll.get_size() == 5
    #
    #     # two items that are the same
    #     dll = DLL([4,4])
    #     dll.count_unique()
    #     assert dll == DLL([4,2])
    #     assert dll.get_head().get_value() == 4
    #     assert dll.get_tail().get_value() == 2
    #     assert dll.get_size() == 2
    #
    #     # 3 items that are the same
    #     dll = DLL([1,1,1,1,1,1,1,1])
    #     dll.count_unique()
    #     assert dll == DLL([1,8])
    #     assert dll.get_head().get_value() == 1
    #     assert dll.get_tail().get_value() == 8
    #     assert dll.get_size() == 2
    #
    #     # 3 items that are the same
    #     dll = DLL([])
    #     dll.count_unique()
    #     assert dll == DLL([])
    #     # assert dll.get_head().get_value() == 1
    #     # assert dll.get_tail().get_value() == 3
    #     # assert dll.get_size() == 2
    #
    #     # 2 numbers that are duplicated a lot
    #     dll = DLL([0,0,0,0,0,0,1,1,1,1,1])
    #     dll.count_unique()
    #     # print(dll)
    #     assert dll == DLL([0,6,1,5])
    #     assert dll.get_head().get_value() == 0
    #     assert dll.get_tail().get_value() == 5
    #     assert dll.get_size() == 4
    #
    #     # regular test
    #     dll = DLL([0,1,1,2,3,3,3,3,4,5,5,6])
    #     dll.count_unique()
    #     # print(dll)
    #     assert dll == DLL([0,1,2,2,3,4,4,5,2,6])
    #     assert dll.get_head().get_value() == 0
    #     assert dll.get_tail().get_value() == 6
    #     assert dll.get_size() == 10
    #
    #     # 100 1's
    #     dll = DLL([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    #     dll.count_unique()
    #     # print(dll)
    #     assert dll == DLL([1,1,0,0])
    #     assert dll.get_head().get_value() == 1
    #     assert dll.get_tail().get_value() == 0
    #     assert dll.get_size() == 4
    #
    #     # triple digit
    #     dll = DLL([1,1,1,1,1,1,1,1,1,1,1,1,2,2,2])
    #     dll.count_unique()
    #     # print(dll)
    #     assert dll == DLL([1,1,2,2,3])
    #     assert dll.get_head().get_value() == 1
    #     assert dll.get_tail().get_value() == 3
    #     assert dll.get_size() == 5
    #
    #     # # 20 1's
    #     # dll = DLL([4,3,2,1])
    #     # dll.count_unique()
    #     # print(dll)
    #     # assert dll == DLL([1,2,3,4])
    #     # assert dll.get_head().get_value() == 1
    #     # assert dll.get_tail().get_value() == 4
    #     # assert dll.get_size() == 3
    #

    #
    # def test_partition(self):
        # 1 ele check
        # dll = DLL([9,2,7,1,3,6,4,5])
        # test = partition(dll.get_head(), dll.get_tail())
        # print(dll)
        # print(test)

        # 2 ele unsorted check
        # dll = DLL([1,2,4,5,6,7,3])
        # test = partition(dll.get_head(), dll.get_tail())
        # print(dll)
        # print(test)
    #
    #     # decending list of 4 check
    #     dll = DLL([4,3,2,1])
    #     test = partition(dll.get_head(), dll.get_tail())
    #     print(dll)
    #     print(test)
    # # #
    # # #     # random unordered list of 4
    #     dll = DLL([1,2,3])
    #     test = partition(dll.get_head(), dll.get_tail())
    #     print(dll)
    #     print(test)
    #     # duplicate list
    #     dll = DLL([1,1,1,1,0,1,1])
    #     test = partition(dll.get_head(), dll.get_tail())
    #     print(dll)
    #     print(test)
    #     #s
    #     dll = DLL([3,4,5,6])
    #     test = partition(dll.get_head().get_next(), dll.get_tail())
    #     print(dll)
    #     print(test)
        # dll = DLL([2,1])
>>>>>>> f39e3b14ac55bc1f92fc152e7e5a0672b52e0cc7
    #     # quick_sort(dll, dll.get_head(), dll.get_tail(), dll.get_size(), 2)
    #     # insertion_sort(dll, dll.get_head(), dll.get_tail())


if __name__ == "__main__":
    unittest.main()

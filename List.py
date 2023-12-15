# List Structures #
list1 = [1, 2, 3, 4, 5, 6]

list2 = ["x", "y", "z"]

list3 = [12, 13, 14, "p", "q", "r", [101, 102, "a", "b", "c"]]

# I will use index method #

m = list3[0]  # m = 12

n = list3[2]  # n = 14


print(m*n)

print(list1[-1])  # 6

print(list2[:2])  # ['x', 'y']

print(list2[1:])  # ['y', 'z']


o = list3[6]  # o = [101, 102, "a", "b", "c"]

p = list3[6][2]  # p = 'a'

# I will change some values #

list2[1] = 9999  # list2 = ['x', 9999, 'z']

list1[0:4] = list2  # list1 = ['x', 9999, 'z', 5, 6]

# Some List Methods #

len(list1)  # 5

list1.append(77)  # list1 = ['x', 9999, 'z', 5, 6, 77]

list1.pop(1)  # list1 = ['x', 'z', 5, 6, 77]

list1.insert(1,"y")  # list1 = ['x', 'y', 'z', 5, 6, 77]










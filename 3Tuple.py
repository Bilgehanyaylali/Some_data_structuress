# Tuple Structures #

tuple1 = (1, 2, 3, "a", "b", "c")

tuple2 = ("x","y","z",[1, 2, 3])

# I use index method #

m = tuple1[0]  # m=1

n = tuple2[3][1]  # n=2

print(m**n)  # 1

tuple1[:5]  # (1, 2, 3, 'a', 'b')

tuple2[1:]  # ('y', 'z', [1, 2, 3])

# I change some values #

tuple1[0] =99  # TypeError: 'tuple' object does not support item assignment

# Some tuple methods #

tuple1.count("a")  # 1

tuple2.count("a")  # 0

tuple1.index(3)  # 2

tuple1.index("a") # 3



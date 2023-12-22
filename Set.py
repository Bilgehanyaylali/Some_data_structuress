# Set Structures #
set1 = set([1, 2, 3, 4, 5, 6])

set2 = set(["x", "y", "z", 1, 2])

set3 = {99,100,101}

# Differences of sets #

set1.difference(set2)  # {3, 4, 5, 6}

set2.difference(set1)  # {'z', 'x', 'y'}

# Intersection of sets #

set1.intersection(set2)  # {1, 2}

set2.intersection(set3)  # set()

#  Symmetric differences  sets #

set1.symmetric_difference(set2)  # {3, 4, 5, 6, 'z', 'x', 'y'}

# Union of sets #

set1.union(set2)  # {1, 2, 3, 4, 5, 6, 'z', 'x', 'y'}

set1.union(set3)  # {1, 2, 3, 4, 5, 6, 99, 100, 101}

# Returns whether two sets have a intersection or not #

set1.isdisjoint(set2)  # False

set1.isdisjoint(set3)  # True

# Returns whether another set contains this set or not #

set1.issubset(set2)  # False

# Returns whether this set contains another set or not #

set1.issuperset(set3)  # False

# I try to access Items in set #

for i in set2:
    print(i)   # 1
               # 2
               # z
               # x
               # y

# I add item into set #

set1.add(11)  # set1 = {1, 2, 3, 4, 5, 6, 11}

# I add set into other set #

set3.update(set2)  # set3 = {1, 2, 99, 100, 101, 'z', 'x', 'y'}





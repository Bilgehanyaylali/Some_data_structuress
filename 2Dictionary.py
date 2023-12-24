# Dictionary Structures #
dictionary1 = {"a": 1,
               "b": 2,
               "c": 3}

dictionary2 = {"a": [1, "x"],
               "b": [2, "y"],
               "c": [3, "z"]}

# I find relation between key and value #
dictionary1["a"]  # 1

dictionary2["b"]  # [2, "y"]

dictionary2["c"][1]  # 'z'

dictionary2.get("c")   # [3, "z"]

# Key inquiry #

"a" in dictionary1  # True

"d" in dictionary1  # False

# I change some values #

dictionary1["a"]= 99  # {'a': 99, 'b': 2, 'c': 3}

dictionary2["c"]= 111  # {'a': [1, 'x'], 'b': [2, 'y'], 'c': 111}

# I find all keys #

dictionary1.keys()  # dict_keys(['a', 'b', 'c'])

# I find all values #

dictionary1.values()  # dict_values([99, 2, 3])

# I find keys and values together#

dictionary1.items()  # dict_items([('a', 99), ('b', 2), ('c', 3)])

# I update key and value #

dictionary1.update({"a": 1})  # {'a': 1, 'b': 2, 'c': 3}

dictionary2.update({"c": [3,"z"], "d": [4, "t"] })  # {'a': [1, 'x'], 'b': [2, 'y'], 'c': [3, 'z'], 'd': [4, 't']}



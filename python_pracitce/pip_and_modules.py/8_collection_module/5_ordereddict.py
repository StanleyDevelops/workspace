# Ordereddict
from collections import OrderedDict
d = OrderedDict()

d["a"] = 1
d["b"] = 2

print(d)

# ChainMap - Treat multiple dictionaries as one.
from collections import ChainMap
d1 = {"a":1}
d2 = {"b":2}
c = ChainMap(d1,d2)
print(c["a"])
print(c["b"])


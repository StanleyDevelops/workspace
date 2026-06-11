from calculator import add 
from calculator import multiply as mul
from calculator import subtract,divide

print(add(4,5))
print(mul(8,9))
print(subtract(6,8))
print(divide(2,9))



# Trying to import from a user defined package
from utils import even
from utils import rev_string

print(rev_string("LOVE"))
print(even(9))
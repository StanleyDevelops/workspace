# method I

set_1 = {12,3,2,54,24}
result_1 = ", ".join(map(str, set_1))
print(result_1)
print(type(result_1))

# json.dump method
import json
set_2  = {1,2,3,4,5}
result_2 = json.dumps(list(set_2))
print(result_2)
print(type(result_2))
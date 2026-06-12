#uuid

import uuid

id = uuid.uuid4()

print(id)

#functools
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print(result)
# Collections Module
from collections import Counter
mylist = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3]
print(Counter(mylist))
print(Counter('asdfasdfasasfasdfa'))

from collections import defaultdict
d = defaultdict(lambda: 0)
d['correct key'] = 100
# WRONG KEY is matched with default value
print(d['correct key'], d['WRONG KEY'])

from collections import namedtuple
Pet = namedtuple('Pet', ['name', 'age', 'type'])
tombik = Pet(name='Tombik', age=12, type='bird')
print(tombik)
print(tombik.age, tombik[1]) # diff ways getting age
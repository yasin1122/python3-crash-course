"""
Numbers: Store Integers and Float values.
Strings: Stores a string of characters.
Lists: [] list of different or same data types.
Tuples: () Same as lists but immutable.
Dictionaries: Key value pairs.

10*10+0.25

44, 29, 34
float
num ** 0.5
num ** 2
"""

s = 'hello'
print(s[1])
print(s[::-1])
print(s[-1], s[4])

list1 = []
list1.append(0)
list1.append(0)
list1.append(0)
list2 = list([0, 0, 0])
print(list1, list2)

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
list4 = [5,3,4,6,1]
list4.sort()
print(list3, list4)

d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

"""
Tuples are immutable lists and use () instead of [].
Sets only contain unique (one of each) value and use {}.
"""

list5 = [1,2,2,33,4,4,11,22,3,3,2]
mySet = set(list5)
print(mySet)

"""
2 > 3 is False
3 <= 2 is False
3 == 2.0 is False
3.0 == 3 is True
4**0.5 != 2 False

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']
3 >= 4 is False
"""


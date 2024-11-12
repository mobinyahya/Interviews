import sys
import pandas as pd
from collections import defaultdict
import collections

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Nairobi", "Accra")


class Person(object):
    x = 1
    y = 1
    pointer = None
    def __init__(self, x, y = 0):
        self.pointer = None
        self.x = x
        self.y = y

    def distance(self):
        """Find distance from origin"""
        return (self.x**2 + self.y**2) ** 0.5
    
class student(Person):
    grade = 0
    def __init__(self, grade, x, y = 0):
        self.grade = grade
        # inheriting the properties of parent class
        super().__init__(x, y)
    def distance(self):
        return (self.x + self.y)


person_list = [Person(0,1), Person(0,3), Person(2,4), Person(1,7)]
list_of_lists = [[0,1], [0,3], [2, 4], [1, 7]]

# Sort *in place* based on first elements (ascending order)
person_list.sort(key=lambda person: person.x)
list_of_lists.sort(key=lambda sublist: sublist[0])

list_of_tuples = [(1, 3), (2, 2), (3, 1)]
sorted_list = sorted(list_of_tuples, key=lambda x: x[0])
numbers = [2,5,2,9]
sorted_list = sorted(numbers)

dict = {"a": 10, "b":2}
sorted_keys = sorted(dict, key=lambda x: dict[x]) # returns ["b", "a"] -- Add reverse=True if you want descending order


# for loop printing 10,9,...,0
for i in range(10, -1, -1):
    print(i)
# for loop printing 0,1,2,..,9
for i in range(0, 10):
    print(i)

sample_string = "[welcome test]"
sample_string.find("%") # is -1 if non found
sample_string.split("[", 1)
string = sample_string[0:3]


stack = queue = []
queue.append("1")
stack.append("1")
stack.insert(0, "-1")  # Insert "-1" at index 0
queue_top = queue.pop(0)
stack_top = stack.pop()

#for each key that is not in the dict, assume it's there and value of the key is an empty list
edges = defaultdict(list)

# Deque:
d = collections.deque([1, 2, 3]) #.pop(), .popleft(), .append(), .appendleft()


dp = [[0] * 500 for _ in range(200)] # initilize 200 * 500 zero matrix
visited_list = [False] * 10 # append(), .insert(index, element), .pop(index)

visited_set = set()  #.add, .intersection, .union, .difference
# or
visited_set1 = {"a", "b", "c"}
# merge one two sets
visited_set.update(visited_set1)
# add elements to a set
visited_set.add("d")
visited_set.remove("a")


infty_var = float('inf') # initilie a variable as positive infty
result = 11 // 2 # equals 5

import heapq
heap = []
heapq.heapify(heap)
heapq.heappush(heap, 5)
heapq.heappush(heap, 6)
smallest = heapq.heappop(heap)
frequency_tuple1 = (10, "Apples")
heapq.heappush(heap, frequency_tuple1) # Adding tuples -- sorts based on tuple first element 
smallest = heapq.heappop(heap)


# Create iterators
iterator = iter(person_list)
print(next(iterator))

###########################################################  read input
import csv
input = sys.stdin.readline().split()


data = sys.stdin.readlines()
df_list = []
for line in csv.reader(data):
    df_list.append(line)
df = pd.DataFrame(columns = df_list[0], data = df_list[1:]).astype(float)


try:
    result = 10/0
except Exception as e:
    print(e)

# Or
raise ValueError("Invalid. Division by zero")






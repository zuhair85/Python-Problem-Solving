# Create a custom iterator class called ReverseIterator that takes a sequence (such as a list, tuple, or string) and allows you to iterate over its elements in reverse order.
#
# You must implement Python's iterator protocol using __iter__() and __next__().
# Requirements
# Your ReverseIterator class must:
# 1. Accept a sequence when creating an iterator.
# 2. Iterate over the sequence from the last element to the first.
# 3. Implement __iter__() to return the iterator object itself.
# 4. Implement __next__() to return the next element in reverse order.
# 5. Raise StopIteration when there are no more elements.
# Expected behavior

# Example 1: List

# numbers = [10, 20, 30, 40, 50]
# reverse_numbers = ReverseIterator(numbers)
# for number in reverse_numbers:
#   print(number)
#
# Output:
# 50
# 40
# 30
# 20
# 10

class ReverseIterator:
    def __init__(self, items):
        self.items = items
        self.size = len(items)

    def __iter__(self):
        return self

    def __next__(self):
        if self.size <= 0:
            raise StopIteration
        else:
            val = self.items[self.size - 1]
            self.size -= 1
            return val

numbers = [10, 20, 30, 40, 50]

reverse_numbers = ReverseIterator(numbers)

for number in reverse_numbers:
    print(number)
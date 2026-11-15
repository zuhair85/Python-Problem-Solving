# Iterator = An object that returns elements one at a time
#            from a sequence (or data stream)
#            and remembers its position between calls
#            A python object is an iterator if it has:
#            __iter__() --> Returns the iterator object itself
#            __next__() --> Returns the next item in the sequence
#                           (raises StopIteration when no more items)

import random

class Dice:
    def __init__(self, rolls):
        self.rolls = rolls
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.rolls:
            self.count += 1
            return random.randint(1, 6)
        else:
            raise StopIteration
# Program: 1
# dice = Dice(3)
# for die in dice:
#     print(die)

# Program: 2 (same as program 1 but uses list comprehension)
# dice = [die for die in Dice(3)]
# print(dice)


#What's basically happening in program 1 & 2

dice = Dice(3)

iterator = iter(dice)   #same as: iterator = dice.__iter__()

while True:
    try:
        roll = next(iterator)   #same as: iterator.__next__()
        print(roll)
    except StopIteration:
        break
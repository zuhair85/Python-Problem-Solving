# Create a custom context manager called Timer that measures how long a block of code takes to execute.
#
# Your context manager must use Python's context management protocol: __enter__() and __exit__().
# Requirements
# Your Timer class must:
# 1. Implement __enter__() to record the starting time.
# 2. Implement __exit__() to record the ending time.
# 3. Calculate the elapsed execution time.
# 4. Display the elapsed time after the with block finishes.
# 5. Work with any ordinary block of Python code.

import time

class Timer:
    def __init__(self):
        self.start = None
        self.end = None
        self.time_elapsed = None

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.time_elapsed = self.end - self.start
        print(f'Execution time: {self.time_elapsed}')

with Timer():
    total = 0
    for i in range(1_000_000):
        total += i
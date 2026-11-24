import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")



# import random
# import time
#
# OPERATORS = ['+', '-', '*']
# MIN_OPERAND = 3
# MAX_OPERAND = 13
# TOTAL_PROBLEMS = 10
# wrong = 0
# correct = 0
#
# def problem_generator(wrong, correct):
#     left = random.randint(MIN_OPERAND, MAX_OPERAND)
#     right = random.randint(MIN_OPERAND, MAX_OPERAND)
#     operator = random.choice(OPERATORS)
#     expr = str(left) + " " + operator + " " + str(right)
#     answer = eval(expr)
#     while True:
#         guess = input(f"{expr} = ")
#         if guess == str(answer):
#             correct += 1
#             break
#         else:
#             wrong += 1
#             break
#
#     return wrong, correct
#
# input('Press ENTER to start!')
# print('---------------------')
#
# start_time = time.time()
# for i in range(TOTAL_PROBLEMS):
#     wrong, correct = problem_generator(wrong, correct)
# end_time = time.time()
# time_taken = end_time - start_time
#
# print(f'Correct: {correct}')
# print(f'Wrong: {wrong}')
# print(f'Your attempt took {time_taken} seconds')

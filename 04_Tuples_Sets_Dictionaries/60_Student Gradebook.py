# Task: Build a student gradebook using nested dictionaries. Store students and their scores, calculate each student's average, and identify the student with the highest average.

def add_student(gradebook, name, scores):
    # Add a student and their subject scores
    gradebook[name] = scores
    return gradebook

def calculate_average(gradebook, name):
    # Calculate and return the student's average
    if len(gradebook) == 0:
        return

    total_score = 0
    subject_count = 0
    for subject in gradebook[name]:
        total_score = total_score + gradebook[name][subject]
        subject_count += 1

    avg_score = total_score / subject_count
    return avg_score

def calculate_all_averages(gradebook):
    # Return a dictionary containing each student's average
    if len(gradebook) == 0:
        return

    avg_dct = {}
    for n in gradebook:
        avg_dct[n] = calculate_average(gradebook, n)

    return avg_dct

def find_top_student(gradebook):
    # Return the student with the highest average
    if len(gradebook) == 0:
        return

    avg_dct = calculate_all_averages(gradebook)
    highest_avg = max(avg_dct.values())
    top_student_list = []
    for key,value in avg_dct.items():
        if value == highest_avg:
            top_student_list.append(key)

    return top_student_list

# gradebook = {
#     "Alice": {
#         "Math": 90,
#         "Science": 85,
#         "English": 95
#     },
#     "Bob": {
#         "Math": 80,
#         "Science": 90,
#         "English": 85
#     },
#     "Charlie": {
#         "Math": 95,
#         "Science": 92,
#         "English": 88
#     }
# }

gradebook = {
    "Alice": {"Math": 90, "Science": 80},
    "Bob": {"Math": 85, "Science": 85},
    "Charlie": {"Math": 95, "Science": 75}
}

add_student(gradebook, "David", {
    "Math": 88,
    "Science": 92,
    "English": 90
})

#print(gradebook)
# print(calculate_average(gradebook, "Charlie"))
# print(calculate_all_averages(gradebook))
print(find_top_student(gradebook))
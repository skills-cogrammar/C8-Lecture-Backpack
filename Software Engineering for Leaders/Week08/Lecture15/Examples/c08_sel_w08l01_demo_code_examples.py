def sum_list(num_list):
    # Initialise the total to zero
    total = 0
    # Iterate over each number in the list
    for num in num_list:
        # If the current item is not a number, return None
        if not isinstance(num, (int, float)):
            return None
        # Add the number to the total
        total += num
    # Return the final sum of the list
    return total


def get_middle_of_list(lst):
    # Check if the list is not empty
    if lst:
        # Calculate the middle index
        mid_index = len(lst) // 2
        # Return the middle element of the list
        return lst[mid_index]
    # Return None if the list is empty
    return None


def get_average(grades):
    # Calculate the average by dividing the total by the number of grades
    return sum(grades) / len(grades)


def get_all_students_average(student_grades):
    # Check if the list of student grades is not empty
    if student_grades:
        # Initialise the overall grade average to zero
        grade_average = 0
        # Iterate over each student's grades
        for grades in student_grades:
            # Add the average of each student's grades to the overall average
            grade_average += get_average(grades)
        # Calculate the final average, rounding to two decimal places
        grade_average = round(grade_average / len(student_grades), 2)
        # Return the calculated average
        return grade_average
    # Return zero if there are no student grades
    return 0


def recursive_word_flip(word):
    # If the word has one or no characters, return it as it is
    if len(word) <= 1:
        return word
    else:
        # Recursively flip the remainder of the word and add the first character at the end
        return recursive_word_flip(word[1:]) + word

""" Refactoring code: return recursive_word_flip(word[1:]) + word[0]"""
# Make sure you save your code before running unittest again

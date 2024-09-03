# Example 1: Simple if statement
age = 16
if age > 18:
    print("You are eligible to vote")
# This will not print anything because the condition is false

# Example 2: if-else statement
age = 16
if age > 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
# This will print "You are not eligible to vote"

# Example 3: Same as Example 2 (redundant in this case)
age = 16
if age > 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
# This will also print "You are not eligible to vote"

# Example 4: More complex conditions with and/or operators
legal_age_to_vote = 18
nationality_to_vote = "local"
henry_nationality = "local"
henry_age = 20

# Check if Henry meets both age and nationality requirements
if (henry_age >= legal_age_to_vote) and (henry_nationality == nationality_to_vote):
    print("Henry is eligible to vote")
# If Henry doesn't meet either the age or nationality requirement
elif (henry_age < legal_age_to_vote) or (henry_nationality != nationality_to_vote):
    print("Henry is not eligible to vote")
# This will print "Henry is eligible to vote"
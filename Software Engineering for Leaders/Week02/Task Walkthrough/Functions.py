'''
Our task is to calculate the wages of employees based on the type of event 
they worked at and the number of hours worked. Employees can be hired to 
work at a wedding, conference, or gala, with hourly wages of $18, $15, and $20, 
respectively.

1. Get the following inputs:
   
    - event_type: The type of event the employee worked at.
    - hours_worked: The number of hours the employee worked.

2. Create the following functions:

    - hourly_wage(): This function takes event_type as an argument and returns 
      how much the employee earns per hour based on the type of event.
    - calculate_wage(): This function takes event_type and hours_worked as 
      arguments and returns the total amount the employee should be paid.

3. Print the results in an easy-to-read format: Display the event type, hours 
   worked, hourly wage and total amount to pay the employee.

'''

# Function to determine hourly wage for an employee based on where they worked
def hourly_wage(event):
    if event == "wedding":
        return 18
    elif event == "conference":
        return 15
    elif event == "gala":
        return 20 

# Function to calculate the total amount an employee will get paid  
def calculate_wage(event, hours):
    wage_per_hour = hourly_wage(event)
    total_wages = wage_per_hour * hours
    return total_wages

# Program to interact with user
event_type = input("Enter the event type (wedding/conference/gala): ").lower()
hours_worked = int(input("Enter the number of hours worked: "))

total_to_pay = calculate_wage(event_type, hours_worked)

print(f"Event Type: {event_type.capitalize()}")
print(f"Hours Worked: {hours_worked}")
print(f"Hourly Wage: ${hourly_wage(event_type)}")
print(f"Total to pay: ${total_to_pay}") 

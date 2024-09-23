'''
Just showing how we can use the split method
in another way to complete this task.
'''

with open('event_items.txt', 'r') as file:
    lines = file.readlines() 
    # print(lines) # just checking the contents of lines

# Initialise list for services
services = []

for line in lines:
    # for first iteration line = 'Sarah Baker: Catering\n'
    name, service = line.strip().split(':')

    # stripped = ['Sarah', 'Baker:', 'Catering']
    services.append(service.strip()) # get rid of leading white spaces

print(services)

'''
for item in services:
    print(item)
'''    



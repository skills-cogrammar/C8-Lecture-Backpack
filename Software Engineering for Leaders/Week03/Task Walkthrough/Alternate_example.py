'''
Create a program that reads a string and alternates 
between adding an @ symbol () after every other letter
for example, "hello" becomes "he@ll@o"
''' 

# h e l l o
# 0 1 2 3 4

# h e @ l l @ o

text = input("Enter a string: ")

new_text = ''

for i, char in enumerate(text): # returns characters in string with their index
    # modulo division 9 and 3 : 9 % 3 = 0, 5 % 4 = 1
    if i == 0:
        new_text = new_text + char 
        # new_text = 'h' after first iteration where i = 0
    elif i % 2 == 0:
        new_text = new_text + '@' + char  
    else:
        new_text = new_text + char  

print("Modified string: ", new_text)

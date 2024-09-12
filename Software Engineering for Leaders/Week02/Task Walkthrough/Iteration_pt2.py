'''
Write a python script that prints out this pattern  using a for loop:

@@@@@
 @@@@
  @@@
   @@
    @
'''

for i in range(5):
    print(" " * i + "@" * (5 - i))

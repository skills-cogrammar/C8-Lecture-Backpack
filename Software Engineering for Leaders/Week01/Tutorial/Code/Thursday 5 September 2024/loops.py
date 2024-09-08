# Sum of numbers in a fixed list
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum using for loop: {total}")



numbers = []
while True:
    num = input("Enter a number (or 'done' to finish): ")
    if num == 'done':
        break
    numbers.append(int(num))

total = 0
i = 0
while i < len(numbers):
    total += numbers[i]
    i += 1
print(f"Sum using while loop: {total}")
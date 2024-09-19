def divide(a, b):
    if b < 0:
        raise ValueError("Division by negative number")
    result = a / b
    return result

div_result = 0
while True:
    try:
        number_1 = int(input("Enter a:"))
        number_2 = int(input("Enter b:"))
        div_result = divide(number_1, number_2)
    except ZeroDivisionError as ez:
        print(f"You wanted to divide by 0. The error is: {ez}")
    except TypeError as et:
        print(f"You wanted to divide by a non int. The error is: {et}")
    finally:
        print(div_result)
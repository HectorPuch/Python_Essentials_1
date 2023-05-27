odd_numbers = 0
even_numbers = 0

number = int(input("Enter a number or enter 0 to stop the program: "))

while number != 0:
    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1
    number = int(input("Enter a number or enter 0 to stop the program: "))

print("Counting odd numbers: ", odd_numbers)
print("counting even numbers: ", even_numbers)

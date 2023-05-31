hat_list = [1, 2, 3, 4, 5]

# Step 1: changes the second item in the list to the number entered by the user.
hat_list[2] = int(input("Please enter a whole number: "))

# Step 2: removes the last item from the list.
del hat_list[-1]

# Step 3: prints the number of items stored in the list.
print(len(hat_list))

# Step 4: print the updated list.
print(hat_list)

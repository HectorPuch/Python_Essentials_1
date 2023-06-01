my_list = [6, 30, 12, 24, 61]
print("Original list:", my_list)

my_list[0], my_list[2] = my_list[2], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print("Updated list:", my_list)

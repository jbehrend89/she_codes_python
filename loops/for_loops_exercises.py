# Ask the user for a number. Use a for loop to print the times tables for that number.

multiply = input("Enter a number.")

for item in range(1, int(multiply) +1):
    product = item * int(multiply)

    print(f"{multiply} * {item} = {product}")

# Ask the user for a number. Use a for loop to sum from 0 to that number

addition = int(input("Enter a number."))

sum = 0
for i in range(addition + 1):
  sum = sum + i
  i = i + 1
print("Sum is ", sum)


# for item in range(int(addition)):
#     product = item + (addition)

#     print(f"{multiply} + {item} = {product}")

# Given a list, use a for loop to sum all the numbers in the list.




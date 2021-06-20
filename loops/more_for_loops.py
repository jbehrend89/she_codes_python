# def sum_list(l):
#     sum = 0
#     for x in l:
#         sum += x
#     return sum

# l = [1, 2, 3, 4, 5]
# sum_list(l)

# l = list(map(int, input("Enter numbers separated by spaces: ").split()))
# sum_list(l)


# n = input("Enter Number to calculate sum")
# n = int (n)
# sum = 0
# for num in range(0, n+1, 1):
#     sum = sum+num
# print("SUM of first ", n, "numbers is: ", sum )

lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))

# sum_list = []

# n = int(input("Enter numbers seperated by spaces "))
# sum_list.append(n)

# print(sum_list)

# print("Sum = ", sum(int(sum_list)))

# loops

for num in range(10):
    print(num)

print()

for num in range(1, 11):
    print(num)

print()

for num in range(0, 11, 2):
    print(num)

# use a for loop to print numbers 0 to 100 (inclusive)
for num in range(1, 101):
    print(num)

# use a for loop to print the numbers 0 - 100 in steps of 5
for num in range(0, 101, 5):
    print(num)

chilli_wishlist = [
    "igloo", 
    "chicken", 
    "donut toy",
    "cardboard box"
]

for item in chilli_wishlist:
    print(f"Chilli wants: {item}")

guess = ""
while guess != "a":
    guess = input("Guess a letter: ")

counter = 0
while counter <= 5:
    print(counter)
    counter = counter + 1
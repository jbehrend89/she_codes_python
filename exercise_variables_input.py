# addition exercise int
addition1 = input("Enter a number ")
addition2 = input("Enter another number ")

total_value = int(addition1) + int(addition2)
print(f"Adding those numbers together equals {total_value}")

# addition exercise float
addition3 = input("Lets do that again enter a number 1-9 ")
addition4 = input("Enter another number ")

total_value2 = float(addition3) + float(addition4)
print(f"Adding those numbers together equals {total_value2}")


# multiplication exercise
multiply1 = input ("Now choose a number between 1-9 ")
multiply2 = input ("And another number between 1-9 ")

multiply_value = int(multiply1) * int(multiply2)
print(f"Wow I have multiplied those numbers for you and they equal {multiply_value}")

# km to m
km_dist = input ("How many kilometers did you run today? ")
m_dist = float(km_dist) * 1000
print(f"Great work! That's {m_dist} meters. Congratulations!")

# name and height exercise
name = input("What is your name? ")
height = input("How tall are you in centimeters? ")
print(f"{name} is {height}cm tall.")
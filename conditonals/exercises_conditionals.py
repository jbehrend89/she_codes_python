# Time for Roary to catch moths
moths_in_house = False
if moths_in_house:
    print("Get the moths!")
else:
    print("No threats detected.")
print()

# Mitch is home and its time for Roary to catch moths
moths_in_house = False
mitch_is_home = True
if moths_in_house and mitch_is_home:
    print("Get the moths!")
elif not moths_in_house and not mitch_is_home:
    print("No threats detected.")
elif moths_in_house and not mitch_is_home:
    print("Meooooooooooooow! Hissssss!")
else:
    print("Climb on Mitch.")
print()

# Red light cameras
light_colour = "Red"
car_detected = True
if light_colour == "Red" and car_detected:
    print("Flash!")
else:
    print("Do nothing.")
print()

# Can you ride the rollercoaster?
height = input("What is your height in centimeters?")
if (int(height)) > 120:
    print("Hop on!")
else:
    print("Sorry, not today :(")
print()

# user name and password
username = input("Enter your username.")
password = input("Enter your password.")
if username == "fleur" and password == "password123":
    print("Correct!")
else:
    print("Incorrect!")

# valid email address
email_address = input("Enter your email address...")
if "@" in email_address and "." in email_address:
    print("Valid email address.")
else:
    print("Invalid email address.")
print()
def create_greeting(name):
    greeting = f"Hello, {name}!"
    return greeting


# print(create_greeting("Chilli"))

def convert_cm_to_in(length_cm):
    length_in_inches = length_cm / 2.54
    return round(length_in_inches, 2)

print(convert_cm_to_in(20))

# define a function to convert inches to cms

def convert_in_to_cm(length_in):
    length_in_cm = length_in * 2.54
    return round(length_in_cm, 2)

print(convert_in_to_cm(2))

def calculate_mean(a, b):
    total = a + b
    mean = total / 2
    return mean

print(calculate_mean(2, 4))
print(calculate_mean(3, 4))
print(calculate_mean(5, 10))

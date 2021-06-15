# Q1)Write a function that takes a temperature in fahrenheitand returns the temperature in celsius.

def convert_f_to_c(temp_in_f):
    temp_in_c = (temp_in_f - 32) * 5 / 9
    return round(temp_in_c, 2)

print(convert_f_to_c(350))

# Q2)Write a function that accepts one parameter (an integer) and returns True when that parameter is odd and False when that parameter is even.

def odd(x):
    return x % 2 == 1

print(odd(4))


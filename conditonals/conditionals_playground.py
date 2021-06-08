# boolean
# is_raining = True
# is_cold = True
# print(type(is_raining))
# print(type(is_cold))

# print(is_raining)
# print(not is_raining)
# print(is_raining and is_cold)
# print()

# #Comparison is_raining and is_cold
# print(is_raining) #True
# print(not is_raining) #False
# print(is_raining or is_cold) #True
# print(is_raining and not is_cold) #False
# print(is_raining or not is_cold) #True
# print(not is_raining and not is_cold) #False
# print()

# temp = 16
# print(temp < 18)
# print(temp > 18)

# wind_chill = 3
# print(wind_chill > 4)
# print(temp - wind_chill < 16)
# print()

# # voucher code
# code = "freeticket"
# print(code == "freeticket")
# print(code != "freeticket")

is_raining = True
if is_raining:
    print("Take an umbrella")
else:
    print("Do not take an umbrella")
print("cats")
print()

temp = 16
wind_chill = 4

if temp - wind_chill < 16:
    print("Take a jumper.")
elif temp - wind_chill > 30:
    print("Its hot. Stay home.")
else:
    print("Wow, what a lovely day!")
print()

if temp < 16:
    if is_raining:
        print("Just stay home.")
    else:
        print("It's ok today.")
else: 
    print()
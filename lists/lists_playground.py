# hello world

chilli_wishlist = [
    "igloo", 
    "chicken", 
    "donut toy",
    "cardboard box"
]
print(chilli_wishlist)
print(chilli_wishlist[0])
print(len(chilli_wishlist))

print(len(chilli_wishlist))
#print(chilli_wishlist[4])
print(chilli_wishlist[0])
print(chilli_wishlist[1])
print(chilli_wishlist[-1])
print(chilli_wishlist[0:2])
print(chilli_wishlist[1:3])
chilli_wishlist[1] = 'carrot'
print(chilli_wishlist)
print()

# print the sublist of items in positions 2 through to 3.
print(chilli_wishlist[1:3])
print()

# print the item in the -3 position. 
print(chilli_wishlist[-3])
print()

# add to the list
chilli_wishlist.append("dig mat")
print(chilli_wishlist)
chilli_wishlist.extend(["kong", "tennis ball", "crocodile toy"])
print(chilli_wishlist)
chilli_wishlist.insert(1, 'peanut butter')
print(chilli_wishlist)
print()

# remove items 
print(chilli_wishlist.pop())
print(chilli_wishlist)
print(chilli_wishlist.pop(2))
print(chilli_wishlist)

chilli_wishlist.remove("kong")
print(chilli_wishlist)
print()

# add a new item to position -2
chilli_wishlist.insert(-2, 'sqweeky toy')
print(chilli_wishlist)

# remove the third item from the list
print(chilli_wishlist.pop(2))
print(chilli_wishlist)

# add four new items to the end of the list.
chilli_wishlist.extend(["rubber ball", "lambie", "old shoe", "newspaper"])
print(chilli_wishlist)

# remove the "igloo" item from the list
chilli_wishlist.remove("igloo")
print(chilli_wishlist)
print()

chilli_wishlist = [
    ["igloo"], # bed
    ["donut toy", "tennis ball", "crocodile toy"], # toys
    ["chicken", "peanut butter"], # treats
    ["cardboard box", "kong", "dig mat"] # activity basedtoys]
]

print(chilli_wishlist)
print(chilli_wishlist[2])
print(chilli_wishlist[2][1])
print()

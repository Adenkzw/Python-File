# Transform the list into a list of numbers

items =[
    ("Product1", 10),
    ("Product2", 9),
    ("product3", 12),
]

#prices = []
#for item in items:
#   prices.append(item[1])
#print(prices)

#bottom function can make same result which is the map function by using lambda

prices = list(map(lambda item: item[1], items))
print(prices)
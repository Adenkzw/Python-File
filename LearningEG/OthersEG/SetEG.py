# They are not in sequence and have no duplicates so cannot access them using index
# Set helps to remove duplicates, only have unique items
# Converts list into a set

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second) # Union of both ( add them together into one, removes duplicates), from the duplicates only 1 of it remains out of the same number or letters (1, 1) or (A, A)
print(first & second) # Print only duplicates
print(first - second) # Only prints what first set have that second set don't have
print(first ^ second) # Removes duplicates and prints the rest/remaining
#1
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price #total = total + price
print(f"Total: {total}")

#2
friends = ['Aden', 'Wei En', 'Kwan']
for friend in friends:
    print(friend)

#3
for numbers in range(2, 10 , 3):
    print(numbers)

#Exponent Funtions uisng for loop - take a certain number and raise it to a specific power
# simple way is print(2**5)

base_num = int(input('Enter number: '))
pow_num = int(input('Enter power number: '))

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result *=base_num #result = result* base_num
    return result
print(raise_to_power(base_num, pow_num))

#4
def multiply(*numbers): #instead of (x, y, z, c), bascially a collection of information
    total = 1            # **numbers makes it into dictionary which is {} 
    for number in numbers:
        total *= number
    return total
print(multiply(2,3,4,5))
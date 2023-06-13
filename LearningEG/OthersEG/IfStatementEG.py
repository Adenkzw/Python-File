is_male = False
is_tall = False

if is_male and is_tall:
    print('You are male and tall')
elif is_male and not is_tall:
    print('You are male and not tall')
elif not is_male and is_tall:
    print("You are not male and is tall")
else:
    print('You are neither male nor tall')

# If statement and comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2>= num3:
        return num2
    else:
        return num3

print(max_num(20, 60, 50))

#Ternary Operator - make it neater
age = 12
message = 'Eligible' if age >= 18 else 'Not eligible'
print(message)

#is the same as
# if age >= 18:
#   message = 'Eligible'
#else:
#   message = 'Not  eligible'
#print(message)
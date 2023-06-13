# Passing information to functions
# def 'Smth" is making it into a function
#1
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome')
    
print('Start')
greet_user('John', 'Smith') #passing info to the func greet_user
greet_user('Marie', 'Gold')
print('Finish')

#2
def say_hi(name, age):
    print(f'Hello {name}, you are {age} years old')
say_hi('Wei En', 22)

#3
def greet(name, last):
    return(f'Hi {name} {last}') #Use return so that "None" will not appear

name = input('Enter name: ')
last = input('Enter last: ')

print(greet(name, last)) #User pass the information instead

#4
def greet(name, last):
    return f'Hi {name} {last}'

print(greet(name= input('Enter name: '), last=  input('Enter last: '))) #Easier to figure out which value is for which(Perform same as #3)
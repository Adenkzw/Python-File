# Handling errors in python programs, prevent program crash by using try & except
# Printing proper error messages
# So when print out wont have red word errors


try:
    age = int(input('Age: '))
    income = 2000
    risk = income/age
    print(risk)
except ZeroDivisionError: #anything /0 will come out this error
    print('Age cannot be 0.')
except ValueError:
    print('Invalid Value') #anything not number
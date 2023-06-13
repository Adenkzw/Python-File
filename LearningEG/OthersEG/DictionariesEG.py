# the words/numbers you give meaning to
# {} this kind of brackets are for dictionaries
# .get() if got error it will show "None" and not red errors or .get(TT, "Not Valid") errors would get "Not Valid"

#1
MonthsConversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March'
}

print(MonthsConversions.get('Sept', 'Not Valid'))

#2
phone = input('Phone: ')
num_to_words = {
     '1': 'One',
     '2': 'Two',
     '3': 'Three'
 }
output = ''
for ch in phone:
     output += num_to_words.get(ch, 'Not Valid') + ' '
print(output)

#3
customer = {
    'name': "Aden",
    'age': 24,
    'is_verified': True
}
customer['birthdate'] = '6 March 1997'
print(customer['birthdate'])


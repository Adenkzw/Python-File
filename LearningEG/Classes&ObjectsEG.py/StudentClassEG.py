#Creating own data type. Eg. phone data, student data etc
# can get information easily from the data
from StudentClassFuncEG import Student

student1 = Student('Jim', 'Business', 3.1)
student2 = Student('Jane', 'Art', 3.5)
print(student1.major)
print(student2.on_honour_roll())
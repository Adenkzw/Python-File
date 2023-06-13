#Read files that are outside of your python file
'''
read(.r) - read only
Write(.w) - create new file or overwrite whole file
append(.a) - add to the end of the file
read&write(.r+) - combination of r and w
'''

employee_file = open("LearningEG/RWAFilesEG/emp.txt", 'r')
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
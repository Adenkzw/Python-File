#for loop in for loop

#1
for x in range(3):
    for y in range(2): #the number in brackeyt wont be counted
        print(f'{x}, {y}')

#2
numbers = [2, 3, 5, 4, 6]
for x in numbers:
    output = ''
    for count in range(x):
        output += 'o'
    print(output)

#3
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[1][1])

for row in number_grid:
    for col in row:
        print(col)
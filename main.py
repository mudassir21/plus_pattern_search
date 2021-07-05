# Compiled and tested at "https://www.programiz.com/python-programming/online-compiler/"

# Input Matrix:
# *******
# *******
# ***x***
# **xxx**
# ***x***
# *******
# ***x***
# *******

# N.B: I was asked only to write a function that will return True or False for pattern found or not found. So I have written and used that. But I also did some additional things for my own interest. I wrote and used a function that returns the graph locations also. And also I show number of pattern found.

# Function for print 2D array matrix
def print_matrix(input_matrix):
    for row in input_matrix:
        for item in row:
            print(item, end='')
        print("\n", end='')

# Function for check plus pattern exists in a matrix or not
def is_pattern_exist(input_matrix, pattern_char):
    for idy,row in enumerate(input_matrix):
        for idx,item in enumerate(row):
            count = 0
            if item == pattern_char:
                if idy>0 and input_matrix[idy-1][idx] == item:
                    count += 1
                if idx>0 and input_matrix[idy][idx-1] == item:
                    count += 1
                if idy<len(input_matrix)-1 and input_matrix[idy+1][idx] == item:
                    count += 1
                if idx<len(row)-1 and input_matrix[idy][idx+1] == item:
                    count += 1
                if count >= 4:
                    return True
    return False
    
# Function for get plus pattern found loactions from a matrix
def get_pattern_locations(input_matrix, pattern_char):
    found_locations = [] 
    for idy,row in enumerate(input_matrix):
        for idx,item in enumerate(row):
            count = 0
            if item == pattern_char:
                if idy>0 and input_matrix[idy-1][idx] == item:
                    count += 1
                if idx>0 and input_matrix[idy][idx-1] == item:
                    count += 1
                if idy<len(input_matrix)-1 and input_matrix[idy+1][idx] == item:
                    count += 1
                if idx<len(row)-1 and input_matrix[idy][idx+1] == item:
                    count += 1
                if count >= 4:
                    found_locations.append((idx+1,idy+1))
    return found_locations

# Plus pattern character
pattern_char = 'x'

# Some input matrix for test
matrix1 = [
    ['*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*'],
    ['*','*','*','x','*','*','*'],
    ['*','*','x','x','x','*','*'],
    ['*','*','*','x','*','*','*'],
    ['*','*','*','*','*','*','*'],
    ['*','*','*','x','*','*','*'],
    ['*','*','*','*','*','*','*']
]
matrix2 = [
    ['*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*'],
    ['*','*','*','x','*','*','*'],
    ['*','x','x','x','*','*','*'],
    ['*','*','*','x','*','*','*'],
    ['*','*','*','*','*','*','*'],
    ['*','*','*','x','*','*','*'],
    ['*','*','*','*','*','*','*']
]
matrix3 = [
    ['*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*'],
    ['*','*','*','x','*','*','*'],
    ['*','*','x','x','x','*','*'],
    ['*','x','x','x','*','*','*'],
    ['*','*','x','*','*','*','*'],
    ['*','*','*','x','*','*','*'],
    ['*','*','*','*','*','*','*']
]
matrix4 = [
    ['*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*'],
    ['*','*','*','x','*','*','*'],
    ['*','*','x','x','*','*','*'],
    ['*','x','x','x','*','*','*'],
    ['*','*','x','*','*','*','*'],
    ['*','*','*','x','*','*','*'],
    ['*','*','*','*','*','*','*']
]
matrix5 = [
    ['*','*','*','*','*','*','*'],
    ['*','*','*','*','*','*','*'],
    ['*','*','*','x','*','*','*'],
    ['*','*','x','x','x','*','*'],
    ['*','*','*','x','*','*','*'],
    ['*','*','*','*','*','x','*'],
    ['*','*','*','x','x','x','x'],
    ['*','*','*','*','*','x','x']
]

# Test results for all input matrix
# matrix1
input_matrix = matrix1
print("\n\nInput matrix:")
print_matrix(input_matrix)
print(f"\nPlus Pattern of char '{pattern_char}' exists in the matrix:")
print(is_pattern_exist(input_matrix, pattern_char))
founded_locations = get_pattern_locations(input_matrix, pattern_char)
if founded_locations:
    print(f"\nPlus Pattern of char '{pattern_char}' Found {len(founded_locations)} times in following locations:")
    print(founded_locations)
else:
    print(f"\nPlus Pattern of char '{pattern_char}' Not found")

# matrix2
input_matrix = matrix2
print("\n\nInput matrix:")
print_matrix(input_matrix)
print(f"\nPlus Pattern of char '{pattern_char}' exists in the matrix:")
print(is_pattern_exist(input_matrix, pattern_char))
founded_locations = get_pattern_locations(input_matrix, pattern_char)
if founded_locations:
    print(f"\nPlus Pattern of char '{pattern_char}' Found {len(founded_locations)} times in following locations:")
    print(founded_locations)
else:
    print(f"\nPlus Pattern of char '{pattern_char}' Not found")

# matrix3
input_matrix = matrix3
print("\n\nInput matrix:")
print_matrix(input_matrix)
print(f"\nPlus Pattern of char '{pattern_char}' exists in the matrix:")
print(is_pattern_exist(input_matrix, pattern_char))
founded_locations = get_pattern_locations(input_matrix, pattern_char)
if founded_locations:
    print(f"\nPlus Pattern of char '{pattern_char}' Found {len(founded_locations)} times in following locations:")
    print(founded_locations)
else:
    print(f"\nPlus Pattern of char '{pattern_char}' Not found")

# matrix4
input_matrix = matrix4
print("\n\nInput matrix:")
print_matrix(input_matrix)
print(f"\nPlus Pattern of char '{pattern_char}' exists in the matrix:")
print(is_pattern_exist(input_matrix, pattern_char))
founded_locations = get_pattern_locations(input_matrix, pattern_char)
if founded_locations:
    print(f"\nPlus Pattern of char '{pattern_char}' Found {len(founded_locations)} times in following locations:")
    print(founded_locations)
else:
    print(f"\nPlus Pattern of char '{pattern_char}' Not found")

# matrix5
input_matrix = matrix5
print("\n\nInput matrix:")
print_matrix(input_matrix)
print(f"\nPlus Pattern of char '{pattern_char}' exists in the matrix:")
print(is_pattern_exist(input_matrix, pattern_char))
founded_locations = get_pattern_locations(input_matrix, pattern_char)
if founded_locations:
    print(f"\nPlus Pattern of char '{pattern_char}' Found {len(founded_locations)} times in following locations:")
    print(founded_locations)
else:
    print(f"\nPlus Pattern of char '{pattern_char}' Not found")

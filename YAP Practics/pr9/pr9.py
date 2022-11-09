from random import *   

def create_matrix(row, column, min, max):
    a = []
    for i in range(row):
        b = []
        for j in range(column):
            b.append(randint(min, max)) 
        a.append(b)
    return a

def print_matrix(matrix):
    row = len(matrix)
    for i in range(row):
        column = len(matrix[i])
        for j in range(column):
            print(matrix[i][j], end = ' ')
        print()

def write_matrix(filename, matrix):
    file = open(filename, 'w')
    row = len(matrix)
    for i in range(row):
        file.write(' '.join(map(str, matrix[i])))
        if i < row - 1:
            file.write('\n')

def write_text(filename, text):
    file = open(filename, 'w')
    file.write(text)

def read_matrix(filename):
    file = open(filename, 'r') 
    lines = file.readlines()
    row = len(lines)
    matrix = []
    for i in range(row):
        matrix.append(list(map(int, lines[i].split(' '))))
    return matrix

def v1_n1(matrix):
    x = 0
    s = 0
    t = 0
    row = len(matrix)
    for i in range(row):
        x += 1
        column = len(matrix[i])
        for j in range(x, column):
            if matrix[i][j] > 0:
                s += 1
                t += matrix[i][j] 
    return 'summa elementov: ' + str(t) + ' kolichestvo elementov: ' + str(s) 

def v1_n2(matrix):
    row = len(matrix)
    for i in range(row):
        column = len(matrix[i])
        first = matrix[i][0]
        last = matrix[i][column - 1]
        min_index = 0
        max_index = 0
        min = 10
        max = -10
        column = len(matrix[i])
        for j in range(column):
            if matrix[i][j] > max:
                max_index = j
                max = matrix[i][j]
                
            if matrix[i][j] < min:
                min_index = j 
                min = matrix[i][j]
                
        matrix[i][0] = max
        matrix[i][column - 1] = min
        matrix[i][max_index] = first
        matrix[i][min_index] = last
    
    return matrix
    
def v2_n2(matrix):
    row = len(matrix)
    for i in range(row):
        column = len(matrix[i])
        for j in range(column):
            q = matrix[0][0]
            r = matrix[1][0]
            t = matrix[2][0] 

            matrix[0][0] = matrix[0][2] 
            matrix[0][2] = q
            
            matrix[1][0] = matrix[1][2]
            matrix[1][2] = r
            
            matrix[2][0] = matrix[2][2]
            matrix[2][2] = t

    return matrix

# a = create_matrix(3, 3, -10, 10)
# print_matrix(a) 
# write_matrix('pr9\\1_КоролёвНикита_УБ-23_vvod_вариант2№2.txt', a)  

b = read_matrix('pr9\\1_КоролёвНикита_УБ-23_vvod_вариант1№2.txt')
print_matrix(b)
t = v1_n2(b)

write_matrix('pr9\\2_КоролёвНикита_УБ-23_vivod_вариант1№2.txt', t)  
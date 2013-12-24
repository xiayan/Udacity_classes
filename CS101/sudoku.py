#!/usr/bin/python

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]
incorrect4 =  [[1,1.5,3],
              [3,1,1.5],
              [1.5,3,1]]
incorrect4 =  [[0,1,2],
              [1,2,0],
              [2,0,1]]


def check_sudoku(sample):
    length = len(sample)
    for row in sample:
        if len(row) != length or len(row) != len(set(row)) or max(row) > length or min(row) <= 0:
            return False

    for i in range(length):
        column = []
        for j in range(length):
            if not isinstance(sample[j][i], int):
                return False
            column.append(sample[j][i])
        if len(set(column)) != len(column) or max(column) > length:
            return False
    return True

print check_sudoku(correct)
##>>> True
#
print check_sudoku(incorrect)
##>>> False
#
print check_sudoku(incorrect2)
##>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
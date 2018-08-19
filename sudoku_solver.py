# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 14:38:43 2018

@author: Bob Currie
"""

import numpy as np
#np.set_printoptions(threshold=np.nan)


# set sudoku_table dimensions
min_number = 1
max_number = 9
board_dimension = 9
box_dimension = 3

    
#def sudoku_solver(sudoku):
def sudoku_solver(sudoku):
    if(findSolution(sudoku, 0, 0)):
        #self.print_solution()
        return sudoku
    else:
        set_minusones(sudoku)



def isValidMove(sudoku, row, column, number):
    
    # check if number already in row
    for i in range(board_dimension):
        if(sudoku[row][i] == number):
            return False
        
    for j in range(board_dimension):
        if(sudoku[j][column] == number):
            return False
    
    boxVerticalCorner = (row // 3) * box_dimension
    boxHorizontalCorner = (column // 3) * box_dimension
    
    for i in range(box_dimension):
        for j in range(box_dimension):
            if(number == sudoku[i + boxVerticalCorner][j + boxHorizontalCorner]):
                return False
          
    return True

        
def findSolution(sudoku, row, column):
    if((row == max_number) and (column == max_number-1)):
        # problem solved
        return True
    
    if(row == max_number):
        column +=1
        row = 0
        
    if(sudoku[row][column] != 0):
        return findSolution(sudoku, row + 1, column)
        
    for number in range(1, 10):
        if(isValidMove(sudoku, row, column, number)):
            sudoku[row][column] = number
            if(findSolution(sudoku, row+1, column)):
                return True
            
    #if no solution found then backtrack
    sudoku[row][column] = 0
    return False



def set_minusones(sudoku):
    for i in range(9):
        for j in range(9):
            sudoku[i][j] = -1
    return sudoku    
             
            
sudoku = np.array([
                [3, 0, 6, 5, 0, 8, 4, 0, 0],
                [5, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1],
                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                [9, 0, 0, 8, 6, 3, 0, 0, 5],
                [0, 5, 0, 0, 9, 0, 6, 0, 0],
                [1, 3, 0, 0, 0, 0, 2, 5, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 4],
                [0, 0, 5, 2, 0, 6, 3, 0, 0]])       
    
sudoku2 = np.array([
        [0, 0, 4, 3, 0, 0, 2, 0, 9],
        [0, 0, 5, 0, 0, 9, 0, 0, 1],
        [0, 7, 0, 0, 6, 0, 0, 4, 3],
        [0, 0, 6, 0, 0, 2, 0, 8, 7],
        [1, 9, 0, 0, 0, 7, 4, 0, 0],
        [0, 5, 0, 0, 8, 3, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 1, 0, 5],
        [0, 0, 3, 5, 0, 8, 6, 9, 0],
        [0, 4, 2, 9, 1, 0, 3, 0, 0]])    
       
  
#sudoku = Sudoku(sudoku_table)
print(np.matrix(sudoku_solver(sudoku)))
print()
print(np.matrix(sudoku_solver(sudoku2)))
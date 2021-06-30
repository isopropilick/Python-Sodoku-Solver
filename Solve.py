import csv
import os
import time
from os import listdir
from os.path import isfile, join

usolved = [f for f in listdir(os.getcwd() + "\\Puzz\\usolved\\") if isfile(join(os.getcwd() + "\\Puzz\\usolved\\", f))]
solved = [f for f in listdir(os.getcwd() + "\\Puzz\\solved\\") if isfile(join(os.getcwd() + "\\Puzz\\solved\\", f))]
start_time = time.time()


def console_print(puzz):
    print('┎───────────────────────────┒')
    for i in puzz:
        if puzz.index(i) == 3 or puzz.index(i) == 6: print('┠───────────────────────────┨')
        print('' + str(''.join(str(i[0:3]))) + ' ' + str(''.join(str(i[3:6]))) + ' ' + str(''.join(str(i[6:9]))),
              end='\n')
    print('┖───────────────────────────┚')


def find_next_cell_to_fill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def is_valid(grid, i, j, e):
    row_ok = all([e != grid[i][x] for x in range(9)])
    if row_ok:
        column_ok = all([e != grid[x][j] for x in range(9)])
        if column_ok:
            sec_top_x, sec_top_y = 3 * (i // 3), 3 * (j // 3)
            for x in range(sec_top_x, sec_top_x + 3):
                for y in range(sec_top_y, sec_top_y + 3):
                    if grid[x][y] == e:
                        return False
            return True
    return False


def solve_sudoku(grid, i=0, j=0):
    i, j = find_next_cell_to_fill(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if is_valid(grid, i, j, e):
            grid[i][j] = e
            if solve_sudoku(grid, i, j):
                return True
            grid[i][j] = 0
    return False


def main():
    curr_puzz = []
    for file in usolved:
        with open(os.getcwd() + "\\Puzz\\usolved\\" + file) as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                curr_puzz.append(row)
            curr_puzz.pop(0)
            for i in range(0, len(curr_puzz)):
                for x in range(0, len(curr_puzz[i])):
                    curr_puzz[i][x] = int(curr_puzz[i][x])
        print("\n\n──────────────" + file + "──────────────\n\n Unsolved puzzle:")
        console_print(curr_puzz)
        print("\nSolved puzzle:")
        solve_sudoku(curr_puzz)
        console_print(curr_puzz)
        print("\n──────────────────────────────────")
        curr_puzz = []
    print("\n" + str(len(usolved)) + " Solved puzzles in %s seconds." % (time.time() - start_time))


if __name__ == "__main__":
    main()

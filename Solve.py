import os
from os import listdir
from os.path import isfile, join
import csv


unsolved = [f for f in listdir(os.getcwd()+"\\Puzzles\\unsolved\\") if isfile(join(os.getcwd()+"\\Puzzles\\unsolved\\", f))]
unsolved=sorted(unsolved)


def console_print(puzz):
    n=0
    print('┎───────────┒')
    for i in puzz:
        if n%3==0 and n!=0:
            print('┠───────────┨')
        print('┃'+str(''.join(i[1:4])),end='┃')
        print(str(''.join(i[4:7])),end='┃')
        print(str(''.join(i[7:10])),end='┃\n')
        n+=1
    n=0
    print('┖───────────┚')


for file in unsolved:
    curr_puzz = []
    print("----------"+str(unsolved.index(file)+1)+" ("+file+")----------")
    with open(os.getcwd()+"\\Puzzles\\unsolved\\"+file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            curr_puzz.append(row)
        curr_puzz.pop(0)
    console_print(curr_puzz)






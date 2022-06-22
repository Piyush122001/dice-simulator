import random 

def dice_3():
    dice= [[' ',' ','*'],[' ','*',' '],['*',' ',' ']]
    for row in range(3):
        for col in range(3):
            print(dice[row][col],end=' ')
        print()


def dice_1():
    dice= [[' ',' ',' '],[' ','*',' '],[' ',' ',' ']]
    for row in range(3):
        for col in range(3):
            print(dice[row][col],end=' ')
        print()

def dice_2():
    dice= [['*',' ',' '],[' ',' ',' '],[' ',' ','*']]
    for row in range(3):
        for col in range(3):
            print(dice[row][col],end=' ')
        print()
def dice_4():
    dice= [['*',' ','*'],[' ',' ',' '],['*',' ','*']]
    for row in range(3):
        for col in range(3):
            print(dice[row][col],end=' ')
        print()
def dice_5():
    dice= [['*',' ','*'],[' ','*',' '],['*',' ','*']]
    for row in range(3):
        for col in range(3):
            print(dice[row][col],end=' ')
        print()
def dice_6():
    dice= [['*',' ','*'],['*',' ','*'],['*',' ','*']]
    for row in range(3):
        for col in range(3):
            print(dice[row][col],end=' ')
        print()

def roling(n):
    switcher = {
        1 : dice_1(),
        2 : dice_2(),
        3 : dice_3(),
        4 : dice_4(),
        5 : dice_5(),
        6 : dice_6()
    }
    return switcher.get(n,"op")
n = random.randrange(1,6)
print(n)
roling(n)

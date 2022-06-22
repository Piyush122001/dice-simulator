import random 

n = random.randrange(1,7)
dice = [['','',''],['','',''],['','','']]
if n==1:
    for row in range(3):
        for col in range(3):
            if row == 1 and col == 1:
                dice[row][col] = "*"
            else:
                dice[row][col] = ' '
elif n==2:
    for row in range(3):
        for col in range(3):
            if row == 0 and col == 0:
                dice[row][col] = "*"
            elif row ==2 and col == 2:
                dice[row][col] = "*"
            else:
                dice[row][col] = ' '
elif n==3:
    for row in range(3):
        for col in range(3):
            if row == 0 and col == 2:
                dice[row][col] = "*"
            elif row==1 and col ==1:
                dice[row][col] = "*"
            elif row == 2 and col ==0:
                dice[row][col] ="*"
            else:
                dice[row][col] = ' '

elif n==4:
    for row in range(3):
        for col in range(3):
            if row == 0 :
                if col == 0 :
                    dice[row][col] = "*"
                elif col ==2:
                    dice[row][col] = "*"
            elif row ==2:
                if col == 0 :
                    dice[row][col] = "*"
                elif col ==2:
                    dice[row][col] = "*"
            else:
                dice[row][col] = " "
            

elif n==5 :
    for row in range(3):
        for col in range(3):
            if row == 0 :
                if col == 0 :
                    dice[row][col] = "*"
                elif col ==2:
                    dice[row][col] = "*"
            elif row ==1 and col==1:
                dice[row][col] = "*"
            elif row ==2:
                if col == 0 :
                    dice[row][col] = "*"
                elif col ==2:
                    dice[row][col] = "*"
            else:
                dice[row][col] = " "

else:
    for row in range(3):
        for col in range(3):
            if row == 0 :
                if col == 0 :
                    dice[row][col] = "*"
                elif col ==2:
                    dice[row][col] = "*"
            elif row ==1:
                if col == 0 :
                    dice[row][col] = "*"
                elif col ==2:
                    dice[row][col] = "*"
            elif row ==2:
                if col == 0 :
                    dice[row][col] = "*"
                elif col ==2:
                    dice[row][col] = "*"
            else:
                dice[row][col] = " "
            

for row in range(3):
    for col in range(3):
        print(dice[row][col],end=' ')

    print()

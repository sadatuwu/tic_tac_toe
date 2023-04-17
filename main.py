'''
updated version of main0 to engine2.1
'''

"START"#--------------------------------------------------------------------------

import platform
from os import system

import random

#--------------------------------------------------------------------

"GLOBALS"#-----------------------------------------------------------

board=[' ']*10
pos='''
1|2|3
-+-+-
4|5|6
-+-+-
7|8|9
'''
turn=0
player = 'X'
bot = 'O'
position =0
draw=1
odd=False
#E1 = True
#--------------------------------------------------------------------

"ALL FUNCTION DEFINITIONS"#------------------------------------------


def selectbot():
    level = input("Select bot (1 or 2): ")

    if level=='1' or level=='2':
            level =int(level)
    else:
        print("Only bot 1 and 2 are avaiable. Try again")
        level = selectbot()

    return level
    
#level = selectbot()
#print("level chosen",level)
    

"VISUALS"#-----------------------------------------------------------
def clearboard():
    global botmove
    for i in range(10):
        board[i]=' '



def newpage():
    
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

'''
def newpage():
    for i in range(30):
        print()
'''
def intro_message():
    printboard(board)
    print("Here are the positions on the board",pos)
    print("Toss for first move........")
    first = random.randint(0,1)
    #first=1
    if first :
        print("You go first as 'X'")
        #E1 = False
        
        
    else:
        print("Bot goes first as 'O', you are 'X'")
        #botmove = -1
        

    input("press enter to start.   ")
    newpage()
    printboard(board)

    return False if first else True

def printboard(board):
    for i in range(1,10):
        print(board[i],end='')
        if(i%3):
            print('|',end='')
        elif(i<=6):
            print("\n-+-+-")
        else:
            print()

#--------------------------------------------------------------------
#--------------------------------------------------------------------

"WIN AND DRAW"#------------------------------------------------------   
def win(X):
    W=[#all 8 possible "3 in a row" combinations
        [1,2,3], #1st row
        [4,5,6], #2nd row
        [7,8,9], #3rd row
        [1,4,7], #1st col
        [2,5,8], #2nd col
        [3,6,9], #3rd col
        [1,5,9], #dig one
        [3,5,7]  #dig two
    ]

    for i in range(8):
        matched = 1
        for j in range(3):
            if X != board[W[i][j]]:
                matched = 0

        if matched:
            return True
    return False


def full(board):
    for i in range(1,10):
        if board[i] ==' ':
            return False
    return True

#-------------------------------------------------------------------- 
#--------------------------------------------------------------------


"CHOSING MOVES"#-----------------------------------------------------
def select_move(X):
    global position, E1B1
    
    if(X==bot):
        
        if E1B1:
            E1B1= False
            #print("E1")
            return engine1(board)
        else:
            #print("E2")
            return engine2(board)

    else:
        #return engine1(board)
        p=input("Enter your position: ")
        if len(p)==1 and p>='1' and p<='9' :
            if board[int(p)]==' ':
                position=int(p)
            else:
                print("invalid move, Try again")
                position= select_move(X)

                
                
        else:
            print("invalid move, Try again")
            position= select_move(X)
 
        return position
    
    #return engine1(board)

#--------------------------------------------------------------------
#--------------------------------------------------------------------


'''
#ENGINES --------------------------------------------------------------
#--------------------------------------------------------------
'''

def engine1(board):
    emptycell=[]
    for i in range(1,10):
        if(board[i]==' '):
            emptycell.append(i)
    
    total= len(emptycell)
    index = random.randint(0,total-1)
    return emptycell[index]



def engine2(board):
    maxVal= -1000
    bestpos= 0
    
    for i in range(1,10):
        if board[i]==' ':
            board[i]=bot
            Eval = minimax(board, False)
            board[i]=' '
            
            if Eval > maxVal:
                maxVal=Eval
                bestpos=i


    return bestpos



def minimax(board, maximizing):
    if win(bot):
        return 1
    elif win(player):
        return -1
    
    elif full(board):
        return 0
    
    if maximizing:
        maxVal= -1000

        for i in range(1,10):
            if board[i]==' ':
                board[i]=bot
                Eval = minimax(board, False)
                board[i]=' '
                
                maxVal= max(Eval , maxVal)
        
        return maxVal
    
    else:
        minVal= 1000
        
        for i in range(1,10):
            if board[i]==' ':
                board[i]= player
                Eval = minimax(board, True)
                board[i]=' '
                
                minVal= min(Eval , minVal)
        
        return minVal
    


#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------

'''
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
'''

#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------

'''
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
'''

#MAIN GAME LOOP-------------------------------------------
while True:
 draw = True
 E1B1 = False #True   #engine1 entry for bot1
 #E1B2 = True
 turn=0
 clearboard()
 newpage()
 while turn<10:
    
    #initial screen setup:
    if turn==0 :
        odd=intro_message()
        turn += 1
        continue
    
    
    #choose who's move, select move, set move in board
    odd = False if(odd) else True
    who = player if(odd) else bot
    position = select_move(who)
    board[position]= who
    
    #new when player selects move, then show updated board:
    if odd :
        newpage()
    print()        
    print(who,"chose position",position)
    printboard(board)
    
    
    #if anyone win, end loop, not draw
    if win(who):
        print()
        print(who,"WON THE GAME.")
        draw= False
        break

    turn += 1
    
 #END OF GAME LOOP-------------------------------------------

 if draw:
    print("\nTHATS A DRAW!")


 print()
 print()
 a=input("play again? y/n")
 if(a=='n'):
    break
     



















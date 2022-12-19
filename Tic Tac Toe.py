while 1==1:
    print("Play Tic Tac Toe, designed by Smera Kanaujia")
    win=0
    player=1 
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    def grid():
        print("1      |2      |3")
        print(f"   {board[0]}   |   {board[1]}   |   {board[2]}   ") 
        print("_______|_______|_______")
        print("4      |5      |6")
        print(f"   {board[3]}   |   {board[4]}   |   {board[5]}   ")
        print("_______|_______|_______")
        print("7      |8      |9")
        print(f"   {board[6]}   |   {board[7]}   |   {board[8]}   ")
        print("       |       |       ")
    def check():
        #to check row
        for i in range(0,8,3):
            if board[i]==board[i+1]==board[i+2]:
                return board[i]
        #to check column
        for i in range(0,3):
            if board[i]==board[i+3]==board[i+6]:
                return board[i]
        #to check diagonal
        if board[0]==board[4]==board [8]:
            return board[0]
        elif board[2]==board[4]==board[6]:
            return board[2]
    grid()
    while player<10:
        if player % 2 != 0:
            current_player='X'
        else:
            current_player='O'
        print()
        x=int(input(f"{current_player} Enter position number"))
        if x==10:
            player=10
        x-=1
        if player % 2 != 0:
            board[x]='X'
        else:
            board[x]='O'
        player+=1
        print()
        grid()
        result=check()
        if result=='X':
            print("Player 1 Won!!")
            win=1
            break
        elif result=='O':
            print("Player 2 won!!")
            win=1
            break
    if win==0:
        print("DRAW GAME, PLAY AGAIN!")
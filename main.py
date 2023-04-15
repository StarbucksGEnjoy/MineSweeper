from tkinter import *
from random import randint
import numpy as np

ft = Tk()
ft.title("Mine Sweeper")
im0 = PhotoImage(file="0.png")
im1 = PhotoImage(file="1.png")
im2 = PhotoImage(file="2.png")
im3 = PhotoImage(file="3.png")
im4 = PhotoImage(file="4.png")
im5 = PhotoImage(file="5.png")
im6 = PhotoImage(file="6.png")
im7 = PhotoImage(file="7.png")
im8 = PhotoImage(file="8.png")
im9 = PhotoImage(file="bomb.png")
#ft.geometry("800x800")

im_dict = {0:im0,1:im1, 2:im2, 3:im3, 4:im4, 5:im5, 6:im6,7:im7,8:im8,9:im9}

def create_matrix(height, width):
    matrix = []
    
    around_matrix = np.zeros((height,width))

    #that part creates the matrix of bombs and 
    for hei in range(height):
        line = []
        for wid in range(width):
            line.append(False)
        matrix.append(line)


    bomb_counter = 0
    bomb_goal = int(height*width*0.3)

    #that part adds the desired amount of bombs
    while(bomb_counter!=bomb_goal):
        randX = randint(0,width-1)
        randY = randint(0,height-1)
        if (not matrix[randY][randX]):
            matrix[randY][randX] = True
            bomb_counter+=1



    #That part is Gonna create a matrix in which case there is the number of bombs around
    for x in range(0,width):
        for y in range(0,height):
 
            if not matrix[y][x]:#if the case is not a bomb
                bomb_around = 0

                #left top corner
                if x==0 and y==0:
                    if matrix[0][1]:
                        bomb_around+=1
                    if matrix[1][0]:
                        bomb_around+=1
                    if matrix[1][1]:
                        bomb_around+=1
                    #print(f"nw{bomb_around}")
                
                #right top corner
                if x==width-1 and y==0:
                    if matrix[y][x-1]:
                        bomb_around+=1
                    if matrix[y+1][x-1]:
                        bomb_around+=1
                    if matrix[y+1][x]:
                        bomb_around+=1
                    #print(f"ne{bomb_around}")
                
                #left bot corner
                if x==0 and y==height-1:
                    if matrix[y][x+1]:
                        bomb_around+=1
                    if matrix[y-1][x+1]:
                        bomb_around+=1
                    if matrix[y-1][x]:
                        bomb_around+=1
                    #print(f"sw{bomb_around}")

                #right bot corner
                if x==width-1 and y==height-1:
                    if matrix[y][x-1]:
                        bomb_around+=1
                    if matrix[y-1][x-1]:
                        bomb_around+=1
                    if matrix[y-1][x]:
                        bomb_around+=1
                    #print(f"se{bomb_around}")

                #left column
                if x==0 and y!=0 and y!=height-1:
                    if matrix[y-1][x+1]:
                        bomb_around+=1
                    if matrix[y][x+1]:
                        bomb_around+=1
                    if matrix[y+1][x+1]:
                        bomb_around+=1
                    if matrix[y-1][x]:
                        bomb_around+=1
                    if matrix[y+1][x]:
                        bomb_around+=1
                    #print(f"l{y} {bomb_around}") 

                #right column
                if x==width-1 and y!=0 and y!=height-1:
                    if matrix[y-1][x-1]:
                        bomb_around+=1
                    if matrix[y][x-1]:
                        bomb_around+=1
                    if matrix[y+1][x-1]:
                        bomb_around+=1
                    if matrix[y-1][x]:
                        bomb_around+=1
                    if matrix[y+1][x]:
                        bomb_around+=1
                    #print(f"r{y} {bomb_around}") 
    
                #top row
                if y==0 and x!=0 and x!=width-1:
                    if matrix[y][x-1]:
                        bomb_around+=1
                    if matrix[y][x+1]:
                        bomb_around+=1
                    if matrix[y+1][x-1]:
                        bomb_around+=1
                    if matrix[y+1][x]:
                        bomb_around+=1
                    if matrix[y+1][x+1]:
                        bomb_around+=1
                    #print(f"t{y} {bomb_around}")
                
                #bot row
                if y==height-1 and x!=0 and x!=width-1:
                    if matrix[y][x-1]:
                        bomb_around+=1
                    if matrix[y][x+1]:
                        bomb_around+=1
                    if matrix[y-1][x-1]:
                        bomb_around+=1
                    if matrix[y-1][x]:
                        bomb_around+=1
                    if matrix[y-1][x+1]:
                        bomb_around+=1
                    #print(f"b{y} {bomb_around}")

                #middle cases
                if x!=0 and x!=width-1 and y!=0 and y!=height-1:
                    if matrix[y][x-1]:
                        bomb_around+=1
                    if matrix[y][x+1]:
                        bomb_around+=1
                    if matrix[y+1][x-1]:
                        bomb_around+=1
                    if matrix[y+1][x]:
                        bomb_around+=1
                    if matrix[y+1][x+1]:
                        bomb_around+=1
                    if matrix[y-1][x-1]:
                        bomb_around+=1
                    if matrix[y-1][x]:
                        bomb_around+=1
                    if matrix[y-1][x+1]:
                        bomb_around+=1
                    #print(f"{x},{y} : {bomb_around}")

                around_matrix[y,x] = bomb_around
    

    return matrix,around_matrix

def game_over(): 
    global matrix
    
    im0_go = PhotoImage(file="0.png")
    im9_go = PhotoImage(file="bomb.png")

    height = len(matrix)
    width = len(matrix[1])
    
    
    for hei in range(0,height):
        for wid in range(0,width):
            if(matrix[hei][wid]):
                w = Label(ft,  
                    image=im9_go,
                    fg="white",
                    relief="groove")
                w.grid(row=hei, column=wid)
                print(f"hei:{hei}  wid:{wid}")
            else: 
                w = Label(ft,  
                    image=im0_go,
                    fg="white",
                    relief="groove")
                w.grid(row=hei, column=wid)
    
    #ft.mainloop


matrix, ar_mat = create_matrix(height = 15,width = 10)

height = len(matrix)
width = len(matrix[1])

for hei in range(0,height):
    for wid in range(0,width):
        if(matrix[hei][wid]):
            w = Button(ft,  
                command=game_over,
                image=im9,
                fg="white",
                relief="groove")
            w.grid(row=hei, column=wid)
        else: 
            surr = ar_mat[hei,wid]
            lbl = Label(ft, image= im_dict[surr]).grid(row=hei, column=wid)
            btn = Button(ft,  
                image=im_dict[0],
                fg="white",
                relief="groove")
            btn.grid(row=hei, column=wid)
            btn.config(command = btn.destroy)


ft.mainloop()



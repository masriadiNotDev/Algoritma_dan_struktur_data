#tictactoe 
#MASRIADI SISTEM INFORMASI
#nim D0425309
#hasiyl modifikasi dari program tictactoe dasar
#tambahan popup messagebox dari tkinter dan tambahan tombol untuk mengakhiri program
#perubahan warna dan posisi tombol



from tkinter import *
from tkinter import messagebox #untuk menampilkan pesan atau popup
import random
window = Tk()
x_state = []   
o_state = []

window.title("Welcome to TICTACTOE game")

#creating a turn variable
turn = 0


#creating a winning_list
winning_list = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]


# membuat jendela mengambang menggunakan module tkinter
window.title("TTC mod by masriadi")
window.configure(bg="blue")
window.geometry("625x600")
#adding padding to the window
window.config(padx=10, pady=10)

#label dan font
title_label = Label(text="klik mulai untuk memulai", font=("arial", 20, "bold"))
title_label.grid(row=4, column=1, padx=15, pady=10)

#creating a game_tied function  
def game_tied():
    global x_state, o_state
    if x_state.count(1) + o_state.count(1) == 9: #count 1's in x_state and o_state
        title_label.config(text="seri")
        messagebox.showinfo("permainan seri", "Permainan berakhir dengan seri!") #untuk popup pesan seri
        for i in button_list:
            i.config(command=DISABLED)


#membuat tombol list untuk X dan O 
button_list = []

#creating cells for the game
def create_cells():
    global button_list
    for i in range(3):
        for j in range(3):
            cell = Button(
                text=" ", 
                font=("arial", 30, "bold"), 
                width=8, 
                height=3, 
                borderwidth=1,
                bg ='darkblue',
                state=DISABLED,
            )
            button_list.append(cell)
            cell.grid(row=i+1, column=j+1)
#function to print the board
def printboard(x_state, o_state):     
    #function to check game tied
    game_tied()

    #mencetak tombol
    #msriadi
    for i in range(3):
        for j in range(3):
            if x_state[i*3+j] == 1:
                button_list[i*3+j].config(text="X",
                                            fg="white",
                                            font=("arial", 30, "bold"), 
                                            command=DISABLED)
            elif o_state[i*3+j] == 1:
                button_list[i*3+j].config(text="O",
                                            fg="cyan",
                                            font=("arial", 30, "bold"), 
                                            command=DISABLED)
            
            else:
                button_list[i*3+j].config(text=" ")

def restart_game():
    global turn, x_state, o_state, button_list
    turn = random.randint(0, 1)
    x_state = [0,0,0,0,0,0,0,0,0]
    o_state = [0,0,0,0,0,0,0,0,0]

#enabling the buttons
    for i in range(3):
        for j in range(3):
            button_list[i*3+j].config( state=NORMAL,command=lambda i=i, j=j: handle_click(i, j))

    printboard(x_state, o_state)




#ngecek siapa yg mnang 

#function to handle the button click
def handle_click(row, col):
    global turn, x_state, o_state
    if turn:
        title_label.config(text="GILIRAN O",fg="lightblue", bg="blue" )
        x_state[row*3+col] = 1
    else:
        title_label.config(text="GILIRAN X",fg="lightblue", bg="blue" )
        o_state[row*3+col] = 1
    printboard(x_state, o_state)
    result = check_winner(x_state, o_state)
    if result == 1:
        for i in button_list:
            i.config(command=DISABLED)
    elif result == 0:
        for i in button_list:
            i.config(command=DISABLED)
    turn = 1 - turn


# 1. start button
start_button = Button(text="MULAI", font=("arial", 16, "bold"),  fg="white", bg="darkblue" )
start_button.grid(row=4, column=2, padx=15, pady=10, ipady=10 , ipadx=5)
#akhiri button 
akhiri_button = Button(text="KELUAR", font=("arial", 16, "bold"), fg="white", bg="darkblue"  )
akhiri_button.grid(row=4, column=3, padx=12, pady=4 , ipady=10 ,)

#function to start the game
def start_game():
    global turn, x_state, o_state, button_list
    turn = random.randint(0, 1)
    x_state = [0,0,0,0,0,0,0,0,0]
    o_state = [0,0,0,0,0,0,0,0,0]

#enabling the buttons
    for i in range(3):
        for j in range(3):
            button_list[i*3+j].config( state=NORMAL,command=lambda i=i, j=j: handle_click(i, j))

    printboard(x_state, o_state)
    title_label.config(text="GILIRAN O" if turn == 0 else "GILIRAN X",fg="white", bg="blue" )

#binding the start button to the start_game function
    start_button.config(text="RESTART")
    akhiri_button.config(text="AKHIRI")

#binding the start button to the start_game function
start_button.config(command=start_game)  
akhiri_button.config(command=quit)
# calling the create_cells function
def check_winner(x_state, o_state):
    for i in winning_list:
        if x_state[i[0]] and x_state[i[1]] and x_state[i[2]]:
            title_label.config(text="X MENANG")
            jawab = messagebox.askyesno("X menang", "Lanjutkan permainan?")  # POPUP
            if jawab:
              print("1")
            else:
                quit()
            printboard(x_state, o_state)

            return 1
        if o_state[i[0]] and o_state[i[1]] and o_state[i[2]]:
            title_label.config(text="O menang")
            jawab = messagebox.askyesno("O MENANG", "Lanjutkan permainan?") # POPUP
            if jawab:
              print("restart")
              start_game()
            else:
                quit()
            printboard(x_state, o_state)
            printboard(x_state, o_state)
            return 0
        
    return -1

create_cells()
start_game()
#creating mainloop for the window
window.mainloop()

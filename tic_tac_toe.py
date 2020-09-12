# basic window interface by importing tkinter module
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("100x50+320+150")
root.attributes('-alpha', 2.0)
root.minsize(width=30, height=55)
root.maxsize(width=30, height=55)
root.config(bg="#befc03")
root.title("Tic Tac Toe")
# variables we will use further in  the game
font = "Verdana", 20, "bold"
back = "#befc03"
fore = "#fc03b1"
active = "blue"
db = "blue"
player = "X"
m=1

# creating play button
play_button=Button(root,text="Play",font=font,bg="red",fg="#0ffc03",activebackground="blue",command=lambda:changed_geometry())
play_button.grid(row=2,column=4,padx=10)

# changed size of window after clicking on play button
def changed_geometry():
    root.geometry("560x375+320+105")
    root.attributes('-alpha', 2.0)
    root.minsize(width=650, height=560)
    root.maxsize(width=650, height=560)
    all_buttons()

# all the required buttons are created inside this function including some labels
def all_buttons():
    lab = Label(root, text="Tic Tac Toe\n Game By \nSandeep Bisht", font=("Gungshu", 20, ""), fg="blue")
    lab.grid(row=0, column=4)
    lab = Label(root, text="Player= X\n Player= 0", font=("lucida", 20, "bold"), fg="blue")
    lab.grid(row=1, column=4)
    lab = Label(root, text="Tic Tac Toe\n Game By \nSandeep Bisht", font=("lucida", 20, "bold"), fg="blue")
    lab.grid(row=0, column=4)
    lab = Label(root, text="Player= X\n Player= 0", font=("lucida", 20, "bold"), fg="blue")
    lab.grid(row=1, column=4)

    but1=Button(root,text="",font=font,command=lambda:buttons_logic(1),bg=back,fg=fore,activebackground=active,disabledforeground=db)
    but1.grid(row=0,column=0,ipadx=50,ipady=50)

    but2=Button(root,text="",font=font,command=lambda:buttons_logic(2),bg=back,fg=fore,activebackground=active,disabledforeground=db)
    but2.grid(row=0,column=1,ipadx=50,ipady=50)

    but3=Button(root,text="",font=font,command=lambda:buttons_logic(3),bg=back,fg=fore,activebackground=active,disabledforeground=db)
    but3.grid(row=0,column=2,ipadx=50,ipady=50)

    but4=Button(root,text="",font=font,command=lambda:buttons_logic(4),bg=back,fg=fore,activebackground=active,disabledforeground=db)
    but4.grid(row=1,column=0,ipadx=50,ipady=50)

    but5=Button(root,text="",font=font,command=lambda:buttons_logic(5),bg=back,fg=fore,activebackground=active,disabledforeground=db)
    but5.grid(row=1,column=1,ipadx=50,ipady=50)

    but6=Button(root,text="",font=font,command=lambda:buttons_logic(6),bg=back,fg=fore,activebackground=active,disabledforeground=db)
    but6.grid(row=1,column=2,ipadx=50,ipady=50)

    but7=Button(root,text="",font=font,command=lambda:buttons_logic(7),bg=back,fg=fore,activebackground=active,disabledforeground=db)
    but7.grid(row=2,column=0,ipadx=50,ipady=50)

    but8=Button(root,text="",font=font,command=lambda:buttons_logic(8),bg=back,fg=fore,activebackground=active,disabledforeground=db)
    but8.grid(row=2,column=1,ipadx=50,ipady=50)

    but9=Button(root,text="",font=font,command=lambda:buttons_logic(9),bg=back,fg=fore,activebackground=active,disabledforeground=db)
    but9.grid(row=2,column=2,ipadx=50,ipady=50)
    exit_button = Button(root, text="Exit", font=font, bg="orange", fg="#fc03b1", activebackground="blue",
                     command=exit)
    exit_button.grid(row=3, column=4)

    # reset_button = Button(root, text="Reset", font=font, bg="orange", fg="#fc03b1", activebackground="blue",
    #                      command=lambda:changed_geometry())
    # reset_button.grid(row=5, column=3)

    # the logic behind the buttons are created in this function
    def buttons_logic(val):
        global player
        if val == 1 and player == "X":

            but1.config(text="X")
            but1["state"] = DISABLED
            player = "0"

        elif val == 1 and player == "0" :
            but1.config(text="0")
            but1["state"] = DISABLED
            player = "X"

        elif val == 2 and player == "X":
            but2.config(text="X")
            but2["state"] = DISABLED
            player = "0"

        elif val == 2 and player == "0":
            but2.config(text="0")
            but2["state"] = DISABLED
            player = "X"

        elif val == 3 and player == "X" :
            but3.config(text="X")
            but3["state"] = DISABLED
            player = "0"

        elif val == 3 and player == "0" :
            but3.config(text="0")
            but3["state"] = DISABLED
            player = "X"

        elif val == 4 and player == "X" :
            but4.config(text="X")
            but4["state"] = DISABLED
            player = "0"

        elif val == 4 and player == "0" :
            but4.config(text="0")
            but4["state"] = DISABLED
            player = "X"

        elif val == 5 and player == "X" :
            but5.config(text="X")
            but5["state"] = DISABLED
            player = "0"

        elif val == 5 and player == "0" :
            but5.config(text="0")
            but5["state"] = DISABLED
            player = "X"

        elif val == 6 and player == "X" :
            but6.config(text="X")
            but6["state"] = DISABLED
            player = "0"

        elif val == 6 and player == "0" :
            but6.config(text="0")
            but6["state"] = DISABLED
            player = "X"

        elif val == 7 and player == "X" :
            but7.config(text="X")
            but7["state"] = DISABLED
            player = "0"

        elif val == 7 and player == "0" :
            but7.config(text="0")
            but7["state"] = DISABLED
            player = "X"

        elif val == 8 and player == "X" :
            but8.config(text="X")
            but8["state"] = DISABLED
            player = "0"

        elif val == 8 and player == "0" :
            but8.config(text="0")
            but8["state"] = DISABLED
            player = "X"

        elif val == 9 and player == "X" :
            but9.config(text="X")
            but9["state"] = DISABLED
            player = "0"

        elif val == 9 and player == "0" :
            but9.config(text="0")
            but9["state"] = DISABLED
            player = "X"

        check_result()

# this function checks the result of the game
    def check_result():
        global play_button
        play_button["state"] = DISABLED
        global m
        m=m+1
        # winning condition for player "0"
        if (but1["text"]=="0" and but2["text"]=="0" and but3["text"]=="0"
            or but4["text"]=="0" and but5["text"]=="0" and but6["text"]=="0"
            or but7["text"] == "0" and but8["text"] == "0" and but9["text"] == "0"
            or but1["text"]=="0" and but4["text"]=="0" and but7["text"]=="0"
            or but2["text"]=="0" and but5["text"]=="0" and but8["text"]=="0"
            or but3["text"]=="0" and but6["text"]=="0" and but9["text"]=="0"
            or but1["text"] == "0" and but5["text"] == "0" and but9["text"] == "0"
            or but3["text"] == "0" and but5["text"] == "0" and but7["text"] == "0"):
            # display message that player 0 has won
            messagebox.showinfo("Result", "Player 0 is winner")
            # disabled all the buttons if player 0 wins
            but1["state"]= DISABLED
            but2["state"] = DISABLED
            but3["state"] = DISABLED
            but4["state"] = DISABLED
            but5["state"] = DISABLED
            but6["state"] = DISABLED
            but7["state"] = DISABLED
            but8["state"] = DISABLED
            but9["state"] = DISABLED

            # it will display play again button so user can play the game again
            play_button = Button(root, text="Play Again", font=font, bg="orange", fg="#fc03b1", activebackground="blue",command=lambda: changed_geometry())
            play_button.grid(row=2, column=4)
            m=1

        # winning condition for player "X"
        elif (but1["text"]=="X" and but2["text"]=="X" and but3["text"]=="X"
            or but4["text"]=="X" and but5["text"]=="X" and but6["text"]=="X"
            or but7["text"] == "X" and but8["text"] == "X" and but9["text"] == "X"
            or but1["text"]=="X" and but4["text"]=="X" and but7["text"]=="X"
            or but2["text"]=="X" and but5["text"]=="X" and but8["text"]=="X"
            or but3["text"]=="X" and but6["text"]=="X" and but9["text"]=="X"
            or but1["text"] == "X" and but5["text"] == "X" and but9["text"] == "X"
            or but3["text"] == "X" and but5["text"] == "X" and but7["text"] == "X"):
            # display message that player X has won
            messagebox.showinfo("Result", "Player X is winner")

            # disabled all the buttons if player X wins
            but1["state"] = DISABLED
            but2["state"] = DISABLED
            but3["state"] = DISABLED
            but4["state"] = DISABLED
            but5["state"] = DISABLED
            but6["state"] = DISABLED
            but7["state"] = DISABLED
            but8["state"] = DISABLED
            but9["state"] = DISABLED

            # it will display play again button so user can play the game again
            play_button = Button(root, text="Play Again", font=font, bg="orange", fg="#fc03b1", activebackground="blue",command=lambda:changed_geometry())
            play_button.grid(row=2, column=4)
            m=1

        # condition if the match is drawn
        elif m>=10:
            # display message that match is drawn
            messagebox.showinfo("Result","Match Drawn")

            # it will display play again button so user can play the game again
            play_button = Button(root, text="Play Again", font=font, bg="orange", fg="#fc03b1", activebackground="blue",command=lambda:changed_geometry())
            play_button.grid(row=2, column=4)
            m=1

root.mainloop()
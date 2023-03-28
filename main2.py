from tkinter import *
from tkinter import messagebox

root = Tk()
root.resizable(False, False)
root.title("Tic Tac Toe")

Label(root, text="Tic Tac Toe", font=('Ariel', 25)).pack()
play_area = Frame(root, width=300, height=300, bg='white')
play_area.pack(pady=10, padx=10)

button_identities = []
i = 0
# Create 9 buttons and place them in the list "button_identities"
for j in range(1, 4):
    for k in range(3):
        btn = Button(play_area, command=lambda i=i: player(i), text="", height=5, width=10, relief=GROOVE, bg="white",
                     bd=1)
        btn.grid(row=[j], column=[k])
        button_identities.append(btn)
        i += 1


cur_player = ""


def player(i):
    global cur_player
    player1 = "X"
    player2 = "O"

    # Condition that verifies that the field is empty
    if button_identities[i]["text"] != "":
        pass
    else:
        # Switch player moves
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1

        # Change the value of text button
        bname = (button_identities[i])
        bname.config(text=cur_player)

        check_win()


def check_win():
    condition = (button_identities[0]['text'] == button_identities[1]['text'] == button_identities[2]['text'] != "",
                 button_identities[3]['text'] == button_identities[4]['text'] == button_identities[5]['text'] != "",
                 button_identities[6]['text'] == button_identities[7]['text'] == button_identities[8]['text'] != "",
                 button_identities[0]['text'] == button_identities[3]['text'] == button_identities[6]['text'] != "",
                 button_identities[1]['text'] == button_identities[4]['text'] == button_identities[7]['text'] != "",
                 button_identities[2]['text'] == button_identities[5]['text'] == button_identities[8]['text'] != "",
                 button_identities[0]['text'] == button_identities[4]['text'] == button_identities[8]['text'] != "",
                 button_identities[2]['text'] == button_identities[4]['text'] == button_identities[6]['text'] != ""
                 )

    if any(condition):
        messagebox.showinfo(title="gg", message=("Joueur", cur_player, "gagne"))


root.mainloop()

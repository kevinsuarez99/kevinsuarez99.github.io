# Rock, Paper, Sissors, Choose game
# 1 = rock | 2 = paper | 3 = sissor
import tkinter
import random
userChoice = 0
cpuChoice = 0
class RPSGame:
    def __init__(self):
        self.game_window = tkinter.Tk()
        self.game_window.title("Game")

        self.desc_label = tkinter.Label(self.game_window, text = "Select from the choices below: ")
        self.desc_label.pack()

        self.button_frames = tkinter.Frame(self.game_window)
        self.button_frames.pack()

        self.rock_button = tkinter.Button(self.button_frames, text = "Rock", command= self.rock_selection)
        self.rock_button.pack()

        self.paper_button = tkinter.Button(self.button_frames, text = "Paper", command= self.paper_selection)
        self.paper_button.pack(side= "left")

        self.sissor_button = tkinter.Button(self.button_frames, text = "Sissors", command= self.sissor_selection)
        self.sissor_button.pack(side = "left")

        self.cpu_var = tkinter.StringVar()
        self.cpu_var.set("CPU is wating on you...")

        self.cpu_label = tkinter.Label(self.game_window, textvariable = self.cpu_var)
        self.cpu_label.pack()

        #who WON!
        self.winner_var = tkinter.StringVar()
        self.winner_var.set("Who will Win.")

        self.winner_frame = tkinter.Frame(self.game_window)
        self.winner_frame.pack()

        self.winner_label = tkinter.Label(self.winner_frame, textvariable = self.winner_var)
        self.winner_label.pack()

        self.final_frame = tkinter.Frame(self.game_window)
        self.final_frame.pack(side= "right")

        self.quit_button = tkinter.Button(self.final_frame, text= "Quit Game", command= self.game_window.destroy)
        self.quit_button.pack()



        tkinter.mainloop()

    def rock_selection(self):
        global userChoice
        global cpuChoice

        userChoice = 1 #user chose rock
        cpuChoiceLst = [1,2,3]
        cpuChoice = random.choice(cpuChoiceLst)

        if cpuChoice == 1:
            self.winner_var.set("Its a tie.\nTry again.")
            self.cpu_var.set("The CPU chosed Rock")
        elif cpuChoice == 2:
            self.winner_var.set("You Lost.")
            self.cpu_var.set("The CPU chosed Paper.")
        elif cpuChoice == 3:
            self.winner_var.set("You Won.")
            self.cpu_var.set("The CPU chosed Sissors.")

    def paper_selection(self):
        global userChoice
        global cpuChoice

        userChoice = 2#paper
        cpuChoiceLst = [1,2,3]
        cpuChoice = random.choice(cpuChoiceLst)

        if cpuChoice == 1:#rock
            self.winner_var.set("You Won.")
            self.cpu_var.set("The CPU chosed Rock.")
        elif cpuChoice == 2:#paper
            self.winner_var.set("Its a tie.\nTry again.")
            self.cpu_var.set("The CPU chosed Paper.")
        elif cpuChoice == 3:#sissor
            self.winner_var.set("You Lost.")
            self.cpu_var.set("The CPU chosed Sissors.")

    def sissor_selection(self):
        global userChoice
        global cpuChoice

        userChoice = 3#sissor
        cpuChoiceLst = [1,2,3]
        cpuChoice = random.choice(cpuChoiceLst)

        if cpuChoice == 1:#rock
            self.winner_var.set("You Won.")
            self.cpu_var.set("The CPU chosed Rock.")
        elif cpuChoice == 2:#paper
            self.winner_var.set("You Won.")
            self.cpu_var.set("The CPU chosed Paper.")
        elif cpuChoice == 3:#sissor
            self.winner_var.set("Its a tie.\nTry again.")
            self.cpu_var.set("The CPU chosed Sissors.")



my_gui = RPSGame()

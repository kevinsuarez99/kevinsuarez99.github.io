#Speeding Fine Calculator GUI Program
#Questions needed to be asked
# Speed Limit of a zone:
# Speed of the Vehicle:
# Whether Construction or School Zone: Yes/No
spclZone = False#global variable
import tkinter#imports tkinter so it can be used to create a GUI window program
#makes the beginning of a class
class SpeedCalcGUI:#class name
    def __init__(self):#function that initializes the class with a parameter of self
        #main Window
        self.main_window = tkinter.Tk()
        self.main_window.title("Fine Calculator")#sets the name of the main window

        self.desc_var = tkinter.StringVar()#makes it a variable that will contain a string in it
        self.desc_var.set("This program calculates the fines for speeding.")#sets what the string in it is
        #description frame
        self.descMsg_frame = tkinter.Frame(self.main_window)
        self.descMsg_frame.pack()
        #description label
        self.descMsg_label = tkinter.Label(self.descMsg_frame, textvariable= self.desc_var)
        self.descMsg_label.pack()

        #speed limit frame
        self.spdLmt_frame = tkinter.Frame(self.main_window)#creates a frame for the speed limit in the main window
        self.spdLmt_frame.pack()#the pack function makes it appear in the main window, otherwise it wont be displayed
        #speed limit label
        self.spdLmt_label = tkinter.Label(self.spdLmt_frame, text = "Speed Limit of a zone: ")#creates a label with a description of what the input should be
        self.spdLmt_label.pack(side = "left")
        #speed limit input box
        self.spdLmt_entry = tkinter.Entry(self.spdLmt_frame, width = "5")#creates an input box so a value can be inputed
        self.spdLmt_entry.pack(side = "left")

        #speed of the vehicle frame
        self.speed_frame = tkinter.Frame(self.main_window)
        self.speed_frame.pack()
        #speed of the vehicle label
        self.speed_label = tkinter.Label(self.speed_frame, text = "Speed of the Vehicle: ")
        self.speed_label.pack(side = "left")
        #speed of the vehicle input box
        self.speed_entry = tkinter.Entry(self.speed_frame, width = "5")#the width sets the size of the input box is
        self.speed_entry.pack(side = "left")

        #type of zone or no zone frame
        self.zone_frame = tkinter.Frame(self.main_window)
        self.zone_frame.pack()
        #type of zone or no zone label
        self.zone_label = tkinter.Label(self.zone_frame, text = "Select the type of:")#takes an input of either yes or not to let the
        self.zone_label.pack(side = "left")                                                                #the computer know if there was any special zone or no
        #type of zone or no zone input box
        #radio buttons
        self.rb_var = tkinter.IntVar()
        self.rb_var.set(0)
        #Radiobutton
        self.const_rb = tkinter.Radiobutton(self.main_window, text= "Construction Zone", variable = self.rb_var, value = 1, command= self.special_zone)#radio button for a construction zone
        self.schl_rb = tkinter.Radiobutton(self.main_window, text= "School Zone", variable = self.rb_var, value = 2, command= self.special_zone)#radio button for a school zone
        self.noZone_rb = tkinter.Radiobutton(self.main_window, text= "None", variable = self.rb_var, value = 3, command= self.reg_zone)#radio button for a regular zone
        #packs the radio buttons so they can show in the main window
        self.const_rb.pack()
        self.schl_rb.pack()
        self.noZone_rb.pack()

        #calculated fine value
        self.value = tkinter.StringVar()#creates a string variable which will contain the output string with the calculated fine
        self.value.set("...")#at first this variable's value will be set to "..." but the it will be subbed with the actual output string
        self.fine_frame = tkinter.Frame(self.main_window)#then a frame for it is created
        self.fine_label = tkinter.Label(self.fine_frame, textvariable= self.value)#a label is also created where will show "..." at first but then will show
                                                                                #the output string
        self.fine_frame.pack()#packs the frame and the label so it can be displayed in the ,ain window
        self.fine_label.pack()

        #bottons
        self.calc_button = tkinter.Button(self.main_window, text = "Calculate Fine", command= self.calc_fine)#button that when clicked, calculates the fine by
        self.calc_button.pack()                                                                             #calling a function inside the code of the program

        self.quit_button = tkinter.Button(self.main_window, text = "Quit", command= self.main_window.destroy)#button that when clicked closes the main window
        self.quit_button.pack()

        tkinter.mainloop()#keeps the main window showing on the screen, otherwise will not pop up

    def special_zone(self):#function that sets the global variable to True, which means that there is a special zone
        global spclZone#calls the global variable
        spclZone = True#sets the value of the global variable

    def reg_zone(self):#function that sets the value of the global variable so that it says that there is no special zone
        global spclZone
        spclZone = False#no special zone


    def calc_fine(self):#function that calculates the fine
        sLmt = float(self.spdLmt_entry.get())#gets the value entered in the speed limit input box
        s = float(self.speed_entry.get())#gets the value entered in the speed of the vehicle input box

        spDif = s - sLmt#formula that calculates the difference between (speed of the vehicle) - (speed limit)

        overSpeed = False#is set to false at first, meaning the car was not speeding

        global spclZone

        if spDif > 0:
            overSpeed = True # means the vehicle is over the speed limit
        else:
            overSpeed = False# means the vehicle is under the speed Limit

        if overSpeed == True and spclZone == False:#if there was no special zone, depending on the range of the  difference calculated by the earlier
            if spDif > 0 and spDif < 10:                                        #formula, the fine will be printed
                self.value.set("""The fine is $129.00.\n"Be Careful" """)#the value of the variable will be changed with the this string
            elif spDif >= 10 and spDif < 15:
                self.value.set("""The fine is $204.00.\n"Drive with caution" """)
            elif spDif >= 15 and spDif < 20:
                self.value.set("""The fine is $254.00.\n"You are driving dangerous" """)
            elif spDif >= 20 and spDif < 30:
                self.value.set("""The fine is $279.00.\n"You are in Danger zone" """)
            else:
                self.value.set("""Court is mandatory.\n"See ya in court" """)

        #in the case of there being a special zone
        elif overSpeed == True and spclZone == True:
            if spDif > 0 and spDif < 10:
                self.value.set("""The fine is $258.00.\n"Be Careful" """)
            elif spDif >= 10 and spDif < 15:
                self.value.set("""The fine is $408.00.\n"Drive with caution" """)
            elif spDif >= 15 and spDif < 20:
                self.value.set("""The fine is $508.00.\n"You are driving dangerous" """)
            elif spDif >= 20 and spDif < 30:
                self.value.set("""The fine is $558.00.\n"You are in Danger zone" """)
            else:
                self.value.set("""Court is mandatory.\n"See ya in court" """)
        else:
            self.value.set("""The fine is $0.0.\n"Keep it up!" """)


my_gui = SpeedCalcGUI()#needs to be included for the main window to show

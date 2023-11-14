import tkinter as tk

class Calculator:
    def __init__(self):
        #Set a variable (usually called "root", "master" or "window") to the value of "tk.Tk(), the title of the window and a non-modifiable window"
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.minsize(301, 415)
        self.root.maxsize(301, 415)
        #Call the variables that create the buttons
        self.createScreen()
        self.createButtons()
        #Set the main loop in this window(root)
        self.root.mainloop()

    def createButtons(self):
        #Create all the buttons with its own width, height, content(text), function(command) and position(grid)
        self.button1 = tk.Button(self.root, width=8, height=4, text="1", command=lambda: self.operation("1"))
        self.button1.grid(row=3, column=0)

        self.button2 = tk.Button(self.root, width=8, height=4, text="2", command=lambda: self.operation("2"))
        self.button2.grid(row=3, column=1)

        self.button3 = tk.Button(self.root, width=8, height=4, text="3", command=lambda: self.operation("3"))
        self.button3.grid(row=3, column=2)

        self.button4 = tk.Button(self.root, width=8, height=4, text="4", command=lambda: self.operation("4"))
        self.button4.grid(row=2, column=0)

        self.button5 = tk.Button(self.root, width=8, height=4, text="5", command=lambda: self.operation("5"))
        self.button5.grid(row=2, column=1)

        self.button6 = tk.Button(self.root, width=8, height=4, text="6", command=lambda: self.operation("6"))
        self.button6.grid(row=2, column=2)

        self.button7 = tk.Button(self.root, width=8, height=4, text="7", command=lambda: self.operation("7"))
        self.button7.grid(row=1, column=0)

        self.button8 = tk.Button(self.root, width=8, height=4, text="8", command=lambda: self.operation("8"))
        self.button8.grid(row=1, column=1)

        self.button9 = tk.Button(self.root, width=8, height=4, text="9", command=lambda: self.operation("9"))
        self.button9.grid(row=1, column=2)

        self.button0 = tk.Button(self.root, width=8, height=4, text="0", command=lambda: self.operation("0"))
        self.button0.grid(row=4, column=0)

        self.buttonSum = tk.Button(self.root, width=8, height=4, text="+", command=lambda: self.operation("+"))
        self.buttonSum.grid(row=1, column=3)

        self.buttonSubt = tk.Button(self.root, width=8, height=4, text="-", command=lambda: self.operation("-"))
        self.buttonSubt.grid(row=2, column=3)

        self.buttonProd = tk.Button(self.root, width=8, height=4, text="*", command=lambda: self.operation("*"))
        self.buttonProd.grid(row=3, column=3)

        self.buttonDiv = tk.Button(self.root, width=8, height=4, text="/", command=lambda: self.operation("/"))
        self.buttonDiv.grid(row=4, column=3)

        self.buttonEqual = tk.Button(self.root, width=32, height=4, text="=", command=self.resolve)
        self.buttonEqual.grid(row=5, columnspan=4, pady=5)

        self.buttonClear = tk.Button(self.root, width=8, height=4, text="C", command=self.clear)
        self.buttonClear.grid(row=4, column=2)

        self.buttonPoint = tk.Button(self.root, width=8, height=4, text=".", command=lambda: self.operation("."))
        self.buttonPoint.grid(row=4, column=1)

    def createScreen(self):
        #Create two variables, "output" is what will be shown and "currentOperation" the operation that is currently being written
        self.output = tk.StringVar()
        self.currentOperation = ""
        #Create the screen with all its parameters
        self.screen = tk.Entry(self.root, width=16, font=("arial", 24), state="readonly", textvariable=self.output)
        self.screen.grid(row=0, columnspan=4, padx=5, pady=5)
    
    def operation(self, number):
        #Add the new inputted number into a string while this string is shown in the screen
        self.currentOperation += number
        self.output.set(self.currentOperation)
    
    def resolve(self):
        #Convert the string into a real operation with "eval()" (other things are to check if it is an integer remove the ".0")
        try:
            if int(eval(self.currentOperation)) == float(eval(self.currentOperation)):
                    self.currentOperation = str(int(eval(self.currentOperation)))
            else:
                self.currentOperation = str(eval(self.currentOperation))

            self.output.set(self.currentOperation)
        #If the operation has syntax or logic error print this in the screen
        except:
            self.output.set("Error")

    def clear(self):
        #Clear the screen and the current operation
        self.currentOperation = ""
        self.output.set("")

#Call the class to execute it
Calculator()
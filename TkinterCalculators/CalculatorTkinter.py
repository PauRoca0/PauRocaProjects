import tkinter as tk

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.minsize(292, 398)
        self.root.maxsize(292, 398)

        self.createButtons()
        self.createOutput()

        self.root.mainloop()
    
    def createButtons(self):
        self.buttonPoint = tk.Button(self.root, width=8, height=4, text=".", command= lambda: self.currentNum("."))
        self.buttonPoint.grid(row=4, column=1)

        self.buttonClear = tk.Button(self.root, width=8, height=4, text="C", command= lambda: self.clear())
        self.buttonClear.grid(row=4, column=2)


        self.buttonSum = tk.Button(self.root, width=8, height=4, text="+", command= lambda: self.sum())
        self.buttonSum.grid(row=1, column=3)

        self.buttonSubt = tk.Button(self.root, width=8, height=4, text="-", command= lambda: self.subt())
        self.buttonSubt.grid(row=2, column=3)

        self.buttonProd = tk.Button(self.root, width=8, height=4, text="*", command= lambda: self.prod())
        self.buttonProd.grid(row=3, column=3)

        self.buttonDiv = tk.Button(self.root, width=8, height=4, text="/", command= lambda: self.div())
        self.buttonDiv.grid(row=4, column=3)

        self.buttonEqual = tk.Button(self.root, width=39, height=4, text="=", command= lambda: self.equal(True))
        self.buttonEqual.grid(row=5, columnspan=4)


        self.button0 = tk.Button(self.root, width=8, height=4, text="0", command= lambda: self.currentNum(0))
        self.button0.grid(row=4, column=0)

        self.button1 = tk.Button(self.root, width=8, height=4, text="1", command= lambda: self.currentNum(1))
        self.button1.grid(row=3, column=0)

        self.button2 = tk.Button(self.root, width=8, height=4, text="2", command= lambda: self.currentNum(2))
        self.button2.grid(row=3, column=1)

        self.button3 = tk.Button(self.root, width=8, height=4, text="3", command= lambda: self.currentNum(3))
        self.button3.grid(row=3, column=2)

        self.button4 = tk.Button(self.root, width=8, height=4, text="4", command= lambda: self.currentNum(4))
        self.button4.grid(row=2, column=0)

        self.button5 = tk.Button(self.root, width=8, height=4, text="5", command= lambda: self.currentNum(5))
        self.button5.grid(row=2, column=1)

        self.button6 = tk.Button(self.root, width=8, height=4, text="6", command= lambda: self.currentNum(6))
        self.button6.grid(row=2, column=2)

        self.button7 = tk.Button(self.root, width=8, height=4, text="7", command= lambda: self.currentNum(7))
        self.button7.grid(row=1, column=0)

        self.button8 = tk.Button(self.root, width=8, height=4, text="8", command= lambda: self.currentNum(8))
        self.button8.grid(row=1, column=1)

        self.button9 = tk.Button(self.root, width=8, height=4, text="9", command= lambda: self.currentNum(9))
        self.button9.grid(row=1, column=2)

    def createOutput(self):
        self.output = tk.StringVar()
        self.outputNumber = ""
        self.currentOperation = None
        self.sumState = False
        self.subtState = False
        self.prodState = False
        self.divState = False
        
        self.outputEntry = tk.Entry(self.root, width=16, font=("arial", 24), state="readonly", textvariable=self.output)
        self.outputEntry.grid(row=0, columnspan=4)

    def currentNum(self, number):

        self.outputNumber += str(number)
        self.output.set(self.outputNumber)

    def clear(self):
        self.currentOperation = None
        self.outputNumber = ""
        self.output.set("")

    def sum(self):
        self.output.set("")

        if self.outputNumber != "":
            if self.currentOperation == None:
                self.currentOperation = float(self.outputNumber)
            else:
                self.equal(False)
        
        self.sumState = True
        self.subtState = False
        self.prodState = False
        self.divState = False
        self.outputNumber = ""

    def subt(self):
        self.output.set("")

        if self.outputNumber != "":
            if self.currentOperation == None:
                self.currentOperation = float(self.outputNumber)
            else:
                self.equal(False)
        
        self.sumState = False
        self.subtState = True
        self.prodState = False
        self.divState = False
        self.outputNumber = ""

    def prod(self):
        self.output.set("")

        if self.outputNumber != "":
            if self.currentOperation == None:
                self.currentOperation = float(self.outputNumber)
            else:
                self.equal(False)

        self.sumState = False
        self.subtState = False
        self.prodState = True
        self.divState = False
        self.outputNumber = ""

    def div(self):
        self.output.set("")

        if self.outputNumber != "":
            if self.currentOperation == None:
                self.currentOperation = float(self.outputNumber)
            else:
                self.equal(False)
        
        self.sumState = False
        self.subtState = False
        self.prodState = False
        self.divState = True
        self.outputNumber = ""

    def equal(self, equalState):
        if self.currentOperation != None:
            if self.sumState:
                self.currentOperation += float(self.outputNumber)

            elif self.subtState:
                self.currentOperation -= float(self.outputNumber)

            elif self.prodState:
                self.currentOperation *= float(self.outputNumber)

            elif self.divState:
                self.currentOperation /= float(self.outputNumber)

            if equalState:
                    if self.currentOperation == int(self.currentOperation):
                        self.output.set(int(self.currentOperation))
                    else:
                        self.output.set(self.currentOperation)
                    self.sumState = False
                    self.subtState = False
                    self.prodState = False
                    self.divState = False

Calculator()
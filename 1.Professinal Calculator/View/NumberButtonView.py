import customtkinter as ctk
from Widget.Button.GeneralCalculatorButton import CalculatorButton
from Widget.Button.MiscellaneousButton.ComputeButton import ComputeButton


class NumberButtonView(ctk.CTkFrame):
    def __init__(self, parentContainer):
        super().__init__(parentContainer, width=400, height=140)
        self.paddingBetweenGridCells = 3
        self.grid_propagate(False)
        self.grid_columnconfigure(
            (1, 2, 3, 4, 5), weight=1, pad=self.paddingBetweenGridCells)
        self.rowconfigure((1, 2, 3, 4), weight=1,
                          pad=self.paddingBetweenGridCells)

        # Row 1
        btn7 = CalculatorButton(parentContainer=self, symbol='7')
        btn8 = CalculatorButton(parentContainer=self, symbol='8')
        btn9 = CalculatorButton(parentContainer=self, symbol='9')
        leftPar = CalculatorButton(parentContainer=self, symbol='(')
        rightPar = CalculatorButton(parentContainer=self, symbol=')')
        btn7.grid(column=1, row=1)
        btn8.grid(column=2, row=1)
        btn9.grid(column=3, row=1)
        leftPar.grid(column=4, row=1)
        rightPar.grid(column=5, row=1)

        # Row 2
        btn4 = CalculatorButton(parentContainer=self, symbol='4')
        btn5 = CalculatorButton(parentContainer=self, symbol='5')
        btn6 = CalculatorButton(parentContainer=self, symbol='6')
        btnMult = CalculatorButton(parentContainer=self, symbol='*')
        btnDiv = CalculatorButton(parentContainer=self, symbol='/')
        btn4.grid(column=1, row=2)
        btn5.grid(column=2, row=2)
        btn6.grid(column=3, row=2)
        btnMult.grid(column=4, row=2)
        btnDiv.grid(column=5, row=2)

        # Row 3
        btn1 = CalculatorButton(parentContainer=self, symbol='1')
        btn2 = CalculatorButton(parentContainer=self, symbol='2')
        btn3 = CalculatorButton(parentContainer=self, symbol='3')
        btnAdd = CalculatorButton(parentContainer=self, symbol='+')
        btnMinus = CalculatorButton(parentContainer=self, symbol='-')
        btn1.grid(column=1, row=3)
        btn2.grid(column=2, row=3)
        btn3.grid(column=3, row=3)
        btnAdd.grid(column=4, row=3)
        btnMinus.grid(column=5, row=3)

        # Row 4
        btn0 = CalculatorButton(parentContainer=self, symbol='0')
        btnDot = CalculatorButton(parentContainer=self, symbol='.')
        btnInverse = CalculatorButton(
            parentContainer=self, symbol='-')
        btnCompute = ComputeButton(parentContainer=self, symbol='=')

        btn0.grid(column=1, row=4)
        btnDot.grid(column=2, row=4)
        btnInverse.grid(column=3, row=4)
        btnCompute.grid(column=4, row=4, columnspan=2)

import customtkinter as ctk
import tkinter as tk
from EventManager import EventManager, PossibleEvents
from Error.InvalidInputError import InvalidInputError
from Error.ErrorMessages import ErrorMessages


class EquationEntry(ctk.CTkEntry):
    def __init__(self, parentContainer, width, height, textVariable, font):
        self.currentValue = textVariable
        super().__init__(master=parentContainer, width=width,
                         height=height, textvariable=self.currentValue, font=font)

        EventManager.Register(
            PossibleEvents.CALCULATOR_BUTTON_ISPRESSED, self.printButtonSymbol)

    def printButtonSymbol(self, symbol):
        oldValue = self.currentValue.get()
        self.currentValue.set(f'{oldValue}{symbol}')


class ResultEntry(ctk.CTkEntry):
    functionDictionary = {}

    def __init__(self, parentContainer, width, height, textVariable, font):
        self.currentValue = textVariable
        self.result = tk.StringVar()
        super().__init__(master=parentContainer, width=width,
                         height=height, textvariable=self.result, font=font, state="disabled")

        EventManager.Register(
            PossibleEvents.FUNCTION_BUTTON_ISCREATED, self.addFunctionDefinition)

        EventManager.Register(
            PossibleEvents.COMPUTE_BUTTON_ISPRESSED, self.parseInput)

    def addFunctionDefinition(self, symbol, computeFunction):
        ResultEntry.functionDictionary[symbol] = computeFunction

    def handleException(self, e):
        self.result.set(e)

    def parseInput(self):
        err = None
        try:
            result = eval(self.currentValue.get(),
                          ResultEntry.functionDictionary)
            self.result.set(result)
        except InvalidInputError as e:
            self.handleException(e)
        except SyntaxError as e:
            self.handleException(
                'Invalid characters or unclosed parentheses were used!')
        except Exception as e:
            self.handleException('Something went wrong. Verify your input!')


class OutputView(ctk.CTkFrame):
    width = 400
    height = 80

    def __init__(self, parentContainer):
        super().__init__(master=parentContainer,
                         width=self.width, height=self.height)
        self.pack_propagate(False)

        self.font = ("Roboto", 20)
        self.currentInput = tk.StringVar()

        EventManager.Register(
            PossibleEvents.CLEAR_BUTTON_ISPRESSED, self.clearInput)

        self.equationEntry = EquationEntry(
            parentContainer=self, width=OutputView.width, height=OutputView.height/2, textVariable=self.currentInput, font=self.font)
        self.equationEntry.pack()

        self.resultEntry = ResultEntry(
            parentContainer=self, width=OutputView.width, height=OutputView.height/2, textVariable=self.currentInput, font=self.font)
        self.resultEntry.pack()

    def clearInput(self):
        self.equationEntry.delete(0, 'end')

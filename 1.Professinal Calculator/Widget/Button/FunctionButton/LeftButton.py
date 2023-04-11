import keyboard
from Widget.Button.GeneralCalculatorButton import CalculatorButton
from EventManager import EventManager, PossibleEvents


class LeftButton(CalculatorButton): 
        def __init__(self, parentContainer, symbol):
            super().__init__(parentContainer, symbol)
            
        def onClick(self):
            EventManager.Register(
            PossibleEvents.CALCULATOR_BUTTON_ISPRESSED, keyboard.press("left"))
    
            
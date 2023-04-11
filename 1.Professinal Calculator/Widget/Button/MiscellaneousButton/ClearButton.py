from EventManager import EventManager, PossibleEvents
from Widget.Button.GeneralCalculatorButton import CalculatorButton


class ClearButton(CalculatorButton):
    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)
        self.configure(width=154)

    def onClick(self):
        EventManager.Notify(PossibleEvents.CLEAR_BUTTON_ISPRESSED)

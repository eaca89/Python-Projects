from EventManager import EventManager, PossibleEvents
from Widget.Button.GeneralCalculatorButton import CalculatorButton


class ComputeButton(CalculatorButton):
    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)
        self.configure(width=154)

    def onClick(self):
        EventManager.Notify(PossibleEvents.COMPUTE_BUTTON_ISPRESSED)

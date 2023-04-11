import customtkinter as ctk
from EventManager import EventManager, PossibleEvents


class ModeButtonView(ctk.CTkFrame):
    def __init__(self, parentContainer):
        super().__init__(parentContainer, width=400, height=32)
        self.grid_propagate(False)
        self.columnconfigure((1, 2), weight=1)
        self.rowconfigure(1, weight=1)

        currentMode = ctk.StringVar(value="radian")

        radianButton = ctk.CTkRadioButton(
            master=self, text="Radian", variable=currentMode, value='radian',
            command=lambda: EventManager.Notify(
                PossibleEvents.RADIAN_BUTTON_ISPRESSED))
        radianButton.grid(column=1, row=1)

        degreeButton = ctk.CTkRadioButton(
            master=self, text="Degree", variable=currentMode, value='degree',
            command=lambda: EventManager.Notify(
                PossibleEvents.DEGREE_BUTTON_ISPRESSED)
        )

        degreeButton.grid(column=2, row=1)

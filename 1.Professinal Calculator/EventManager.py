from enum import Enum, auto


class PossibleEvents(Enum):
    CLEAR_BUTTON_ISPRESSED = auto()
    CALCULATOR_BUTTON_ISPRESSED = auto()
    FUNCTION_BUTTON_ISCREATED = auto()
    EQUATION_ENTRY_ISUPDATED = auto()
    COMPUTE_BUTTON_ISPRESSED = auto()
    DEGREE_BUTTON_ISPRESSED = auto()
    RADIAN_BUTTON_ISPRESSED = auto()


class EventManager:

    events = {}

    @classmethod
    def Register(cls, event, functionToExecute):
        if not (event in cls.events.keys()):
            cls.events[event] = []

        cls.events[event].append(functionToExecute)

    @classmethod
    def Notify(cls, event, **params):
        if event in cls.events.keys():
            for function in cls.events[event]:
                function(**params)

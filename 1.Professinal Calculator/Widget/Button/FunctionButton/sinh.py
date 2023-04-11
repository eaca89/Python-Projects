from Widget.Button.GeneralCalculatorButton import CalculatorFunctionButton
from Error.InvalidInputError import InvalidInputError
from Error.ErrorMessages import ErrorMessages
from OurMathClass import OurMathClass
from EventManager import EventManager, PossibleEvents


class SinhButton(CalculatorFunctionButton):
    # input is radians by default
    isInputInDegree = False

    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)
    EventManager.Register(PossibleEvents.RADIAN_BUTTON_ISPRESSED,
                          lambda: SinhButton.setIsInputInDegree(False))

    EventManager.Register(PossibleEvents.DEGREE_BUTTON_ISPRESSED,
                          lambda: SinhButton.setIsInputInDegree(True))

    """
    Compute the hyperbolic sine of x using the formula (e^x - e^(-x)) / 2
    Args: x is a number in radians
    Returns: The hyperbolic sine of x
    """

    @staticmethod
    def setIsInputInDegree(value):
        # Set the input mode to radians or degrees
        SinhButton.isInputInDegree = value

    def sinh(x):
        if SinhButton.isInputInDegree:
            # Convert the input from degrees to radians if necessary
            x = OurMathClass.degreeToRadian(x)
        # Compute the hyperbolic sine using the formula (e^x - e^-x) / 2
        return (OurMathClass.MyEulerConstant**x - OurMathClass.MyEulerConstant**(-x)) / 2

    # Checks that an argument is provided
    def compute(self, *args):
        if len(args) == 0:
            raise InvalidInputError("Error! No Input Found")
        if (len(args) > 1):
            raise InvalidInputError("Error! More Than 1 Parameter Given")

        x = args[0]
        try:
            # Convert the input to a float
            x = float(x)
        except ValueError:
            # Raise an exception if the input is not a valid number
            raise InvalidInputError("Error! Invalid Input")

        # Compute the hyperbolic sine of the input using the static method
        result = SinhButton.sinh(x)
        return result

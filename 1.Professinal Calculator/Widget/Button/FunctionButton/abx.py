# Import packages
from Widget.Button.GeneralCalculatorButton import CalculatorFunctionButton
from Error.InvalidInputError import InvalidInputError
from Error.ErrorMessages import ErrorMessages

#


class abxButton(CalculatorFunctionButton):

    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)


# IMPLEMENT WITG *ARGS INSTEAD

    def compute(self, *args):

        if (len(args) != 3):
            raise InvalidInputError(
                ErrorMessages["Functions"]["abx_input"]["InvalidInput"]
            )

        a = args[0]
        b = args[1]
        x = args[2]

        # Verify input
        if (a == 0) or (not isinstance(a, (int, float))):
            raise InvalidInputError(
                ErrorMessages["Functions"]["abx_a"]["InvalidInputOf0"]
            )

        if (b == 1) or (not isinstance(b, (int, float))):
            raise InvalidInputError(
                ErrorMessages["Functions"]["abx_b"]["InvalidInputOf1"]
            )

        if (b == 0) and (x == 0):
            raise InvalidInputError(
                ErrorMessages["Functions"]["abx_bx"]["InvalidPower0"]
            )

        if not isinstance(x, (int, float)):
            raise InvalidInputError(
                ErrorMessages["Functions"]["General"])

        return (a*(b**x))

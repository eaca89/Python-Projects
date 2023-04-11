from Widget.Button.GeneralCalculatorButton import CalculatorFunctionButton
from Error.InvalidInputError import InvalidInputError
from Error.ErrorMessages import ErrorMessages
from OurMathClass import OurMathClass


class LogButton(CalculatorFunctionButton):
    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)

    def compute(self, *args):
        # Error checking
        if (len(args) == 0):
            raise InvalidInputError(
                ErrorMessages["Functions"]["Log"]["NoParameterGiven"])
        if (len(args) > 2):
            raise InvalidInputError(
                ErrorMessages["Functions"]["Log"]["InvalidNumberOfParameters"])
        
        x = args[0]
        base = 10
        if (x <= 0 or base <= 0):
            raise InvalidInputError(
                ErrorMessages["Functions"]["Log"]["InvalidInputOfNotPositive"])
        
        if (len(args) == 2):
            base = args[1]
        output = self.logarithm(x, base)

        #10 decimal places
        return round(output, 10)
        
    def logarithm(self, x, base):    
        # Define epsilon for accuracy
        epsilon = 1e-10

        # Initialize variables for binary search
        lowerBound = 0
        upperBound = x
        result = 0.0

        # Perform binary search
        while abs(x - OurMathClass.power(base, result)) > epsilon:
            mid = (lowerBound + upperBound) / 2
            mid_result = OurMathClass.power(base, mid)
            if mid_result < x:
                lowerBound = mid
            else:
                upperBound = mid
            result = mid

        return result
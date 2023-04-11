from Widget.Button.GeneralCalculatorButton import CalculatorFunctionButton
from Error.InvalidInputError import InvalidInputError
from Error.ErrorMessages import ErrorMessages


class MADButton(CalculatorFunctionButton):
    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)

    def mean(self, arr):
        n = len(arr)
        return sum(arr)/n

    def myabs(self, arg):
        if arg >= 0:
            return arg
        else:
            return -1 * arg

    def compute(self, *data):
        m = self.mean(list(data))
        deviations = [self.myabs(x - m) for x in list(data)]
        return self.mean(deviations)

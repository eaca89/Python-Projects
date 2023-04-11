from Widget.Button.GeneralCalculatorButton import CalculatorFunctionButton
from Error.InvalidInputError import InvalidInputError
from Error.ErrorMessages import ErrorMessages


class ExponentButton(CalculatorFunctionButton):

    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)

    @staticmethod
    def ourPower(base, power):
        result = 1
        negativeExponent = False
        if power % 1 != 0:
            return base**power
        if power < 0:
            negativeExponent = True
            power = power*(-1)
        while power > 0:
            if power % 2 == 0:
                power = power // 2
                base = base * base
            else:
                power = power - 1
                result = result * base

                power = power // 2
                base = base * base
        if negativeExponent == True:
            return 1/result
        return result

    def compute(self, base, power):
        result = 1
        negativeExponent = False
        if power % 1 != 0:
            return base**power
        if power < 0:
            negativeExponent = True
            power = power*(-1)
        while power > 0:
            if power % 2 == 0:
                power = power // 2
                base = base * base
            else:
                power = power - 1
                result = result * base

                power = power // 2
                base = base * base
        if negativeExponent == True:
            return round((1/result), 9)
        return round(result, 9)

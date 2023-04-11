from Widget.Button.GeneralCalculatorButton import CalculatorFunctionButton
from Error.InvalidInputError import InvalidInputError
from Error.ErrorMessages import ErrorMessages
from OurMathClass import OurMathClass
from EventManager import EventManager, PossibleEvents


class AcosButton(CalculatorFunctionButton):
    # Set of points that we already know the value with certainty
    # Will be used as center for taylor approximation
    isInputInDegree = False

    taylorAppCenters = [
        (-0.8660254037844386, 5*OurMathClass.pi/6),
        (-0.7071067811865476, 3*OurMathClass.pi/4),
        (-0.5, 2*OurMathClass.pi/3),
        (0, OurMathClass.pi/2),
        (0.5, OurMathClass.pi/3),
        (0.7071067811865476, OurMathClass.pi/4),
        (0.8660254037844386, OurMathClass.pi/6),
    ]

    acosDomainExtremityPoints = {
        1: 0,
        -1: OurMathClass.pi,
    }

    # correspond to finding a center for the taylor app to the given input at distance<=1/10**5
    precisionOfComputation = 5

    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)
        EventManager.Register(PossibleEvents.RADIAN_BUTTON_ISPRESSED,
                              lambda: AcosButton.setIsInputInDegree(False))

        EventManager.Register(PossibleEvents.DEGREE_BUTTON_ISPRESSED,
                              lambda: AcosButton.setIsInputInDegree(True))

    def compute(self, *args):
        if (len(args) == 0):
            raise InvalidInputError(
                ErrorMessages["Functions"]["Acos"]["NoParameterGiven"])

        if (len(args) > 1):
            raise InvalidInputError(
                ErrorMessages["Functions"]["Acos"]["MoreThan1ParameterGiven"])

        x = args[0]

        if (abs(x) > 1):
            raise InvalidInputError(
                ErrorMessages["Functions"]["Acos"]["InputOutsideDomain"])

        roundedValueInput = round(x, AcosButton.precisionOfComputation)
        if (abs(roundedValueInput) == 1):
            output = AcosButton.acosDomainExtremityPoints[roundedValueInput]
            if (AcosButton.isInputInDegree):
                output = OurMathClass.radianToDegree(output)
            return output

        output = self.repetitiveTaylorAcos(
            x, AcosButton.precisionOfComputation)

        if (AcosButton.isInputInDegree):
            output = OurMathClass.radianToDegree(output)

        return output

    def taylorAcos(self, initialValue, c, x):
        return initialValue - (1/(OurMathClass.power((-(OurMathClass.power(c, 2)) + 1), 1/2)))*(x-c) - (1/2)*(c/(OurMathClass.power((-(OurMathClass.power(c, 2)) + 1), (3/2))))*OurMathClass.power((x-c), 2)

    def findClosestCenterToTheInput(self, x):
        # find the closest center to the given input
        selectedTupple = tuple()
        for (c, initialValue) in AcosButton.taylorAppCenters:
            if (len(selectedTupple) == 0):
                selectedTupple = (c, initialValue)
            else:
                distanceInputCurrentCenter = abs(x - selectedTupple[0])
                distanceInputPotentialCenter = abs(x - c)
                if (distanceInputPotentialCenter < distanceInputCurrentCenter):
                    selectedTupple = (c, initialValue)

        return selectedTupple

    def repetitiveTaylorAcos(self, x, precision):
        # find closest known points (initial center for taylor app.) to the given input
        (center, initialValue) = self.findClosestCenterToTheInput(x)
        # find the closest point at a distance < 10^-precision from the input
        # with this point compute the value of the given input
        distance = round(abs(center-x), precision)
        counter = 0
        step = 1/(10**precision)
        if (x >= center):
            # if x >= center it means that center must tend to x by increasing center
            while (counter < distance):
                counter = counter + step
                initialValue = self.taylorAcos(
                    initialValue, center, round(center + step, precision))
                center = round(center + step, precision)
        else:
            # if x < center it means that center must tend to x by decreasing center
            while (counter < distance):
                counter = counter + step
                initialValue = self.taylorAcos(
                    initialValue, center, round(center - step, precision))
                center = round(center - step, precision)

        return self.taylorAcos(initialValue, center, x)

    @classmethod
    def setIsInputInDegree(cls, state):
        cls.isInputInDegree = state

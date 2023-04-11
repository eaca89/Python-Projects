from Widget.Button.GeneralCalculatorButton import CalculatorFunctionButton
from Error.InvalidInputError import InvalidInputError
from Error.ErrorMessages import ErrorMessages
"""
Algorithm to calculate standard deviation is as follows:
1) calculate mean of list of numbers
2) for each element in list: subtract the element from the mean, then square the result 
3) calculate mean of result from #2
4) calculate square root of #3

"""
# python -m pipenv shell    -- launch shell to run program
# pipenv run python ./app.py -- run program
class stdevButton(CalculatorFunctionButton):
    def __init__(self, parentContainer, symbol):
        super().__init__(parentContainer, symbol)
    
    def compute(self, *args):     
        n = len(args)
        sum = 0
        sd = 0.0

          
    # 1 or fewer numbers in list means standard dev is 0. Ask user to input larger sample.
        if (n <= 1):
            raise InvalidInputError(
                ErrorMessages["Functions"]["Stdev"]["InvalidInputSmallList"])

        for element in args:
            sum += float(element)
        
    # step 1
        mean = sum / n

    # steps 2 and 3
        for element in args:
         sd += (float(element) - mean) * (float(element) - mean)

    # step 4
        sd = (sd / float(n - 1)) ** (1/2)  

        return sd


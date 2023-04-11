import math
from Widget.Button.FunctionButton.Exponent import ExponentButton

# This class will try to replace the method we use
# in our method for diverse computation [not the calculator itself]
# instead of calling the regular math.<something> you will use OurMathClass.<something>
# if no implementation for the method you want to use is available:
# 1.create a field in the OurMathClass for the method you want
# 2. Make it point to the regular math.<something>
# 3. When we have an implementation for the math.<something> we will replace it in this class.


class OurMathClass:
    power = ExponentButton.ourPower
    pi = math.pi
    radianToDegree = math.degrees
    MyEulerConstant = math.e
    degreeToRadian = math.radians

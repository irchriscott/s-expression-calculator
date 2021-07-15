import sys
from typing import Any
from functools import reduce

class SExpressionCalculator:
    
    def __init__(self, expr: str) -> None:
        self.expression = expr
        self.calculated = {}

    def calculate(self) -> Any:
        """Calculate the expression then return the result"""
        while ')' in self.expression:
            # Check check if already been calculated
            if self.expression in self.calculated:
                return self.calculated[self.expression]

            # Get the index of the closing expression (')') then opening ('(')
            r_index = self.expression.index(')')
            l_index = self.expression[:r_index].rindex('(')

            # Evaluate the expression and return its result
            try:
                value = self.__evaluate_single_expression(self.expression[l_index + 1:r_index])
            except ValueError as e:
                return "Error : " + str(e)

            # Check if the value is a string => Error
            if isinstance(value, str): return value

            # If it is the last expression, return the value. 
            # Otherwise, replace the single expression by its value in the expression.
            if l_index == 0: return value
            else:
                self.expression = self.expression[:l_index] + str(value) + self.expression[r_index + 1:]

        # Return the expression results or the error if the expression was malformed
        return int(self.expression) if self.expression.isdigit() \
                        else "Error : malformed expression\nHint : use double-quotes (\") instead of single quotes (')"

    def __evaluate_single_expression(self, expr: str) -> Any:
        """Evaluate a single expression"""

        # If the expression has already been calculated, return its value
        if expr in self.calculated:
            return self.calculated[expr]

        values = expr.split()

        # It is presumed that the first item is the function name and the rest are the numbers
        if not values[0].isdigit():
            if values[0] == 'add':
                result = self.__sum__(values[1:])
            elif values[0] == 'multiply':
                result = self.__mult__(values[1:])
            elif values[0] == 'exponent':
                result = self.__exp__(values[1:])
            else:
                return f"Error : function <{values[0]}> not supported"
        else:
            result = int(expr)

        # Add the result of the expression into a dict
        self.calculated[expr] = result

        return result

    def __sum__(self, nums: list[str]) -> int:
        """Sum a single expression"""
        return sum(map(lambda x: int(x), nums))

    def __mult__(self, nums: list[str]) -> int:
        """Multiply a single expression"""
        return reduce((lambda x, y: x * y), map(lambda x: int(x), nums))

    def __exp__(self, nums: list[str]) -> int:
        """Exponents of single expression"""
        return reduce((lambda x, y: x ** y), map(lambda x: int(x), nums))         


if __name__ == '__main__':
    calculator = SExpressionCalculator(sys.argv[1])
    print(calculator.calculate())
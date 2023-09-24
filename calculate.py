import re

class operator:
    def addition(self,x,y):
        return x + y
    
    def subtraction(self,x,y):
        return x - y
    
    def multiplication(self,x,y):
        return x * y
    
    def division(self,x,y):
        return x / y
    
    def remainder(self,x,y):
        return x % y
    
    def powerOf(self,x,y):
        return x ** y
    def divisor(self,x,y):
        return x//y

class expresoinCalculator(operator):
    def xor(self,a,b):
        return bool((a and not b) or (b and not a))

    def stringToNumber(self,numberMatch,string:str):
        if numberMatch.group(2):
            return float(string)
        return int(string)


    def parseParentheses(self,string:str):
        ifLeftParentheses = string[0] == "("
        ifRightParentheses = string[-1] == ")"

        parenthesesSyntaxError = self.xor(ifLeftParentheses,ifRightParentheses)

        haveParentheses = ifLeftParentheses and ifRightParentheses

        if parenthesesSyntaxError:
            raise Exception("syntax error:unexpected parentheses ->"+string)
        if haveParentheses:
            return self.parseString(string[1:-1])
        return None

    def parseMultiplicationDivisoinRemainder(self,string:str):
        match = re.match(r"\s*(.+?)(\*|\/\/|\/|%)(.+)",string)
        ifmultiplication = match and match.group(2) == "*"
        ifdivision = match and match.group(2) == "/"
        ifremainder = match and match.group(2) == "%"
        ifdivisor = match and match.group(2) == "//"
        if match and ifmultiplication:
            left = self.parseString(match.group(1))
            right = self.parseString(match.group(3))
            return self.multiplication(left,right)
        if match and ifdivision:
            left = self.parseString(match.group(1))
            right = self.parseString(match.group(3))
            return self.division(left,right)
        if match and ifremainder:
            left = self.parseString(match.group(1))
            right = self.parseString(match.group(3))
            return self.remainder(left,right)
        if match and ifdivisor:
            left = self.parseString(match.group(1))
            right = self.parseString(match.group(3))
            return self.divisor(left,right)
        return None

    def parseAdditionAndSubtraction(self,string:str):

        match = re.match(r"\s*(.*?)(\+|\-)(.+)",string)
        isAddition = match and match.group(2) == "+" and match.group(1) and match.group(2)
        isSubtraction = match and match.group(2) == "-" and match.group(1) and match.group(2)
        isPositive = match and match.group(2) == "+" and (not match.group(1)) and match.group(2)
        isNegative = match and match.group(2) == "-" and (not match.group(1)) and match.group(2)
        if match and isAddition:

            left = self.parseString(match.group(1))
            right = self.parseString(match.group(3))
            return self.addition(left,right)

        if match and isSubtraction:
            left = self.parseString(match.group(1))
            right = self.parseString(match.group(3))
            return self.subtraction(left,right) 

        if match and isPositive:

            return self.parseString(match.group(3))
        if match and isNegative:
            return -1 * self.parseString(match.group(3))
        return None


    def parseNumber(self,string:str):
        match = re.match(r"\s*(\d+)(\.\d+)?\s*$",string)
        """
        12355.1234
        numberMatch.group(1):Interger part -> 12355
        numberMatch.group(2):Float Part -> .1234
        """
        if match:
            return self.stringToNumber(match,string)
        else:
            raise Exception("syntax error:the number \""+string+"\" is unexpected")

    def parseString(self,string):
        stack = [
                self.parseParentheses,
                self.parseMultiplicationDivisoinRemainder,
                self.parseAdditionAndSubtraction,
                ]
        for func in stack:
            if func(string) != None:
                return func(string)
        return self.parseNumber(string)

    def __init__(self,string:str):
        self.result = self.parseString(string)

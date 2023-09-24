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

class expresoinCalculator(operator):
    def xor(self,a,b):
        return bool((a and not b) or (b and not a))

    def stringToNumber(self,numberMatch,string:str):
        if numberMatch.group(2):
            return float(string)
        return int(string)

    def calculateString(self,string):

        ifLeftParentheses = string[0] == "("
        ifRightParentheses = string[-1] == ")"

        parenthesesSyntaxError = self.xor(ifLeftParentheses,ifRightParentheses)

        haveParentheses = ifLeftParentheses and ifRightParentheses

        if parenthesesSyntaxError:
            raise Exception("syntax error:unexpected parentheses ->"+string)
        if haveParentheses:
            return self.calculateString(string[1:-1])
             



        additionMatch = re.match(r"\s*(.*?)?(\+|\-)(.*)",string)
        isAddition = additionMatch and additionMatch.group(2) == "+" and additionMatch.group(1) and additionMatch.group(2)
        isSubtraction = additionMatch and additionMatch.group(2) == "-" and additionMatch.group(1) and additionMatch.group(2)
        isPositive = additionMatch and additionMatch.group(2) == "+" and (not additionMatch.group(1)) and additionMatch.group(2)
        isNegative = additionMatch and additionMatch.group(2) == "-" and (not additionMatch.group(1)) and additionMatch.group(2)
        if additionMatch and isAddition:

            left = self.calculateString(additionMatch.group(1))
            right = self.calculateString(additionMatch.group(3))
            return self.addition(left,right)

        elif additionMatch and isSubtraction:
            left = self.calculateString(additionMatch.group(1))
            right = self.calculateString(additionMatch.group(3))
            return self.subtraction(left,right) 

        elif additionMatch and isPositive:

            return self.calculateString(additionMatch.group(3))
        elif additionMatch and isNegative:
            return -1 * self.calculateString(additionMatch.group(3))

        elif additionMatch:
            raise Exception("syntax error:the operator '+' is unexpected -> "+string)



        numberMatch = re.match(r"\s*(\d+)(\.\d+)?\s*$",string)
        """
        12355.1234
        numberMatch.group(1):Interger part -> 12355
        numberMatch.group(2):Float Part -> .1234
        """
        if numberMatch:
            return self.stringToNumber(numberMatch,string)
        else:
            raise Exception("syntax error:the number \""+string+"\" is unexpected")

    def __init__(self,string:str):
        self.result = self.calculateString(string)

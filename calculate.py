import re
from enum import Enum,unique

class Lexer:
    tokens = None
    varibles:dict[str,float|int] = {
        "TEST_VARIBLE":114514,
        "PI":3.1415926,
    }
    operators = {
        "LParentheses":4,
        "RParentheses":4,

        "neg":3,
        "pos":3,

        "pow":2,

        "mul":1,
        "truediv":1,
        "floordiv":1,
        "mod":1,

        "add":0,
        "sub":0,

    }
    def stringValueToRealValue(self,string:str):
        isVarible = string in self.varibles
        isInteger = re.match(r"\d*$",string)
        isFloat = re.match(r"\d+\.\d+$|\d+\.$|\.\d+$",string)
        result = string
        if isVarible:
            result = self.varibles[string]
        if isInteger:
            result = int(string)
        if isFloat:
            result = float(string)
        return result

    def stringOperatorToEnumOperator(self,left:str|None,between:str):
        leftIsOperator = type(left) == str and not left == ")"
        if between == '+' and (left is None or leftIsOperator):
            return "pos"
        if between == '+' and not (left is None or leftIsOperator):
            return "add"
        if between == '-' and (left is None or leftIsOperator):
            return "neg"
        if between == '-' and not (left is None or leftIsOperator):
            return "sub"
        if between == '*':
            return "mul"
        if between == "/":
            return "truediv"
        if between == "//":
            return "floordiv"
        if between == "%":
            return "mod"
        if between == "**":
            return "pow"
        return between

    def participle(self,exp:str):
        self.tokens = re.findall(test,exp)
        for i in range(len(self.tokens)):
            if i != 0:
                left = self.tokens[i-1]
            else:
                left = None
            between = self.tokens[i]

            self.tokens[i] = self.stringValueToRealValue(between)
            between = self.tokens[i]
            self.tokens[i] = self.stringOperatorToEnumOperator(left,between) 

    def __init__(self,exp:str):
        self.participle(exp)
class interpreter:
    operatorStack = []
    valueStack = []

    def test(self,tokens:list):
        return

    def __init__(self,tokens:list):
        self.tokens = tokens


class expressionCalculator():
    operatorStack = []
    valueStack = []
test = r"[a-zA-Z_]+\(|[0-9\.a-zA-Z_]+|\*\*|\/\/|[^0-9\.a-zA-Z_ ]{1}"

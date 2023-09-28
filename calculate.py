import re
from enum import Enum,unique

class operators:
    operator = {
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

class Lexer:
    tokens:list = []
    varibles:dict[str,float|int] = {
        "TEST_VARIBLE":114514,
        "PI":3.1415926,
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
class interpreter(operators):
    operatorStack:list = []
    valueStack:list = []

    def ifTokenLowerThanBefore(self,token):
        if len(self.operatorStack) == 0 or type(token) != str:
            return False
        if token == "(" or self.operatorStack[-1] == "(":#))
            return False
        if token == ")":
            return True
        if self.operatorStack[-1] == ")":
            return True
        if self.operator[token] < self.operator[self.operatorStack[-1]]:
            return True
        return False
    def calculate(self,operator):
        if operator == "pos":
            result = self.valueStack.pop()
            self.valueStack.append(result)
        if operator == "neg":
            result = -1 * self.valueStack.pop()
            self.valueStack.append(result)
        if operator == "add":
            result = self.valueStack.pop() + self.valueStack.pop()
            self.valueStack.append(result)
        if operator == "sub":
            right = self.valueStack.pop()
            left = self.valueStack.pop()
            result = left - right
            self.valueStack.append(result)
        if operator == "mul":
            result = self.valueStack.pop() * self.valueStack.pop()
            self.valueStack.append(result)
        if operator == "truediv":
            right = self.valueStack.pop()
            left = self.valueStack.pop()
            result = left / right
            self.valueStack.append(result)
        if operator == "floordiv":
            right = self.valueStack.pop()
            left = self.valueStack.pop()
            result = left // right
            self.valueStack.append(result)
        if operator == "mod":
            right = self.valueStack.pop()
            left = self.valueStack.pop()
            result = left % right
            self.valueStack.append(result)
        if operator == "pow":
            right = self.valueStack.pop()
            left = self.valueStack.pop()
            result = left ** right
            self.valueStack.append(result)
    def stackOut(self,token):
        while self.ifTokenLowerThanBefore(token):
            operator = self.operatorStack.pop()
            if operator == "(":#)
                continue
            self.calculate(operator)
        if token == ")":
            self.operatorStack.pop()
            return
        self.operatorStack.append(token)
        return

    def stackIn(self,tokens:list):
        for token in tokens:
            isValue = type(token) != str
            if isValue:
                self.valueStack.append(token)
            elif self.ifTokenLowerThanBefore(token):
                self.stackOut(token)
            else:
                self.operatorStack.append(token)
        while len(self.operatorStack) != 0:
            operator = self.operatorStack.pop()
            self.calculate(operator)
 
    def __init__(self,tokens:list):
        self.stackIn(tokens)
        self.result = self.valueStack[0]

class expressionCalculator:
    def __init__(self,exp:str):
        self.result = interpreter(Lexer(exp).tokens).result
test = r"[a-zA-Z_]+\(|[0-9\.a-zA-Z_]+|\*\*|\/\/|[^0-9\.a-zA-Z_ ]{1}"

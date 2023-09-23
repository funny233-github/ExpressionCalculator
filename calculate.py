class calculate:
    priorityList = {
        "+":2,   
        "-":2,
        "*":1,
        "/":1,
        "%":1,
        "**":0
    }

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

    def getPriority(self,char,nextChar):
        ispower        =  char == "*" and nextChar == "*"
        ismulti        =  char == "*" and nextChar != "*"
        isNum          =  char in "0123456789"
        isParentheses  =  char in "()"
        if ispower:
            return self.priorityList["**"]
        if ismulti:
            return self.priorityList["*"]
        if isNum:
            return 3
        if isParentheses:
            return 0
        return self.priorityList[char]

    def checkParentheses(self,char):
        if char == "(":
            return 1
        if char == ")":
            return -1
        return 0


    def getMaxPriorityIndex(self,string):
        transformString  = string + "#"
        parentheses      = 0
        maxPriority      = -1
        result           = 0

        i                = 0

        while i < len(transformString)-1:
            char             =  transformString[i]
            nextChar         =  transformString[i+1]

            parentheses     +=  self.checkParentheses(char)

            notInParentheses =  parentheses ==  0
            higherPriority   =  self.getPriority(char,nextChar) > maxPriority
            isNotNum         =  not (char in "0123456789")

            if notInParentheses and higherPriority and isNotNum:
                maxPriority = self.getPriority(char,nextChar)
                result      = i

            if  maxPriority == max(self.priorityList):
                return result

            ispower = char == "*" and nextChar == "*"
            if ispower:
                i += 2
            else:
                i += 1

        return result

    def pureNum(self,string):
        for i in string:
            if not(i in "0123456789"): 
                return False
        return True

    def calculateBasedOnOperator(self,operator,leftResult,rightResult):
        if operator == "+":
            return self.addition(leftResult,rightResult)
        if operator == "-":
            return self.subtraction(leftResult,rightResult)
        if operator == "*":
            return self.multiplication(leftResult,rightResult)
        if operator == "/":
            return self.division(leftResult,rightResult)
        if operator == "%":
            return self.remainder(leftResult,rightResult)
        if operator == "**":
            return self.powerOf(leftResult,rightResult)

    def getLeftResult(self,index,string):
        leftString = string[:index]
        return self.calculateString(leftString)
    
    def getRightResultAndOperator(self,index,string):
        ispower = string[index] == "*" and string[index+1] == "*"
        if ispower:
            rightstring = string[index+2:]
            operator    = "**"
        else:
            rightstring = string[index+1:]
            operator    = string[index]
        return self.calculateString(rightstring), operator

    def calculateString(self,string):

        ifInParentheses = string[0] == "(" and string[-1] == ")"
        if ifInParentheses:
            return self.calculateString(string[1:-1])

        if self.pureNum(string):
            return int(string)

        operatorIndex = self.getMaxPriorityIndex(string)


        leftResult            = self.getLeftResult(operatorIndex,string)
        rightResult, operator = self.getRightResultAndOperator(operatorIndex,string)

        return self.calculateBasedOnOperator(operator,leftResult,rightResult)

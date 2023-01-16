#A python interpreter in python!
import re
from calculator import Eval,EvaluateExpression,isValidExpression,isVariableExpression

variables = {}

printVariable = r"[A-z_][A-z0-9_]+"
setVariable = r"([A-z_][A-z0-9_]+) ?= ?(((\'|\").+(\'|\"))|(-?[0-9]+(\.[0-9])?))"

def replaceVariables(expression):
    return expression

def parseInput(exp):
    if re.match(setVariable,exp):
        expression = list(re.findall(setVariable,exp))
        variables[expression[0][0]] = expression[0][1]
        print(variables)
    elif isValidExpression(exp):
        print(EvaluateExpression(exp))
    elif isVariableExpression(exp):
        exp = replaceVariables(exp)
    elif re.match(printVariable,exp):
        expression = list(re.findall(printVariable,exp))
        try:
            print(variables[expression[0]])
        except KeyError:
            print("Variable is undefined")

while True:
    exp = input(">>> ")
    parseInput(exp)
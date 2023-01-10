### Task Description
# Task an arbitrary mathematical expression containing the operators
# +,-,*,/ each with their usual meaning
# and parentheses, including nested parentheses
# and calculate the result
# Input numbers are signed (i.e. account for negatives)
# Remember the order of operations!
### Sample
# "1*2*(1+2)" = 6
# "4*-2/1+5" = 1

## Broad Solution Desciption
# This solution follows the order of operations, firstly by eliminating
# parenthetical expressions, by replaced the expression with the value
# Once parenthetical expressions are eliminated, the final equation is evaluated
# Equations are evaluated using the Eval function, which splits the input string into
# integers and operators using regular expressions. 
# The integer list is length n, the operator list SHOULD be n-1
# Adjacent integers are then operated on (respecting OO) until no operations remain

import re
## Evaluation Function

#Evaluation Function
#This function takes an input without parentheses and evaluates the expression 
#by seperating the function into (signed) integers and operators
#The integer and operator list is reduced by performing the required operations
#Respecting the order of operations
def Eval(string):
    result = 0
    string = string.replace(" ","") #Eliminate whitespace in string to be evaluated
    numbersIdentified = list(re.findall(r"(([^0-9]\-)?[0-9]+)", string)) #Find all numbers, accounting for negatives
    numbers = [] # Create a simple list of numbers
    for i,n in enumerate(numbersIdentified):
        numbers.append(int(re.sub(r"[^0-9\-]","",n[0]))) #Convert the regexp output to a simple integer
    if(string[0] == '-'):#Account for the edge case that the first integer is negative
        numbers[0] = numbers[0]*-1
    operators = list(re.findall('\*|\/|\+|\-', string)) #Find all operators (this will include negative signs as operators)
    #Remove negative operators that are just signs
    if len(list(operators)) >= len(list(numbers)):
        for i,n in enumerate(numbers):
            if int(n) < 0:
                del operators[i]
    #Eliminate all multiplication and division operations through value subsitution
    #A nested loop is required to ensure the elimination of all multiplication and division operations
    for x in range(len(operators)):
        for i, o in enumerate(operators):
            if o == '*':
                numbers[i] = int(numbers[i])*int(numbers[i+1])
                del numbers[i+1]
                del operators[i]
            elif o == '/':
                numbers[i] = int(numbers[i])/int(numbers[i+1])
                del numbers[i+1]
                del operators[i]
    #Eliminate all addition and subtraction operations through value subsitution
    #We again used a nested loop to ensure the elimination of all operators
    for x in range(len(operators)):
        for i, o in enumerate(operators): ## Perform multiplication and division first
            if o == '+':
                numbers[i] = int(numbers[i])+int(numbers[i+1])
                del numbers[i+1]
                del operators[i]
            elif o == '-':
                numbers[i] = int(numbers[i])-int(numbers[i+1])
                del numbers[i+1]
                del operators[i]
    return numbers[0] # At the end of this process, we should have a single entry in our numbers list


#This function evaluates an arbitrary expression containing parentheses
#It first eliminates parentheses by evaluating the most inner parenthetical expression
#which it replaces with a concrete value. This process is repeated until no parentheses remain!
#Once the parentheses no longer remain, the residual expression can be evaluated using the Eval function

def EvaluateExpression(string):
    while '(' in string: #Repeat until every parenthetical expression has been replaced
        internalParentheses = list(re.findall(r"\([0-9\+\-\*\/]+\)", string)) #Find ONLY the most inner parenthetical expressions
        for i,v in enumerate(internalParentheses): #For each inner expression
            string = string.replace(v,str(Eval(v))) #Replace with a concrete value
    return Eval(string) #Return the final value

exp = input("Enter a Mathematical Expression: ")
r1 = EvaluateExpression(exp)
r2 = eval(exp)
print("Result: ",r1," (",r2,")")
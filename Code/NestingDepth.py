import sys

def solve(number):
    """
    This function solves each test case as follows:

    1) It converts the number it's given into a character array.

    2) For each digit x in the array, it adds x opening and closing parentheses 
    before and after the digits.

    3) The resulting array is cleaned by removing all intermediate pairs of ')('.

    4) The cleaned array is joined into a string for the result.
    """


    digitList = convertToList(number)  # Ex: 221 ---> ['2','2','1']

    # The 221 and ((2))((2))(1) style representation below are still character arrays

    parenthesizedList = parenthesize(digitList)  # Ex: 221 ---> ((2))((2))(1)

    cleanedList = cleanParenthesis(parenthesizedList)

    result = "".join(cleanedList)  # Convert character array into a string
    return result



def cleanParenthesis(cleanedList):
    """
    This method removes all consecutive pairs of ')' and '('.
    """


    for i in range(len(cleanedList)-2):
        if(cleanedList[i]==')' and cleanedList[i+1]=='('):
            cleanedList = cleanedList[:i]+cleanedList[i+2:]
            return cleanParenthesis(cleanedList)
    
    return cleanedList



def parenthesize(digitList):
    """
    For each digit x in the digit list, this method adds x
    parenthesis before and after the digit. It returns the new list.
    """


    parenthesizedList = []

    for x in digitList:
        parenthesizedList += ['(']*int(x) + [x] + [')']*int(x)

    return parenthesizedList




def convertToList(number):
    """
    This method converts the number string into a character array
    """


    return list(number.rstrip())




def output(case,result):
    """
    Prints the output in Case #x: y format. Where x is the case no.
    and y is the resulting string of nested digits.
    """


    print("Case #{}: {}".format(case,result))



def main():
    """
    This function reads standard input and passes data around to the 
    functions that actually solve and print the result. 
    
    It keeps track of the current test case along the way.
    """


    tCases = int(sys.stdin.readline())  # Total Test Cases
    currentTestCase = 1

    while(currentTestCase <= tCases):
        number = sys.stdin.readline()
        result = solve(number)

        output(currentTestCase,result) 

        currentTestCase+=1
main()
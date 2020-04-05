import sys

def solve(matrix,size):
    """
    This function calls the necessary functions to calculate what is needed for each 
    test case.

    It calculates the trace and the number of rows and columns containing duplicates.
    """


    trace = findTrace(matrix,size)
    duplicateRows = row_duplicates(matrix,size)
    duplicateColumns = column_duplicates(matrix,size)

    return trace,duplicateRows,duplicateColumns




def row_duplicates(matrix, size):
    """
    This function extracts one row at a time from the given
    square matrix and then checks the resulting list for duplicate values.
    """

    count = 0   # Number of rows with duplicates

    for i in range(size):
        currentRow = matrix[i]
        if(checkDuplicate(currentRow)):
            count+=1

        
    return count



def column_duplicates(matrix,size):
    """
    This function extracts one column at a time from the given
    square matrix and then checks the resulting list for duplicate values.
    """


    count = 0  # Number of columns with duplicates

    for i in range(size):
        currentColumn = []
        for j in range(size):
            currentColumn.append(matrix[j][i])

        if(checkDuplicate(currentColumn)):
            count+=1
    
    return count


    
def checkDuplicate(myList):
    """
    This function checks for duplicate values in a given Python list.
    """

    for i in range(len(myList)):
        myDict = {}  # Count occurences in a dictionary
        for x in myList:
            if x in myDict:
                return True  # If it already exists, the current x is a duplicate!
            else:
                myDict[x] = 1
    return False



def findTrace(matrix,size):
    """
    This function calculates the trace of a natural latin square.
    """

    trace = 0

    for i in range(size):
        for j in range(size):
            if i==j:
                trace = trace + int(matrix[i][j])
    
    return trace



def output(case, trace, duplicateRows, duplicateColumns):
    """
    Prints the output in Case #x: a b c format. Where x is the case no.,
    a is the trace of the latin square, and b and c are the number of duplicate
    rows and columns respectively.
    """


    print("Case #{}: {} {} {}".format(case,trace,duplicateRows,duplicateColumns))



def main():
    """
    This function reads standard input and passes data around to the 
    functions that actually solve and print the result. 
    
    It keeps track of the current test case along the way.
    """


    tCases = int(sys.stdin.readline())  # Total Test Cases
    currentTestCase = 1

    while(currentTestCase <= tCases):
        size = int(sys.stdin.readline())  # Size of square matrix
        matrix = []
        
        for i in range(size):
            currentRow = sys.stdin.readline().split()
            matrix.append(currentRow)  # Square matrix is stored as a list of lists
        
        trace,duplicateRows,duplicateColumns = solve(matrix,size)

        output(currentTestCase,trace,duplicateRows,duplicateColumns)    
        
        currentTestCase+=1

main()
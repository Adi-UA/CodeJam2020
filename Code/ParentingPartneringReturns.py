import sys

def solve(originalChoreList):
    """
    This function assigns chores as follows:

    1) We copy the original chore list into a new list such that the list
    references themselves are different, but the value references are the same.

    2) Sort the new chore list by the chore start times.

    3) We then set two variables to keep track of when James and Cameron are finising
    their last assigned chore. This is 0 by default.

    4) Iterate. For each chore in the new ordered chore list, we extract the start and
    end times. 

    5) If both James and Cameron are ending their chores AFTER the current start
    time, we can return IMPOSSIBLE.

    6) Otherwise, we first check if Cameron's or James' end times are less than the
    current start time. Depending on who is free we change the 0th index of the current
    chore array to 'C' or 'J'. We now update the person's end time.

    7) Modifying the 0th index of the chore modifies the VALUE in both the original and
    new ordered list. So when we are done iterating the chores, our original list
    has the answers in the original order it wass given.

    8) For the final result, we concatenate chore[0] for all chores in the original list
    into a string and return it.
    """


    choreList = originalChoreList.copy()  # Doesn't create new individual value references
    choreList.sort(key=sortKey)

    JEndTime = 0
    CEndTime = 0


    for chore in choreList:
        startTime = int(chore[0])
        endTime = int(chore[1])

        if(JEndTime > startTime and CEndTime > startTime):
            return "IMPOSSIBLE"
        else:
            if(CEndTime <= startTime):
                chore[0] = 'C'  # Modifies original list too
                CEndTime = endTime
            elif(JEndTime <= startTime):
                chore[0] = 'J'  # Modifies original list too
                JEndTime = endTime

    result = createResult(originalChoreList)
    return result



def createResult(originalChoreList):
    """
    Concatenates the 0th index of every chore in the chore array after
    results have been calculated.
    """


    result = ""
    for x in originalChoreList:
        result+=x[0]
    return result



def sortKey(e):
    """
    This sorts the chores based on their start time. 
    e[0] is the start time for all the chores in my array of chores.
    """


    return int(e[0])



def output(case,result):
    """
    Prints the output in Case #x: y format. Where x is the case no.
    and y is the scheduling string.
    """


    print("Case #{}: {}".format(case,result))



def main():
    """
    This methods reads standard input and passes data around to the 
    methods that actually solve and print the result. 
    
    It keeps track of the current test case along the way.
    """


    tCases = int(sys.stdin.readline())  # Total Test Cases
    currentTestCase = 1

    while(currentTestCase <= tCases):
        chores = int(sys.stdin.readline())
        choreList = []

        for i in range(chores):
            chore = sys.stdin.readline().rstrip().split()
            choreList.append([chore[0],chore[1]])  # Each chore  in choreList is [startTime, endTime]

        result = solve(choreList)
        output(currentTestCase,result)

        currentTestCase+=1
main()
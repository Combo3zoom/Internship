def InputArr(arr,a,b):
    count=0
    countValues=3
    print('Enter number, which more 0 and less 106 ')
    while count !=countValues:
        try:
            number=int(input())
            if(number>a and number<b):
                arr.append(number)
                count +=1
            else:
                print('Try again, number must to be more 0 and less 106 ')
                continue
        except ValueError:
           print("Syntax error, try again ")
           continue 
    return

def OutputArr(arr):
    print(arr)
    return

def SpecialAddition(number1, number2):
    resSum = ''
    while((number1 !=0) or (number2 !=0)):
        currentSum = number1 % 10 + number2 % 10
        number1 //= 10
        number2 //= 10
        resSum = str(currentSum) + resSum
    return int(resSum)

def AddListNumbers(numList):
    resSum = 0;
    for i in numList:
        resSum = SpecialAddition(resSum, i)
    return resSum

def CheckEqualityNumberElements(elemementsList):
    return elemementsList.count(elemementsList[0]) == len(elemementsList)

def IsExpressionAsosiative(arr):
    resSum = []
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            sum = AddListNumbers([arr[i], arr[j], arr[len(arr) - (i + j)]])
            print(sum)
            resSum.append(sum)
    return CheckEqualityNumberElements(resSum)

def OutputResult():
    if (IsExpressionAsosiative(arr)):
        print("Numbers is asosoative")
    else:
        print("Numbers is not asosoative")
    return

while True:
    a,b=0,106
    arr=[]
    InputArr(arr,a,b)
    OutputArr(arr)
    OutputResult()
   
    break

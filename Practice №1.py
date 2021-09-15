

def InputArr(arr):
    count=0
    print('Enter number, which more 0 and less 106 ')
    while count !=3:
        try:
            number=int(input())

            if(number>0 and number<106):
                arr.append(number)
                count +=1
            else:
                print('Try again, number must to be more 0 and less 106 ')
                continue
        except UncorrectValue:
           print("Syntax error, try again ")
           continue 
    return
  
def Adition(number1,number2):
    check=1
    while(check):
        if((number1 !=0) or (number2!=0)):
            allSumInt=number1%10 +number2%10
            number1 = number1 // 10
            number2 = number2 // 10
            allSumString=str(allSumInt)
            check=1
        else:
            check=0
            
    return int(allSumString)


def OutputArr(arr):
    print(arr)


def Asosiate(arr):
    res=[]
    for i in range(3):
        for j in range(i+1,3):
            resSumNumber = AllAdd([arr[i],arr[j],arr[3-i-j]])
            print(resSumNumber)
            res.append(resSumNumber)   
    if(res.count(res[0]) == len(res)):
         print('Expression is asosiate')
    else:
        print("Expression is not asosiate")


    return
        


def AllAdd(newNumbers):
    res=0
    for i in newNumbers:
        res = Adition(i,res)
    return res

while True:
    arr=[]
    InputArr(arr)
    OutputArr(arr)
    Asosiate(arr)

    break
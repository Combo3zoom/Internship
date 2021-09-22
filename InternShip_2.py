from random import uniform

def InputArray(size):
    array=[]
    for i in range(size):
      array.append([])
      for j in range(size):
          array[i] += [float(input())]
    print()
    return array
            

def AutomaticallyInputArray(size,a,b):
    array=[]
    for i in range(size):
      array.append([])
      for j in range(size):
          array[i] += [uniform(a,b)]
    print()
    return array

def OutputArray(array):
    for i in range(len(array)):
        print(array[i])
    print()
    return

def MatrixIndexes(indexIn1DArr, matrixColNum):
    row = indexIn1DArr // matrixColNum
    col = indexIn1DArr - row * matrixColNum
    return row, col

def BinarySearch(array,searchValue):
    lowerLimit=0
    upperLimit=len(array)*len(array)
    while lowerLimit != upperLimit:
        middle = (lowerLimit + upperLimit) // 2
        coordinates = MatrixIndexes(middle, len(array))
        if array[coordinates[0]][coordinates[1]] == searchValue:
            return coordinates
        elif array[coordinates[0]][coordinates[1]] > searchValue:
            upperLimit = middle
        else:
            lowerLimit = middle + 1

    return 'does not exist'

def Sorting(array):
    count=0
    size =len(array)*len(array)
    for run in range(size-1):
        for i in range(len(array)):
            for j in range(len(array)-1):
                if(array[i][j] > array[i][j+1]):
                    array[i][j],array[i][j+1]=array[i][j+1], array[i][j]
                    count +=1     
                if(j==len(array)-2 and i !=len(array)-1):
                    if(array[i][j+1]>array[i+1][0]):
                        array[i][j+1],array[i+1][0]= array[i+1][0],array[i][j+1]
                        count +=1  
    return array,count

def main():
    array=[]
    while True:
        try:      
            print("Enter command \n"
                  "1 - Input matrix manually \n"
                  "2 - Input matrix automatically \n"
                  "3 - Output matrix \n"
                  "4 - Use binary search \n"
                  "5 - Use sorting \n"
                  "exit - exit with program \n")
            userChoose = input()
            if(userChoose=='1'):
                size=int(input("Enter array order: "))
                while(size<=0):
                    size=int(input("Enter array order more 0: "))
                array=InputArray(size)
                continue
            elif(userChoose=='2'):
                size=int(input("Enter array order: "))
                while(size<=0):
                    size=int(input("Enter array order more 0: "))
                print("Also enter the lower and upper limits of the matrix elements:")
                a=float(input("a = "))
                b=float(input("b = "))
                while(a>b):
                    print("a must be less b")
                    a=float(input("a = "))
                    b=float(input("b = "))
                array=AutomaticallyInputArray(size,a,b)
                continue
            elif(userChoose=='3'):
                OutputArray(array)
                continue
            elif(userChoose=='4'):
                if(array==[]):
                    print("fill the array with elements")
                    continue
                value=float(input("Enter value, which your want to found: "))
                a = BinarySearch(array,value)
                print("coordinates ",a )
                continue
            elif(userChoose=='5'):
                if(array==[]):
                    print("fill the array with elements")
                    continue
                count=Sorting(array)[1]
                array=Sorting(array)[0]
                print('Count operation ', count)
                continue
            elif(userChoose=='exit'):
                break
            elif(userChoose !='exit'):
                print('incorrect input, try again')
                continue
        except ValueError:
            print()
            print("Syntax error, try again ")
            print('-----------------------')
            continue
        break 
    return

main()
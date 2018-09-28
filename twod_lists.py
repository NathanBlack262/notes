a = [[1,2,3],
     [4,5,6]]

#One way to traverse a 2D list
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        print(a[i][j],end=' ')
#    print()

#Another way to traverse a 2D list
def print_2D_List(lst):
    for row in lst:
        for element in row:
            print(element,end = ' ')
        print()
        
#Add all elements in a 2D list
#sum = 0
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        sum += a[i][j]
#print(sum)

#sum = 0
#for row in a:
#    for element in row:
#        sum += element
#print(sum)

#Changing elements in 2d lists
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        a[i][j] += 1
#print_2D_List(a)

#Creating a 2D list ***DOES NOT WORK EDITION***
#x = [[0] * 5] * 8
#x[0][0] = 100
#print(x)
 
m = 5
n = 8
x = [[0] * n for i in range(m)]
print(x)


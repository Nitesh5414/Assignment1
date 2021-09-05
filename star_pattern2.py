'''
*
**
***
****
****
***
**
*
'''
rows = int(input("Enter no. of rows: "))
for i in range(0, rows):
    for j in range(0, i+1):
        print("*", end=" ")
    print(" ")                 #change line after each iteration
#for second pattern
for i in range(rows+1, 0, -1):
    for j in range(0, i-1):
        print("*", end=" ")
    print(" ")

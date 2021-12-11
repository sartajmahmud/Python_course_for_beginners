"""
///Nested Conditions
Example problem:
    find leap year using nested condition

solution:
    x=int(input())

    if x%4==0:
        if x%100==0:
            if x%400==0:
                print("leap year")
            else:
                print("not leap year")
        else:
            print("leap year")
    else:
        print("not leap year")


Practice problems:
P1:
*****
  *
  *
  *
*****

P2:
*****
*   *
*   *
*   *
*****

P3:
*   *
*   *
*****
*   *
*   *

"""




"""

//Nested Loops

    column -> 1
    row -> 0
    output : *

    column -> 2
    row -> 0, 1
    output : **

    column -> 3
    row -> 0, 1, 2
    output : ***
    
    column -> 4
    row -> 0, 1, 2, 3
    output : ****
    
    column -> 5
    row -> 0, 1, 2, 3, 4
    output : *****

    example 1:
    
    *
    **
    ***
    ****
    *****
    
    solution :
    for column in range(1,6):
        for row in range(column):
            print('*', end='')
    print()

    //Practice problems for nested loop
    practice 1:
    *****
    ****
    ***
    **
    *

    practice 2:
    *****
     ****
      ***
       **
        *

    practice 3:
        *
       **
      ***
     ****
    *****
    


"""
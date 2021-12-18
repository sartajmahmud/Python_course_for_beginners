# patternLength = int(input())

# for column in range(1, patternLength+1):
#     for row in range(column):
#         print('*', end='')
#     print()

# for column in range(1, patternLength+1):
#     for spaceRow in reversed(range(1,(patternLength+1)-column)):
#         print(' ', end='')
#     for row in range(column):
#         print('*', end='')
#     print()

# for row in range(1,patternLength+1):
#     if row==1 or row==patternLength:
#         for col in range(1,patternLength+1):
#             print("*",end="")
#     else:
#         for col in range(1, patternLength + 1):
#             if col == (patternLength + 1)/2:
#                 print("*", end="")
#             else:
#                 print(" ",end="")
#     print()


#neelavro problem
# for i in range(1, patternLength+1):
#     print(i,end='')
# for i in reversed(range(1, patternLength)):
#     print(i,end='')

for row in range(1, 6):
    for space in range(1,6 - row):
        print("_", end="")
    for star in range(1, row+1):
        print("*", end='')
    print()



    """
    5
    123454321
    
    
    ***** -> 1
    *   *
    *   *
    *   *
    ***** -> 5
    
    
    practice 3:
        **
       ****
      ******
     ********
    **********
    **********
     ********
      ******
       ****
        **
    
     practice 1:
    *****
     ****
      ***
       **
        *
    """
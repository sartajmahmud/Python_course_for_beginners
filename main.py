"""
1. takes a user input for number of line to print patterns
2. takes a user input for number of line to print a diamond of that lines (only odd inputs)
3. a guessing game
4. opens a address book (add, delete, update, and view all addresses)
5. finds factorial of inputted number
6. takes a input and finds addition of a sequence (1,1, 2, 4, 8, 16.........n)
7. takes a input and finds addition of a sequence (1,3, 5, 7, 9, 11.........n)
8. takes a input and finds addition of a sequence (1,4, 9, 16, 25, 36.........n)

"""



def app1():
    print('app1')
def app2():
    print('app2')
def app3():
    print('app3')

def app4():
    print('app4')

def app5():
    print('app5')


def printMenu():
    print('**************')
    print('Press 1 for app1')
    print('Press 2 for app2')
    print('Press 3 for app3')
    print('Press 4 for app4')
    print('Press 5 for app5')
    print('Press 0 for Exit')
    print('**************')


while(True):
    printMenu()
    menuInput = int(input('Enter your choice : '))

    if(menuInput == 1):
        app1()
    elif(menuInput == 0):
        print('Exited')
        break;
keypad = {
    1:'.,?!:',
    2:'ABC',
    3:'DEF',
    4:'GHI',
    5:'JKL',
    6:'MNO',
    7:'PQRS',
    8:'TUV',
    9:'WXYZ',
    0:' ',
}

userInput = "Hello, World!".upper()
index = 0
outputString = ''

while(True):
    for i in range(10):
        for j in range(len(keypad[i])):
            if keypad[i][j] == userInput[index]:
                for k in range(j+1):
                    outputString += str(i)

    index+=1

    if index == len(userInput):
        break


print(outputString)



# dict1={'1':'.,?!:','2':'ABC','3':'DEF','4':'GHI','5':'JKL','6':'MNO','7':'PQRS','8':'TUV','9':'WXYZ','0':' '}
# str1=input()
# str2=str1.upper()
# str3=""
# for i in range(len(str2)):
#     for j,value in dict1.items():
#         if str2[i] in value:
#             for x in range(1,value.find(str2[i])+2):
#                 str3=str3+j
# print(str3)
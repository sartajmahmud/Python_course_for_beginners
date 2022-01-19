inputNumber = 0
outputDict = {}

while(True):
    inputNumber = inputNumber + 1

    userInput = input() #user input -> "OMEGA 10000" / "STOP"

    if userInput == 'STOP':
        break
    else:
        inputParts = userInput.split(' ') # if input -> "OMEGA 10000" -> splited list will be -> ['OMEGA','10000']

        firstTwoLetter = inputParts[0][0:2]

        if inputParts[0] in outputDict:   # searches for previous keys with the new input brand name

            outputDict[inputParts[0]].append(str(inputNumber)+"_"+firstTwoLetter+'_'+inputParts[1])
        else:
            outputDict[inputParts[0]] = []
            outputDict[inputParts[0]].append(str(inputNumber)+"_"+firstTwoLetter+'_'+inputParts[1])

print(outputDict)


# dictX = {}
# dictX['KOTKA'] = []
#
# dictX['KOTKA'].append('1_KO_1000')
# dictX['KOTKA'].append('2_KO_3000')
#
# print(dictX)

"""Write a python program that will take input from the user until the user
gives “STOP” as input. In every line the user will provide input as follow:
[Brand Name] [PRICE]
Your task is to create a dictionary where the brand’s name will be key and
the value will be a list of that brand’s watches ID. ID generate process:
inputno_FirstTwoLetterOfBrand_Price. Finally print the dictionary.

Sample Input 1:
OMEGA 10000
TITAN 5000
TITAN 3000
CREDENCE 150000
OMEGA 12000
CREDENCE 90000
STOP
Sample Output 1:
{
'OMEGA': ['1_OM_10000', '5_OM_12000'], 
'TITAN':['2_TI_5000', '3_TI_3000'], 
'CREDENCE': ['4_CR_150000', '6_CR_90000']
} 


 OMEGA 1000 its a 1st input -> 1               The value of inputCounter is now 1          inputCounter = inputCounter + 1

 [0]-> OMEGA                                   Found the Brand name "OMEGA"                userInput.split(' ')[0]
 [1] -> 1000                                   FOUND the price of the watch                userInput.split(' ')[1]

 first 2 letter -> OM                          FOUND the first two letter of the brand     userInput.split(' ')[0][0:2]

 1_OM_1000                                     Processed output String                     str(inputCounter)+'_'+userInput.split(' ')[0][0:2]+'_'+userInput.split(' ')[1]

 {'OMEGA' : []}                                dictX[userInput.split(' ')[0]] = []
 {'OMEGA' : ['1_OM_1000']}                     dictX[userInput.split(' ')[0]].append(str(inputCounter)+'_'+userInput.split(' ')[0][0:2]+'_'+userInput.split(' ')[1])




"""


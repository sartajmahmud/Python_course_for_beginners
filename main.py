"""
///Loops
1. For Loop

for <variable> in range([startingValue], limiting Value, [increment/decrement]):
    <body>

for <variable> in <A set of data>:
    <body>
else:
    <else body works only when the loop breaks>

//remember these keywords
break
pass
continue

2. While Loop

i = 0  -> STEP 1 Initialization

while <Condition>:  -> STEP 2 Condition
    <body>          -> STEP 3 body

    <increment>     -> STEP 4 Update/Increment/Decrement



HW -> Solve 1018 and 1019 no problem from beecrowd.com.br
"""






for i in range(5):
    if i == 3:
        continue
    print(i)
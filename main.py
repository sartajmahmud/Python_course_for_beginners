"""
Data Types

Integer -> int -> 10
Double/Float -> float -> 10.23
Character -> char
String -> str -> 'This is String' (String is basically a set of Characters)
Boolean -> bool -> True/False
"""

"""
Casting

int() -> to cast other data types to integer datatype
float() -> to cast other data types to Float datatype
str() -> to cast other data types to String datatype
"""

"""
Arithmetical Operator

+ , - , *, / , % , ** , //

Logical Operator

and or not  

Assignment Operator

= , +=, -= , *=, /=, %=

Comparison Operator

== , != , > , < , >= , <=

"""

"""
Conditional Statements

//if else elif  (Conventional Way)

if <Condition>:
    body
elif <Condition>:
    body
else:
    body
     
     
//Shortcut/Ternary Operator/ConditionExpression

<body if true> if <condition> else <body if false> 
"""

number = 35

if number<30:
    print('less then 30')
elif number<40:
    pass
elif number<50:
    print('less then 50')
else:
    print('Greater than 50')


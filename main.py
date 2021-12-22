# """
# Encapsulcation
#
# 1. Getter functions/methods
# 2. Setter function/methods
# """
#
#
# class Person:
#
#     def __init__(self,name, address, phonenumber = None):
#         self.name = name
#         self.address = address
#         self.phoneNumber = phonenumber
#
#
#     def printData(self):
#         print("Name is the object : ",self.name)
#         print("Address is the object : ",self.address)
#         print("PhoneNumber is the object : ",self.phoneNumber)
#
#     def getPhoneNumber(self):
#         return self.phoneNumber
#
#     def setPhoneNumber(self, newPhoneNumber):
#         self.phoneNumber = newPhoneNumber
#
#
# person1 = Person('saaaad','kamala',123)
# # person2 = Person('sajjad','lalmaa',123465)
#
# #
# # person1.phoneNumber = 123456789
# # person2.phoneNumber = 987654321
#
# print(person1.getPhoneNumber())
#
# person1.setPhoneNumber(654321)
#
# print(person1.getPhoneNumber())
#
# # Person('Umama','Dhanmondi',123).printData()
# #
# # person1.printData()
# #
# # person2.printData()
#


# x = 10
#
# def getX():
#     return x
#
# def setX(value):
#     global x
#     x = value
#
#
# setX(200)
#
# print(getX())

import Person

# Method Overloading

person1 = Person.Person('Sartaj', 'Uttara')
person2 = Person.Person('Neelavro', 'Shankar', 7689)

# print(person1.name)
# print(person1.address)
# print(person1.phoneNumber)
#
# print(person2.name)
# print(person2.phoneNumber)


def addValues(num1, num2, num3=0):
    return num1+num2+num3

print(addValues(5,5))
print(addValues(5,5,10))


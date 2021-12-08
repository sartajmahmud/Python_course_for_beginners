"""
///List //ArrayList

Lists are dynamically changeable
in List we can store duplicate values
<listName> = [<index 0>, <index 1>, .... ,<index N>]

append(<Val>) //Adds items to the list
insert(<index>,<Val>) //Adds items to specific index in the list
pop(<index>) //Removes specific indexed value from the list
remove(<Val>) //Removes specific value from the list

names = ['Sartaj']
names.append('Neelavro') # ['Sartaj', 'Neelavro']
names.append('Neelavro') # ['Sartaj', 'Neelavro']
names.append('Neelavro') # ['Sartaj', 'Neelavro']
names.append('Umama') # ['Sartaj', 'Neelavro', Umama]

names.insert(2,'Shafin')

names.pop(4)

names.remove('Neelavro')

print(names)



///Tuple
<tupleName> = (<index 0>, <index 1>, .... ,<index N>)

Tuples are not changeable like list
in Tuples we can store duplicate values


///Sets
<tupleName> = {<index 0>, <index 1>, .... ,<index N>}

Sets are not changeable like list
in Sets we can't store duplicate values


///Dictionary //HashMap
Dictionary is the fast setDataType
has the fastest time complexity
more readable than list

<dictionaryName> = {<key>:<value>, <key>:<value>, ..... ,<key>:<value>}

//new entry
<dictionaryName>['newKeyName'] = <val>

//update existing value
<dictionaryName>.update({<keyName>: <newValue>})

//remove a specific pair
<dictName>.pop(<keyname>)
//remove last pair
<dictName>.popitem()


////HW problem 1021 -> using while loop only
"""

userData = {'id':1, 'name':'Sartaj', 'height':5.7}

userData['phone'] = 8801796406262
userData.update({'full_name': 'Sartaj'})

userData.popitem()

print(userData)

def makeMatrix(isItDict, elements, columnNum):
    lst = []
    counter = 1
    if isItDict:
        for key, value in elements.items():
            lst.append(value)
    else:
        for element in elements:
            lst.append(element)
            
    listoflists = []
    sublist = []
    j = 0
    for i in lst:
        if j < columnNum:
            sublist.append(i)
            j += 1
        else:
            listoflists.append(sublist)
            sublist = []  
            sublist.append(i)
            j = 1
    
    listoflists.append(sublist)
    print(listoflists)
    return 

a = {'foo': 1, 'baz': 2, 'hello': 5, 'fdoo': 6, 'bdaz': 8, 'heldlo': 9}
b = [1, 5, 6, 9, 8, 5, 4]
makeMatrix(True, a, 2)
makeMatrix(False, b, 3)


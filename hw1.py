counter = 0
with open('test.txt') as f:
    for line in f:
        for word in line.split():
            if counter < 21:
                if counter < 15:
                    print(word[:5], end=' ')
                    counter += len(word[:5]) + 1
                else:
                    temp = 20 - counter
                    print(word[:temp], end=' ')
                    counter += len(word[:temp]) + 1
                    
            else:
                print()
                counter = 0

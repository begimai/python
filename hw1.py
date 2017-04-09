counter = 0
wCounter = 0
with open('test.txt') as f:
    for line in f:
        for word in line:
            if counter < 20: 
                counter += 1
                wCounter += 1
                if word == ' ' or word == '\n':
                    wCounter = 0
                if wCounter < 6:
                    print(word, end='')
            else:
                counter = 0
                wCounter = 0
                print('')

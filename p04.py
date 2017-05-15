counter = 0
result = ''
file = 'test.txt'

def readFromFile():
    with open(file) as f:
        global counter
        global result
        lines = f.readlines() 
        for line in lines:
            line = line.replace('\n', '')
            words = line.split(' ')
            for word in words:
                if word != '':
                    counter += 1
                    if counter == 10:
                        yield result
                        result = ''
                        counter = 0
                    else:
                        result += word + ' '
    if result != '':
        yield result

def count(line):
    l = len(line.replace(' ', ''))
    words = line.split(' ')
    print('words:    ', len(words))
    print('chars:    ', l)
    print('avg  :     %.2f' % (l/len(words)))

for line in readFromFile():
    print(line)
    count(line)

from collections import defaultdict

tempWord = ''

def refactor(fromFile, shortWords):
    d = {}
    tempWord = ''
    for line in shortWords:
        words = line.split()
        d[words[0]] = ' '.join(words[1:])
    with open(fromFile) as f:
        for line in f:
            words = line.split()
            if tempWord != '':
                words[0] = tempWord[:-1] + words[0]
                tempWord = ''
            if line[-2] == '-':
                tempWord = words[-1]
                words.pop(-1)
                
            for i, word in enumerate(words):
                for key in d:
                    if word.lower() == key.lower():
                        words[i] = d.get(key)
            yield (' '.join(words))
        f.close()
    return 

def cleanUp(line):
    global tempWord
    for char in line:
        if char.isdigit():
            tempWord += ''
        elif char.isalpha() or char == '\'':
            tempWord += char.lower()
        elif char != ' ':
            if tempWord.strip() != '':
                yield (tempWord.strip())
                tempWord = ''
        else:
            tempWord += ' '
    tempWord += ' '
    return 

def removeJoinWordsFromFile(line, joinWords):
    line = ' ' + line + ' '
    for word in joinWords:
        word = word.strip()
        word = ' ' + word.lower() + ' '
        line = line.replace(word, ' ')
    yield (line.strip())
    return 

def removeConjuctionsFromFile(line, shorts):
    line = ' ' + line + ' '
    for short in shorts:
        short = ' ' + short.strip() + ' '
        line = line.replace(short, '\n')
    yield (line.strip())
    return 

def countOccurrences(text):
    d = {}
    d = defaultdict(dict)
    prevWord = ''
    for line in text:
        line = line.split(' ')
        for item in line:
            if prevWord != '':
                if prevWord in d:
                    if item in d[prevWord]:
                        d[prevWord][item] += 1
                    else:
                        d[prevWord][item] = 1
                else:
                    d[prevWord][item] = 1
            prevWord = item
        prevWord = ''
    for item in d:
        l = len(d[item].keys())
        for e in d[item]:
            print(item, '-', e, ': ' '%.2f' % (d[item][e] / l))
    return 

shortWords = []
with open('shorts.txt') as l:
    for word in l:
        shortWords.append(word)

joinWords = []
with open('joinWords.txt') as l:
    for word in l:
        joinWords.append(word)

conjWords = []
with open('conjunctions.txt') as l:
    for word in l:
        conjWords.append(word)
        
temp = []
for line in refactor('test.txt', shortWords):
    for lin in cleanUp(line):
        for li in removeJoinWordsFromFile(lin, joinWords):
            for l in removeConjuctionsFromFile(li, conjWords):
                temp.append(l)
        
countOccurrences(temp)


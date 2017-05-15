from collections import defaultdict

def refactor(fromFile, file):
    d = {}
    lst = []
    tempWord = ''
    with open(fromFile) as f, open(file) as l:
        for line in l:
            words = line.split()
            d[words[0]] = ' '.join(words[1:])
            
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
            lst.append(' '.join(words))
        f.close()
        l.close()
    return lst

def cleanUp(text):  
    lst = []
    tempWord = ''
    for line in text:
        for char in line:
            if char.isdigit():
                tempWord += ''
            elif char.isalpha() or char == '\'':
                tempWord += char.lower()
            elif char != ' ':
                if tempWord.strip() != '':
                    lst.append(tempWord.strip())
                    tempWord = ''
            else:
                tempWord += ' '
        tempWord += ' '
    return lst

def removeConjuctionsFromFile(text, file):
    lst = []
    with open(file) as l:
        for line in text:
            line = ' ' + line + ' '
            l.seek(0, 0)
            for word in l:
                word = ' ' + word.strip() + ' '
                line = line.replace(word, '\n')
            lst.append(line)
        l.close()
    text = []
    for line in lst:
        line = line.strip()
        line = line.split('\n')
        for item in line:
            text.append(item)
    return text

def removeJoinWordsFromFile(text, file):
    lst = []
    with open(file) as l:
        for line in text:
            line = ' ' + line + ' '
            l.seek(0, 0)
            for word in l:
                word = word.strip()
                word = ' ' + word.lower() + ' '
                line = line.replace(word, ' ')
            lst.append(line.strip())
        l.close()
    return lst

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
    return d

#to make I'll to I will
#short words goes like        you're you are
text = refactor('test.txt', 'shorts.txt')

#to make lowercase + remove non alpha chars
text = cleanUp(text)

#to remove conjuctions
#conjuctions are listed one per a line
text = removeConjuctionsFromFile(text, 'conjunctions.txt')

#to remove nums, articles and not
#join words are listed one per a line
text = removeJoinWordsFromFile(text, 'joinWords.txt')

#to count occurrence of words
countOccurrences(text)

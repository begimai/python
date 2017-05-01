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
            lst.append('\n')

        f.close()
        l.close()
                
    with open(fromFile, 'w') as f:
        for line in lst:
            if line.strip() != '':
                f.write(line.strip())
                f.write('\n')
        f.close()
    return

def cleanUp(file):
    lst = []
    tempWord = ''
    with open(file) as f:
        for line in f:
            for char in line:
                if char.isalpha() or char == '\'':
                    tempWord += char.lower()
                elif char == '\n':
                    tempWord += ' '
                elif char != ' ':
                    lst.append(tempWord + ' \n')
                    tempWord = ''
                else:
                    tempWord += ' '
        f.close()
    with open(file, 'w') as f:
        for line in lst:
            if line.strip() != '':
                f.write(line.strip())
                f.write('\n')
        f.close()
    return

def removeConjuctionsFromFile(fromFile, file):
    lst = []
    with open(fromFile) as f, open(file) as l:
        for line in f:
            line = line.strip()
            line = ' ' + line + ' '
            l.seek(0, 0)
            for word in l:
                word = word.strip()
                word = ' ' + word.lower() + ' '
                line = line.replace(word , '\n')
            lst.append(line)
        f.close()
        l.close()
                
    with open(fromFile, 'w') as f:
        for line in lst:
            if line.strip() != '':
                f.write(line.strip())
                f.write('\n')
        f.close()
    return

def removeJoinWordsFromFile(fromFile, file):
    lst = []
    with open(fromFile) as f, open(file) as l:
        for line in f:
            line = line.strip()
            line = ' ' + line + ' '
            l.seek(0, 0)
            for word in l:
                word = word.strip()
                word = ' ' + word.lower() + ' '
                line = line.replace(word, ' ')
            lst.append(line)
        f.close()
        l.close()
                
    with open(fromFile, 'w') as f:
        for line in lst:
            if line.strip() != '':
                f.write(line.strip())
                f.write('\n')
        f.close()
    return

def countOccurrences(fromFile):
    d = {}
    with open(fromFile) as f:
        for line in f:
            words = line.split()
            for word in words:
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1
        for key in d:
            print(key + ': ' + str(d.get(key)))
    return

def wordsAfterOthers(fromFile):
    d = {}
    prevWord = ''
    with open(fromFile) as f:
        for line in f:
            words = line.split()
            for word in words:
                if prevWord != '':
                    if prevWord + ' followed by ' + word in d:
                        d[prevWord + ' followed by ' + word] += 1
                    else:
                        d[prevWord + ' followed by ' + word] = 1
                prevWord = word

            prevWord = ''
        for key in d:
            print(key + ': ' + str(d.get(key)))
    return

#to make I'll to I will
#short words goes like        you're you are
refactor('test.txt', 'shorts.txt')

#to make lowercase + remove non alpha chars
cleanUp('test.txt')

#to remove conjuctions
#conjuctions are listed one per a line
removeConjuctionsFromFile('test.txt', 'conjunctions.txt')

#to remove nums, articles and not
#join words are listed one per a line
removeJoinWordsFromFile('test.txt', 'joinWords.txt')

#to count occurrence of words
countOccurrences('test.txt')

#to count words that follow others
wordsAfterOthers('test.txt')

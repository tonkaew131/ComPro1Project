wordsList = []

def checkWord(targetWord, currWord):
    # Is word empty
    if(len(currWord) == 0):
        return

    # Is word wrong size
    if(len(currWord) != 5):
        return

    # Is word a word
    if(currWord not in wordsList):                 
        return

    # print(currWord, targetWord)

    # Create dict of each letter count of Target Word
    targetWordCount = {}
    for c in targetWord:
        if(c in targetWordCount):
            targetWordCount[c] += 1
        else:
            targetWordCount[c] = 1

    currWordState = {}
    # Check for exact match
    for idx, char in enumerate(currWord):
        if(char == targetWord[idx]):
            # Remove Exact Match from Target Word's letter count
            targetWordCount[char] -= 1

            # Exact Match, green color
            currWordState[idx] = {
                'char': char,
                'color': 'green'
            }
        else:
            # Not Exact Match, can be yellow, or gray
            currWordState[idx] = {
                'char': char,
                'color': 'gray'
            }

    for idx, char in enumerate(currWord):
        # Is there is any char in Target Word
        if(char in targetWord):
            if(targetWordCount[char] != 0):
                # If not Exact Match but exist in word, yellow color
                if(currWordState[idx]['color'] != 'green'):
                    currWordState[idx]['color'] = 'yellow'

                    targetWordCount[char] -= 1
                # No more words left, gray color
                elif(targetWordCount[char] < 1):
                    currWordState[idx]['color'] = 'gray'

    # Set Color, and Char
    # for idx in currWordState:
    #     color = currWordState[idx]['color']
    #     if(color == 'green'):
    #         print('🟩', end='')
    #     elif(color  == 'yellow'):
    #         print('🟨', end='')
    #     elif(color  == 'gray'):
    #         print('⬛', end='')
    # print('')
    return currWordState

def checkWord2(targetWord, currWord):
    # Is word empty
    if(len(currWord) == 0):
        return

    # Is word wrong size
    if(len(currWord) != 5):
        return

    # Is word a word
    if(currWord not in wordsList):                 
        return

    # print(currWord, targetWord)

    # Create dict of each letter count of Target Word
    targetWordCount = {}
    for c in targetWord:
        if(c in targetWordCount):
            targetWordCount[c] += 1
        else:
            targetWordCount[c] = 1

    currWordState = {}
    # Check for exact match
    for idx, char in enumerate(currWord):
        if(char == targetWord[idx]):
            # Remove Exact Match from Target Word's letter count
            targetWordCount[char] -= 1

            # Exact Match, green color
            currWordState[idx] = {
                'char': char,
                'color': 'green'
            }
        else:
            # Not Exact Match, can be yellow, or gray
            currWordState[idx] = {
                'char': char,
                'color': 'gray'
            }

        # Is there is any char in Target Word
        if(char in targetWord):
            if(targetWordCount[char] != 0):
                # If not Exact Match but exist in word, yellow color
                if(currWordState[idx]['color'] != 'green'):
                    currWordState[idx]['color'] = 'yellow'

                    targetWordCount[char] -= 1
                # No more words left, gray color
                elif(targetWordCount[char] < 1):
                    currWordState[idx]['color'] = 'gray'

    # Set Color, and Char
    # for idx in currWordState:
    #     color = currWordState[idx]['color']
    #     if(color == 'green'):
    #         print('🟩', end='')
    #     elif(color  == 'yellow'):
    #         print('🟨', end='')
    #     elif(color  == 'gray'):
    #         print('⬛', end='')
    # print('')
    return currWordState

try:
    f = open('words', 'r')
    wordsList = f.read().split('\n')
    f.close()
except:
    print('Can\'t Find Words list File, exiting...')
    exit()
print(f'Loaded {len(wordsList)} words')

count = 0
wrongCount = 0
total = 0
for i in wordsList:
    for j in wordsList:
        a = checkWord(i, j)
        b = checkWord2(i, j)

        total += 1
        if(a == b):
            count += 1
        else:
            wrongCount += 1
            print(f'{wrongCount}/{total}', i, j)
            print('ori', a)
            print('mok', b)
            print('')
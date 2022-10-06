from tkinter import *
from tkinter import messagebox

import random

# Global Game Variable
entryList = []          # Store all Entry
buttonList = {}         # Store all Keyboard's Button
textVariableList = []   # Store all Entry's TextVariable
wordsList = []          # Wordle's words list
answerVariable = None   # Answer Entry box's TextVariable
targetWord = ''         # Current Game's target word
currRow = 0             # Current Game's playing row


def drawButton(text='', row=0, rowspan=1, column=0, columnspan=1, width=100, height=100, command=None, keyboard=False):
    frame = Frame(root, width=width, height=height)
    button = Button(frame, text=text, command=command)
    if(keyboard):
        button = Button(frame, text=text,
                        command=lambda: onKeyboardClick(text))

    frame.grid_propagate(False)         # Disables resizing of frame
    frame.columnconfigure(0, weight=1)  # Enables button to fill frame
    frame.rowconfigure(0, weight=1)

    frame.grid(row=row, column=column, rowspan=rowspan,
               columnspan=columnspan, padx=5, pady=5)
    button.grid(sticky='wens')
    return button


def drawSquareEntry(textvariable, row=0, rowspan=1, column=0, columnspan=1, width=100, height=100):
    frame = Frame(root, width=width, height=height)
    entry = Entry(frame, textvariable=textvariable, justify='center',
                  foreground='white', font='Helvetica 24 bold')

    frame.grid_propagate(False)         # Disables resizing of frame
    frame.columnconfigure(0, weight=1)  # Enables button to fill frame
    frame.rowconfigure(0, weight=1)

    frame.grid(row=row, column=column, rowspan=rowspan,
               columnspan=columnspan, padx=5, pady=5)
    entry.grid(sticky='wens')
    return entry


def initKeyboardGUI():
    keyboardLayout = [
        'QWERTYUIOP',
        'ASDFGHJKL',
        'ZXCVBNM'
    ]

    offset = [0, 1, 3]
    startRow, startColumn = 19, 1

    # Draw Keyboard Key
    for inxRow, row in enumerate(keyboardLayout):
        placeRow = startRow + (2 * inxRow)
        for inxCol, text in enumerate(list(row)):
            placeColumn = startColumn + (2 * inxCol) + offset[inxRow]

            btn = drawButton(text, width=40, height=40,
                             row=placeRow, rowspan=2,
                             column=placeColumn, columnspan=2, keyboard=True
                             )
            buttonList[text.lower()] = btn

    # Enter Button
    drawButton('Enter', row=23, rowspan=2, column=1,
               columnspan=3, width=40 / 2 * 3, height=40, command=checkWord)

    # Return Button
    drawButton('<=', row=23, rowspan=2, column=18,
               columnspan=3, width=40 / 2 * 3, height=40)


def initDisplay():
    startRow, startColumn = 4, 6

    # Display 6 x 5
    for inxRow in range(6):
        placeRow = startRow + (2 * inxRow)
        textVariableRow = []
        entryRow = []
        for inxCol in range(5):
            placeColumn = startColumn + (2 * inxCol)

            str = StringVar()
            textVariableRow.append(str)

            entry = drawSquareEntry(str,  width=40, height=40,
                                    row=placeRow, rowspan=2,
                                    column=placeColumn, columnspan=2
                                    )
            entry['state'] = DISABLED
            entry['disabledbackground'] = 'white'
            entry['disabledforeground'] = 'white'
            entryRow.append(entry)
        textVariableList.append(textVariableRow)
        entryList.append(entryRow)

    # Answer Box
    Label(root, text='Answer: ').grid(
        row=17, column=6, columnspan=4, pady=15)

    global answerVariable
    answerVariable = StringVar()

    entryAnswer = Entry(root, textvariable=answerVariable)
    entryAnswer.grid(row=17, column=10, columnspan=6, pady=15)
    entryAnswer.bind('<Return>', checkWord)
    entryAnswer.focus()


def onKeyboardClick(key):
    currWord = answerVariable.get()
    currWord += key.lower()
    answerVariable.set(currWord)


def checkWord(event=None):
    currWord = answerVariable.get().strip().lower()

    # Is word empty
    if(len(currWord) == 0):
        messagebox.showinfo('Please enter again', 'Word can\'t be emptied!')
        return

    # Is word wrong size
    if(len(currWord) != 5):
        messagebox.showinfo('Please enter again', 'Word size must be 5!')
        return

    # Is word a word
    if(currWord not in wordsList):
        messagebox.showinfo('Please enter again', 'Not in word list!')
        return

    print(currWord, targetWord)

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

    global currRow
    # Set Color, and Char
    for idx in currWordState:
        if(currWordState[idx]['color'] == 'green'):
            print('🟩', end='')
        elif(currWordState[idx]['color'] == 'yellow'):
            print('🟨', end='')
        elif(currWordState[idx]['color'] == 'gray'):
            print('⬛', end='')

        textVariableList[currRow][idx].set(currWordState[idx]['char'].upper())
        # entryList[currRow][idx]['background'] = currWordState[idx]['color']
        entryList[currRow][idx]['disabledbackground'] = currWordState[idx]['color']
        entryList[currRow][idx]['state'] = DISABLED

        buttonList[currWordState[idx]['char']
                   ]['background'] = currWordState[idx]['color']
        buttonList[currWordState[idx]['char']]['foreground'] = 'white'
    print('')

    answerVariable.set('')
    currRow += 1

    # Answer is correct
    if(currWord == targetWord):
        messagebox.showinfo('You won!', 'Congratulations, You won!')
        gameCycle()
        return


def gameCycle():
    # Pick random words
    # random.seed('Can I get A dai mai, Ajarn')  # Just for testing
    global targetWord
    targetWord = random.choice(wordsList)

    # Reset Counter
    global currRow
    currRow = 0
    for idxRow, row in enumerate(textVariableList):
        for idxCol, textVar in enumerate(row):
            textVar.set('')

            entryList[idxRow][idxCol]['disabledbackground'] = 'white'

    for btn in buttonList:
        # Default Button Color
        buttonList[btn]['background'] = 'SystemButtonFace'
        buttonList[btn]['foreground'] = 'black'


if __name__ == '__main__':
    root = Tk()
    root.title('Wordle')

    root.rowconfigure(tuple(range(22)), weight=1, minsize=1)
    root.columnconfigure(tuple(range(22)), weight=1, minsize=1)

    # Draw Title
    Label(root, text='Wordle', font='Helvetica 24 bold').grid(
        row=1, column=1, rowspan=2, columnspan=20)

    # Draw Components
    initKeyboardGUI()
    initDisplay()

    # Load Words List
    f = open('words', 'r')
    wordsList = f.read().split('\n')
    print(f'Loaded {len(wordsList)} words')

    # Main Game Cycle
    gameCycle()

    root.mainloop()

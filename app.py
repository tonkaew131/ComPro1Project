from tkinter import *


def drawButton(text='', row=0, rowspan=1, column=0, columnspan=1, width=100, height=100):
    frame = Frame(root, width=width, height=height)
    button = Button(frame, text=text)

    frame.grid_propagate(False)         # Disables resizing of frame
    frame.columnconfigure(0, weight=1)  # Enables button to fill frame
    # Any positive number would do the trick
    frame.rowconfigure(0, weight=1)

    frame.grid(row=row, column=column, rowspan=rowspan,
               columnspan=columnspan, padx=5, pady=5)
    button.grid(sticky='wens')


def drawSquareEntry(textvariable, row=0, rowspan=1, column=0, columnspan=1, width=100, height=100):
    frame = Frame(root, width=width, height=height)
    entry = Entry(frame, textvariable=textvariable, justify='center')

    frame.grid_propagate(False)         # Disables resizing of frame
    frame.columnconfigure(0, weight=1)  # Enables button to fill frame
    frame.rowconfigure(0, weight=1)

    frame.grid(row=row, column=column, rowspan=rowspan,
               columnspan=columnspan, padx=5, pady=5)
    entry.grid(sticky='wens')


def initKeyboardGUI():
    keyboardLayout = [
        'QWERTYUIOP',
        'ASDFGHJKL',
        'ZXCVBNM'
    ]

    offset = [0, 1, 3]
    startRow, startColumn = 17, 1

    # Draw Keyboard Key
    for inxRow, row in enumerate(keyboardLayout):
        placeRow = startRow + (2 * inxRow)
        for inxCol, text in enumerate(list(row)):
            placeColumn = startColumn + (2 * inxCol) + offset[inxRow]

            drawButton(text, width=40, height=40,
                       row=placeRow, rowspan=2,
                       column=placeColumn, columnspan=2
                       )

    # Enter Button
    drawButton('Enter', row=21, rowspan=2, column=1,
               columnspan=3, width=40 / 2 * 3, height=40)

    # Return Button
    drawButton('<=', row=21, rowspan=2, column=18,
               columnspan=3, width=40 / 2 * 3, height=40)


def initDisplay():
    startRow, startColumn = 4, 6

    str = StringVar()
    str.set('X')
    for inxRow in range(6):
        placeRow = startRow + (2 * inxRow)
        for inxCol in range(5):
            placeColumn = startColumn + (2 * inxCol)

            drawSquareEntry(str,  width=40, height=40,
                            row=placeRow, rowspan=2,
                            column=placeColumn, columnspan=2
                            )


if __name__ == '__main__':
    root = Tk()
    root.title('Wordle')

    root.rowconfigure(tuple(range(22)), weight=1, minsize=1)
    root.columnconfigure(tuple(range(22)), weight=1, minsize=1)

    # Draw Title
    Label(root, text='Wordle').grid(row=1, column=1, rowspan=2, columnspan=20)

    initKeyboardGUI()
    initDisplay()

    root.mainloop()

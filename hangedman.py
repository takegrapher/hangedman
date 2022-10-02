import random

def hangman(word):
    wrong = 0
    stages = ["",
              "_________        ",
              "|        |       ",
              "|        |       ",
              "|        O       ",
              "|       /|\      ",
              "|       / \      ",
              "|                "
              ]

    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print ("Welcome to Hangman!")

    while wrong < len (stages) -1:
        print ("\n")
        msg = "一文字予想してね"
        char = input (msg)
        if char in rletters:
            cind = rletters.index (char)
            board[cind] = char
            rletters[cind] = '$'

        else:
            wrong += 1

        print (" ".join(board))
        e = wrong + 1
        print ("\n".join(stages[0:e]))
        if "_" not in board:
            print ("You Won!")
            print (" ".join(board))
            win = True
            break

    if not win:
        print ("\n".join(stages[0:wrong+1]))
        print ("You lose! the answer was {}".format(word))

def rword():
    i = random.randint (0,9)
    wlist = ["cat", "dog", "cow", "sheep", "mouse", "pig", "monky", "rat", "human", "goat"]
    return wlist[i]


hangman(rword())

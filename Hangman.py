#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# p139 Chapter 10 Challenge 1

import random

def hangman(answers):
    answer = answers[random.randrange(len(answers))]
    wrong = 0
    stages = ["",
              "________        ",
              "|       |       ",
              "|       |       ",
              "|       0       ",
              "|      /|\      ",
              "|      / \      "
             ]
    rletters = list(answer)
    board = ["_"] * len(answer)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}.".format(word))

answers = ["cat", "dog", "cow", "pig", "rat"]
hangman(answers)


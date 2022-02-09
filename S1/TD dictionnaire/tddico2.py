"""
@author: Thomas PREVOST (FISE24) @ ENSTA B
@date: 11/10/2021
"""
import numpy as np
from bintrees import FastRBTree, FastAVLTree
import matplotlib.pyplot as plt
import time

punct = [',', '.', '\'', '\"', "(", ")", ">", "<", "!", "?"]


def openAsStr(file):
    f = open(file)
    content = f.read()
    f.close()
    return content


def openAsLst(file, n=-1):
    if n <= 0:
        f = open(file)
        content = f.read()
        f.close()
        return content.split("\n")
    else:
        f = open(file)
        content = f.read(n)
        f.close()
        return content.split("\n")


def clean(s):
    s = s.replace("\n", " ")
    for p in punct:
        s = s.replace(p, "")
        s = s.lower()
    tmp = s.split(" ")
    res = []
    for e in tmp:
        if e != "":
            res.append(e)
    return res


def trees():
    avl = FastAVLTree()
    rbt = FastRBTree()

    word = 'test'
    avl.insert(word, None)
    rbt.insert(word, None)

    if word in avl and word in rbt:
        print('ok')
    else:
        print("Erreur d'indexation")


if __name__ == "__main__":
    text = clean(openAsStr("files/text.txt"))
    print(text)
    print(len(text))
    dico = openAsLst('files/dico_gb.txt')
    n = 0
    for w in text:
        if w in dico:
            n += 1
    print(n)
    # print(openAsLst('files/dico_gb.txt'))

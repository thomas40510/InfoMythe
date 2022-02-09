# -*- coding: utf-8 -*-
"""
@author: Christophe Osswald. WTFPL.
"""

from pylab import *

absc = ordo = None


def draw(pd, pf):
    global absc, ordo
    if not absc:
        absc = [pd[0]]
        ordo = [pd[1]]
    absc.append(pf[0])
    ordo.append(pf[1])


def draw_koch():
    axis('equal')
    plot(absc, ordo)
    show()


def longueur():
    long = 0.
    for i in range(len(absc) - 1):
        long += ((absc[i] - absc[i + 1]) ** 2 + (ordo[i] - ordo[i + 1]) ** 2) ** 0.5
    return long
